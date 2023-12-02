from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
import datetime
from baseApp.models import INCTicket, SRTicket


@login_required(login_url='account_login')
def july(request):
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    if not sd:
        return redirect("authView")

    # This is for experimental query
    start_date = datetime.date(2023, 7, 1)
    end_date = datetime.date(2023, 7, 31)

    # This is for searching
    q = request.GET.get('jul') if request.GET.get('jul') is not None else ''
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

    # Counting All Tickets
    # Closed Ticket
    inc = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    sr = SRTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    addTicket = inc + sr

    context = {'addTicket': addTicket, 'closedQuery': closedQuery,
               'SRClosedQuery': SRClosedQuery}
    return render(request, 'staff/month/july.html', context)


@login_required(login_url='account_login')
def august(request):
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    if not sd:
        return redirect("authView")

    # This is for experimental query
    start_date = datetime.date(2023, 8, 1)
    end_date = datetime.date(2023, 8, 31)

    # This is for searching
    q = request.GET.get('aug') if request.GET.get('aug') is not None else ''
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

    # Counting All Tickets
    # Closed Ticket
    inc = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    sr = SRTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    addTicket = inc + sr

    context = {'addTicket': addTicket, 'closedQuery': closedQuery,
               'SRClosedQuery': SRClosedQuery}
    return render(request, 'staff/month/august.html', context)



@login_required(login_url='account_login')
def september(request):
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    if not sd:
        return redirect("authView")

    # This is for experimental query
    start_date = datetime.date(2023, 9, 1)
    end_date = datetime.date(2023, 9, 30)

    # This is for searching
    q = request.GET.get('sep') if request.GET.get('aug') is not None else ''
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

    # Counting All Tickets
    # Closed Ticket
    inc = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    sr = SRTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    addTicket = inc + sr

    context = {'addTicket': addTicket, 'closedQuery': closedQuery,
               'SRClosedQuery': SRClosedQuery}
    return render(request, 'staff/month/september.html', context)


@login_required(login_url='account_login')
def october(request):
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    if not sd:
        return redirect("authView")

    # This is for experimental query
    start_date = datetime.date(2023, 10, 1)
    end_date = datetime.date(2023, 10, 30)

    # This is for searching
    q = request.GET.get('oct') if request.GET.get('oct') is not None else ''
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

    # Counting All Tickets
    # Closed Ticket
    inc = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    sr = SRTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    addTicket = inc + sr

    context = {'addTicket': addTicket, 'closedQuery': closedQuery,
               'SRClosedQuery': SRClosedQuery}
    return render(request, 'staff/month/october.html', context)


@login_required(login_url='account_login')
def november(request):
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    if not sd:
        return redirect("authView")

    # This is for experimental query
    start_date = datetime.date(2023, 11, 1)
    end_date = datetime.date(2023, 11, 30)

    # This is for searching
    q = request.GET.get('nov') if request.GET.get('nov') is not None else ''
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

    # Counting All Tickets
    # Closed Ticket
    inc = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    sr = SRTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    addTicket = inc + sr

    context = {'addTicket': addTicket, 'closedQuery': closedQuery,
               'SRClosedQuery': SRClosedQuery}
    return render(request, 'staff/month/november.html', context)


@login_required(login_url='account_login')
def december(request):
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    if not sd:
        return redirect("authView")

    # This is for experimental query
    start_date = datetime.date(2023, 12, 1)
    end_date = datetime.date(2023, 12, 31)

    # This is for searching
    q = request.GET.get('dec') if request.GET.get('dec') is not None else ''
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

    # Counting All Tickets
    # Closed Ticket
    inc = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    sr = SRTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()
    addTicket = inc + sr

    context = {'addTicket': addTicket, 'closedQuery': closedQuery,
               'SRClosedQuery': SRClosedQuery}
    return render(request, 'staff/month/december.html', context)