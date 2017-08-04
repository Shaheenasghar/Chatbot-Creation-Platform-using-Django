# FYPfinal/fbbot/views.py
import logging
from django.conf import settings
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from pymessenger.bot import Bot
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Partner

# Get an instance of a logger
logger = logging.getLogger(__name__)
bot = Bot(settings.FB_ACCESS_TOKEN, app_secret=settings.FB_APP_SECRET)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def webhook(request, partner_id):
    partner = Partner.objects.get(id=partner_id);
    print(partner_id, partner.token, partner.secret, partner.page_id)
    bot = Bot(partner.token, app_secret=partner.secret)
    if request.method == 'GET':
        verify_token = request.query_params.get('hub.verify_token')
        mode = request.query_params.get('hub.mode')
        challenge = request.query_params.get('hub.challenge')

        if verify_token == "projectX" and mode == "subscribe" and challenge:
            return HttpResponse(challenge)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        data = request.data
        # logger.info(data)
        for event in data['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):  # print statements were failing to display it was in the error log
                    recipient_id = x['sender']['id']
                    if (recipient_id == partner.page_id):
                        next()
                    if x['message'].get('text'):
                        message = x['message']['text']
                        bot.send_text_message(recipient_id, message)
                        res = bot.send_text_message(recipient_id, message)
                        print(res)
                    if x['message'].get('attachment'):
                        bot.send_attachment_url(recipient_id, x['message']['attachment']['type'],
                                                x['message']['attachment']['payload']['url'])


class BotCreate(CreateView):
    template_name = "Partner_form.html"
    model = Partner

    fields = [
                'user',
                'name',
                'page_id',
                'app_id',
                'secret',
                'token'
    ]

    def get_success_url(self):
        return '/fb_messenger/bots/'


class BotListView(ListView):
    template_name = "partner_list.html"
    model = Partner

