# from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect

from baseApp.models import INCTicket, SRTicket, DeskSideEngr
from deskside.forms import deskINCEditForm, deskSREditForm


def desksideView(request):
    context = {}
    return render(request, 'desksideTemplate/index.html', context)


# This is for EditINC and SR
def deskINC(request, pk):
    inc = INCTicket.objects.get(ticket=pk)
    form = deskINCEditForm(instance=inc)
    if request.method == 'POST':
        form = deskINCEditForm(request.POST, instance=inc)
        if form.is_valid():
            form.save()
            # messages.success(request, "Successfully Updated.")
            return redirect('staff')
    context = {'form': form}
    return render(request, 'deskside/deskeditINC.html', context)


# This is for EditINC and SR
def deskSR(request, pk):
    inc = SRTicket.objects.get(tickets=pk)
    form = deskSREditForm(instance=inc)
    if request.method == 'POST':
        form = deskSREditForm(request.POST, instance=inc)
        if form.is_valid():
            form.save()
            # messages.success(request, "Successfully Updated.")
            return redirect('staff')

    deskside = DeskSideEngr.objects.filter(user__id=request.user.id)
    context = {'form': form, "deskside": deskside}
    return render(request, 'deskside/deskeditSR.html', context)



