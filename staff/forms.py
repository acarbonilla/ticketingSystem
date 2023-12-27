from django import forms


from baseApp.models import INCTicket, SRTicket


class SdINCEditForm(forms.ModelForm):
    class Meta:
        model = INCTicket
        fields = '__all__'


class SdSREditForm(forms.ModelForm):
    class Meta:
        model = SRTicket
        fields = '__all__'
