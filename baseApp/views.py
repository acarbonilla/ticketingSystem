from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_protect

from baseApp.forms import INCTicketForm, SRTicketForm, INCTicketEditForm, SRTicketEditForm
from baseApp.models import INCTicket, SRTicket, Advisory, Message, SRMessage, INCChoices, SRChoices

# This is for calling from viewsCall folder
from baseApp.viewsCall.cal import skeleton, get_week_format, deadline
from baseApp.viewsCall.servicedesk import getAllOpenCount, getCloseDayCount


def homeView(request):
    content = {}
    return render(request, 'appTemplate/index.html', content)


# This is the page landing after the login. Done altering the main url's home page.

@login_required(login_url='account_login')
def authView(request):
    # Filtering group membership(static)
    sd = request.user.groups.filter(name="Service_Desk")
    ds = request.user.groups.filter(name="Deskside_Support")

    # Advisory
    advisory = Advisory.objects.all().order_by("-updated")

    # Adding for open ticket. Location right upper(button)
    openTicket = getAllOpenCount()
    # Close Ticket for today
    closedDayCount = getCloseDayCount()

    # This is for the Deskside Engr and their tickets
    # This For calculating the all ticket assigned to each user using INC and SR ticket.
    # Hoping weekly will work

    weekly = get_week_format()
    desksideINC = INCTicket.objects.values(
        'assigned__fName', 'assigned__lName'
    ).annotate(
        incCount=Count('ticket'),

    ).filter(status="Closed", created__week=weekly)

    desksideSR = SRTicket.objects.values(
        'assigned__fName', 'assigned__lName'
    ).annotate(
        srCounts=Count('tickets')
    ).filter(status="Closed", created__week=weekly)

    # Use for month ticket report
    skeletons = skeleton()

    # This is for month closed INC ticket
    monthINCclose = INCTicket.objects.filter(
        created__month=skeletons,
        status="Closed"
    ).count()

    # This is for month closed SR Ticket
    monthSRclose = SRTicket.objects.filter(
        created__month=skeletons,
        status="Closed"
    ).count()
    allClosedMonthTicket = monthINCclose + monthSRclose

    # This is for all ticket within the months
    incMonthticket = INCTicket.objects.filter(
        created__month=skeletons
    ).count()

    # This is for month closed SR Ticket
    srMonthticket = SRTicket.objects.filter(
        created__month=skeletons
    ).count()

    # This for adding all tickets in a month
    monthTicket = incMonthticket + srMonthticket

    # This is for resolution rate
    resoRate = round(float((allClosedMonthTicket / monthTicket) * 100))
    # End of Month report on the left side of page

    # This is for Deskside Report
    # Getting the all assigned ticket that has closed for this month(Week now)

    assignedINC = INCTicket.objects.filter(
        created__month=skeletons, assigned__user__id=request.user.id
    ).count()

    assignedSR = SRTicket.objects.filter(
        created__month=skeletons, assigned__user__id=request.user.id
    ).count()
    # Total Ticket assigned for this engr.
    monthDeskside = assignedINC + assignedSR

    dsINCClosed = INCTicket.objects.filter(
        created__month=skeletons,
        status="Closed", assigned__user__id=request.user.id
    ).count()

    dsSRClosed = SRTicket.objects.filter(
        created__month=skeletons,
        status="Closed", assigned__user__id=request.user.id
    ).count()
    # Calculating all closed ticket for this month
    totalMonth = dsINCClosed + dsSRClosed
    a = monthDeskside + 0.000001
    b = totalMonth + 0.000001
    c = round(float((b / a)) * 100)

    # Getting the Resolution Rate for Deskside Engr.
    desksideRate = c

    # This area is member non staff personnel. This is per month
    memberINC = INCTicket.objects.filter(
        created__month=skeletons, member__id=request.user.id, status="Open"
    ).count()

    memberSR = SRTicket.objects.filter(
        created__month=skeletons, member__id=request.user.id, status="Open"
    ).count()
    # Total Ticket created by user/member.
    memberMonthOpen = memberINC + memberSR

    # This is for close ticket count per month
    memberINCClosed = INCTicket.objects.filter(
        created__month=skeletons, member__id=request.user.id, status="Closed"
    ).count()

    memberSRClosed = SRTicket.objects.filter(
        created__month=skeletons, member__id=request.user.id, status="Closed"
    ).count()
    # Total Ticket created by user/member.
    memberMonthClosed = memberINCClosed + memberSRClosed

    # Showing the availability of deskside Engineer to support.
    memberOpenTicket = INCTicket.objects.filter(member__id=request.user.id, status="Open")
    memberOpenTicketSR = SRTicket.objects.filter(member__id=request.user.id, status="Open")

    # Showing the choices of ticket INC and SR
    iChoices = INCChoices.objects.all()
    srChoices = SRChoices.objects.all()

    # experimentation
    expireOn = timedelta(days=3)

    # this is for experimentation
    expired = deadline()
    event = ""

    content = {
        # This is for grouping and Advisory
        'sd': sd, 'ds': ds, 'advisory': advisory,

        # This is for assigned and closed ticket for each Deskside Engr.
        'desksideINC': desksideINC, 'desksideSR': desksideSR,

        # This is for right appear. It is a button showing open ticket and closed ticket for today.
        'openTicket': openTicket, 'closedDayCount': closedDayCount,

        'monthINCclose': monthINCclose, 'monthSRclose': monthSRclose,
        'allClosedMonthTicket': allClosedMonthTicket, 'resoRate': resoRate, 'monthTicket': monthTicket,

        # This is for individual report of each Deskside Support
        'dsINCClosed': dsINCClosed, 'dsSRClosed': dsSRClosed, 'monthDeskside': monthDeskside, 'totalMonth': totalMonth,
        'desksideRate': desksideRate, 'a': a, 'b': b,

        # Experiment(Used now at staff views/html)
        'expired': expired, 'memberOpenTicket': memberOpenTicket, 'event': event,

        # This is for member non-staff personnel
        'memberINC': memberINC, 'memberSR': memberSR,
        'memberMonthOpen': memberMonthOpen, 'memberMonthClosed': memberMonthClosed,
        'iChoices': iChoices, 'srChoices': srChoices, 'expireOn': expireOn, 'memberOpenTicketSR': memberOpenTicketSR

    }
    return render(request, 'appTemplate/authview.html', content)


