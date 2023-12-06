from django import forms


from baseApp.models import INCTicket, SRTicket


class deskINCEditForm(forms.ModelForm):
    class Meta:
        model = INCTicket
        fields = '__all__'


class deskSREditForm(forms.ModelForm):
    class Meta:
        model = SRTicket
        fields = '__all__'

