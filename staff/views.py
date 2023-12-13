from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.shortcuts import render, redirect

from baseApp.models import INCTicket, SRTicket, Advisory
from baseApp.viewsCall.cal import get_week_format
from staff.forms import SdINCEditForm, SdSREditForm
from datetime import datetime, timedelta
import datetime


# This is the dashboard for staff-Service Desk
@login_required(login_url='account_login')
def staff(request):
    sd = request.user.groups.filter(name="Service_Desk")
    ds = request.user.groups.filter(name="Deskside_Support")

    # Use for month ticket report
    weekly = get_week_format()

    # experimentation
    expireOn = timedelta(days=3)

    # Advisory
    advisory = Advisory.objects.all().order_by("-updated")

    # Table show the open Ticket - Service Desk
    incUserView = INCTicket.objects.filter(status="Open")
    srUserView = SRTicket.objects.filter(status="Open")
    # Counting open ticket - Service Desk
    incUserViewCount = INCTicket.objects.filter(status="Open").count()
    srUserViewCount = SRTicket.objects.filter(status="Open").count()
    countOpen = incUserViewCount + srUserViewCount

    # For Deskside Support
    desksideINCView = INCTicket.objects.all()
    desksideSRView = SRTicket.objects.all()

    # Total count of open ticket
    desksideINCCountOpen = INCTicket.objects.filter(assigned__user__id=request.user.id).filter(status="Open").count()
    desksideSRVCountOpen = SRTicket.objects.filter(assigned__user__id=request.user.id).filter(status="Open").count()
    # Calculating
    dsTicketOpen = desksideINCCountOpen + desksideSRVCountOpen

    # Total count of tickets assigned
    desksideINCCount = INCTicket.objects.filter(assigned__user__id=request.user.id, created__week=weekly)\
        .filter(status="Closed").count()
    desksideSRVCount = SRTicket.objects.filter(assigned__user__id=request.user.id, created__week=weekly)\
        .filter(status="Closed").count()
    dsTicketClosed = desksideSRVCount + desksideINCCount

    # This is for experimental query
    start_date = datetime.date(2023, 7, 1)
    end_date = datetime.date(2023, 7, 30)
    june = INCTicket.objects.filter(created__range=(start_date, end_date))

    # Prohibiting non staff user
    if not request.user.is_staff:
        return redirect("authView")
    # return render(request, 'location of template') it will show a template message that you are not allowed.

    context = {'sd': sd, 'ds': ds, 'advisory': advisory, 'incUserView': incUserView, 'srUserView': srUserView,
               'countOpen': countOpen,
               # This is for Deskside View
               'desksideINCView': desksideINCView, 'desksideSRView': desksideSRView, 'dsTicketOpen': dsTicketOpen,
               'dsTicketClosed': dsTicketClosed, 'expireOn': expireOn, 'june': june}
    return render(request, 'staff/staff.html', context)


@login_required(login_url='account_login')
def openTicket(request):
    incUserView = INCTicket.objects.filter(status="Open")
    srUserView = SRTicket.objects.filter(status="Open")

    # Counting All Tickets
    # Open Ticket
    inc = INCTicket.objects.filter(status="Open").count()
    sr = SRTicket.objects.filter(status="Open").count()
    addTicket = inc + sr

    context = {'incUserView': incUserView, 'srUserView': srUserView, 'addTicket': addTicket}
    return render(request, 'staff/openTicket.html', context)


# This is for All closed ticket,means all no filter on what month. Paginator on this way.
@login_required(login_url='account_login')
def closedTicket(request):
    """
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    ds = request.user.groups.filter(name="Deskside_Support")
    if not sd and ds:
        return redirect("authView")

    """

    # This is for experimental query
    start_date = datetime.date(2023, 6, 1)
    end_date = datetime.date(2023, 6, 30)
    june = INCTicket.objects.filter(created__range=(start_date, end_date))

    # This is for searching
    q = request.GET.get('g') if request.GET.get('g') is not None else ''
    closedQuery = INCTicket.objects.filter(
        Q(ticket__icontains=q) |
        Q(member__username__icontains=q) |
        Q(assigned__fName__icontains=q),
        status="Closed", created__range=(start_date, end_date)
    ).order_by("-created")

    SRClosedQuery = SRTicket.objects.filter(
        Q(tickets__icontains=q) |
        Q(member__username__icontains=q),
        created__range=(start_date, end_date),
        status="Closed").order_by("-created")

    # Closed Ticket
    inc = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    sr = SRTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    addTicket = inc + sr

    context = {'addTicket': addTicket, 'closedQuery': closedQuery,
               'SRClosedQuery': SRClosedQuery, 'june': june}
    return render(request, 'staff/closedTicket.html', context)



# This is for EditINC and SR
@login_required(login_url='account_login')
def sdINC(request, pk):
    inc = INCTicket.objects.get(ticket=pk)
    form = SdINCEditForm(instance=inc)
    if request.method == 'POST':
        form = SdINCEditForm(request.POST, instance=inc)
        if form.is_valid():
            form.save()
            # messages.success(request, "Successfully Updated.")
            return redirect('staff')
    context = {'form': form}
    return render(request, 'staff/editINC.html', context)


# This is for EditINC and SR
@login_required(login_url='account_login')
def sdSR(request, pk):
    inc = SRTicket.objects.get(tickets=pk)
    form = SdSREditForm(instance=inc)
    if request.method == 'POST':
        form = SdSREditForm(request.POST, instance=inc)
        if form.is_valid():
            form.save()
            # messages.success(request, "Successfully Updated.")
            return redirect('staff')
    context = {'form': form}
    return render(request, 'staff/editSR.html', context)


# This is for  monthly report SR and INC.(hold 6/28/2023)
def monthlyFront(request):
    context = {}
    return render(request, 'staff/monthfront.html', context)
