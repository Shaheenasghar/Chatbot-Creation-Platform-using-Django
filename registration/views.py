from django.views import generic
from fbbot.models import partner
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import UserForm
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        return partner.objects.all()


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/customers_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self,request):
       form = self.form_class(request.POST)

       if form.is_valid():
           user = form.save(commit=False)

           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()

           # return username if credentials are correct
           user = authenticate(username=username, password=password)

           if user is not None:

                if user.is_active:
                   login(request, user)
                   return redirect('registration:index')
       return render(request, self.template_name, {'form': form})
