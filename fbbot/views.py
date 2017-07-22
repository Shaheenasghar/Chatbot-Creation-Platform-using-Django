# FYPfinal/fbbot/views.py
import json, requests, random, re
from pprint import pprint
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


#  ------------------------ Fill this with your page access token! -------------------------------
PAGE_ACCESS_TOKEN = "EAAByGyMR704BABTAOe24sOZB7ZC9wOdKbjc62Y2M7LM87cULSL0v44ORpZAHWpKfPPBZABFZBayNGblHXd3Yu5nEYDzqxKOA1KWtE26dQnhVuGZBVWtJbZAhpoz3c9iAbJIywwBRgOZBYjoUv2aNnjY5JuCBx2fZCZBNV6KZATmgqXyjBu9O7JCMW3E"
VERIFY_TOKEN = "51219945121995"

jokes = {'ahtsham': ["""Ki aaaakhaaaan mein.......""",
                    """Hiii' Ahtsham sb!!! Punjab Police Zinda Baaad"""],
          'yousaf': ["""Hiiii' Yousaf mota""",
                    """ami g, munh thalle kro"""],
         'nasir': [
             """' Nasir is Paaathi""",
             """Nasir is bnda"""]}

# Helper function
def post_facebook_message(fbid, recevied_message):
    tokens = re.sub(r"[^a-zA-Z0-9\s]", ' ', recevied_message).lower().split()
    joke_text = ''
    for token in tokens:
        if token in jokes:
            joke_text = random.choice(jokes[token])
            break
    if not joke_text:
        joke_text = "I didn't understand! Send 'ahtsham', 'yousaf', 'nasir' for info.!"

    user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    user_details = requests.get(user_details_url, user_details_params).json()
    joke_text = 'Hii ' + user_details['first_name'] + '..! ' + joke_text

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": joke_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())


# View
class FbBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:

                if 'message' in message:
                    pprint(message)
                    post_facebook_message(message['sender']['id'], message['message']['text'])
        return HttpResponse()    