from django.contrib.auth.models import User
from django.db import models
import random


def incTicket():
    return str("INC") + str(random.randint(10000000000, 99999999999))


def srTicket():
    return str("SR") + str(random.randint(10000000000, 99999999999))


class DeskSideEngr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fName = models.CharField(max_length=50, verbose_name="First Name")
    lName = models.CharField(max_length=50)
    contact = models.IntegerField()

    def __str__(self):
        return f'{self.fName} {self.lName}'


class ServiceDesk(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    contact = models.IntegerField()

    def __str__(self):
        return f'{self.fName} {self.lName}'


class INCChoices(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class SRChoices(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class INCTicket(models.Model):
    ticket = models.CharField(max_length=14, default=incTicket, primary_key=True, editable=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(INCChoices, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[("Open", "Open"), ("Closed", "Closed")],
        default="Open"
    )
    assigned = models.ForeignKey(DeskSideEngr, on_delete=models.SET_NULL, null=True, blank=True)
    assignedBy = models.ForeignKey(ServiceDesk, on_delete=models.SET_NULL, null=True, blank=True)
    ticketUpdate = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.ticket}'


class SRTicket(models.Model):
    tickets = models.CharField(max_length=14, default=srTicket, primary_key=True, editable=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(SRChoices, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[("Open", "Open"), ("Closed", "Closed")],
        default="Open"
    )
    assigned = models.ForeignKey(DeskSideEngr, on_delete=models.SET_NULL, null=True, blank=True)
    assignedBy = models.ForeignKey(ServiceDesk, on_delete=models.SET_NULL, null=True, blank=True)
    ticketUpdate = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.tickets} - {self.created}'


# Advisory
class Advisory(models.Model):
    name = models.TextField()
    updated = models.DateField(auto_now=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.updated}'


# For chat inc
class Message(models.Model):
    inc = models.ForeignKey(INCTicket, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    chat = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.inc} - {self.user}'


# For chat sr
class SRMessage(models.Model):
    sr = models.ForeignKey(SRTicket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.sr} - {self.user}'



