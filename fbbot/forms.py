from django import forms
from .models import Partner


class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partner

        fields = [
            'name',
            'page_id',
            'app_id',
            'token'
         ]