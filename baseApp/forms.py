from django import forms
from django.contrib.auth.models import User

from baseApp.models import INCTicket, SRTicket


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class INCTicketForm(forms.ModelForm):
    class Meta:
        model = INCTicket
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(INCTicketForm, self).__init__(*args, **kwargs)
        if not user.is_staff:
            self.fields['member'].queryset = User.objects.filter(username=user.username)


class INCTicketEditForm(forms.ModelForm):
    class Meta:
        model = INCTicket
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(INCTicketEditForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = User.objects.filter(id=user.id)


class SRTicketForm(forms.ModelForm):
    class Meta:
        model = SRTicket
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(SRTicketForm, self).__init__(*args, **kwargs)
        if not user.is_staff:
            self.fields['member'].queryset = User.objects.filter(id=user.id)


class SRTicketEditForm(forms.ModelForm):
    class Meta:
        model = SRTicket
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(SRTicketEditForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = User.objects.filter(id=user.id)