@login_required(login_url='account_login')
def incForm(request):
    form = INCTicketForm(request.user, request.POST)

    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('authView')
    else:
        form = INCTicketForm(request.user)

    if request.user.groups.filter(id=3):
        return render(request, 'deskside/desksideError.html')

    context = {'form': form}
    return render(request, 'forms/incForm.html', context)


@login_required(login_url='account_login')
def srForm(request):
    form = SRTicketForm(request.user, request.POST)

    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('authView')
    else:
        form = SRTicketForm(request.user)

    if request.user.groups.filter(id=3):
        return render(request, 'deskside/desksideError.html')
    context = {'form': form}
    return render(request, 'forms/srForm.html', context)


# Edit or Update
@login_required(login_url='account_login')
def incEditForm(request, pk):
    inc = INCTicket.objects.get(ticket=pk)
    form = INCTicketEditForm(request.user, request.POST, instance=inc)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.user = request.user
        edit.save()
        return redirect('authView')
    else:
        form = INCTicketEditForm(request.user, instance=inc)

    context = {'form': form}
    return render(request, 'forms/incEdit.html', context)


@csrf_protect
@login_required(login_url='account_login')
def srEditForm(request, pk):
    inc = SRTicket.objects.get(tickets=pk)
    form = SRTicketEditForm(request.user, request.POST, instance=inc)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.user = request.user
        edit.save()
        return redirect('authView')
    else:
        form = SRTicketEditForm(request.user, instance=inc)

    context = {'form': form}
    return render(request, 'forms/srEdit.html', context)


@csrf_protect
@login_required(login_url='account_login')
def incDetails(request, pk):
    inc = INCTicket.objects.get(ticket=pk)
    message = Message.objects.filter(inc=inc)
    updated = Message.objects.order_by("-created")[0:1]
    context = {'inc': inc, 'message': message, 'updated': updated}
    return render(request, 'appTemplate/incDetails.html', context)


@csrf_protect
@login_required(login_url='account_login')
def srDetails(request, pk):
    sr = SRTicket.objects.get(tickets=pk)
    message = SRMessage.objects.filter(sr=sr)
    updated = SRMessage.objects.order_by("-created")[0:1]
    context = {'sr': sr, 'message': message, 'updated': updated}
    return render(request, 'appTemplate/srDetails.html', context)
