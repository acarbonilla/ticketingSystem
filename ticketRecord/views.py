import datetime
from django.shortcuts import render, redirect
from baseApp.models import INCTicket, SRTicket
from django.db.models import Q

# importing Paginator for paging the template
from django.core.paginator import Paginator


# Year 2023
def recordINC(request):
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    if not sd:
        return redirect("authView")

    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    # Filter for closed Ticket
    year_2023 = INCTicket.objects.filter(created__range=(start_date, end_date), status='Closed')

    # This is for searching
    q = request.GET.get('y_2023') if request.GET.get('y_2023') is not None else ''
    closedQuery = INCTicket.objects.filter(
        Q(ticket__icontains=q) |
        Q(member__username__icontains=q),
        status="Closed", created__range=(start_date, end_date)
    ).order_by("-created")

    # Set up Pagination - It can be thank you. I put the Q in Paginator and it working fine
    p = Paginator(INCTicket.objects.filter(
        Q(ticket__icontains=q) |
        Q(member__username__icontains=q),
        status="Closed", created__range=(start_date, end_date)
    ).order_by("-created"), 1)

    page = request.GET.get('page')
    assign = p.get_page(page)

    # Setting loop for counter number in pagination
    nums = "a" * assign.paginator.num_pages

    # Setting counter on all entry
    # counter = INCTicket.objects.all().count()

    # counting close ticket
    inc_count = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()

    content = {'year_2023': year_2023, 'inc_count': inc_count, 'sd': sd, 'closedQuery': closedQuery, 'nums': nums,
               'assign': assign}

    return render(request, 'record/record_inc.html', content)


def recordSR(request):
    # Service Desk only
    sd = request.user.groups.filter(name="Service_Desk")
    if not sd:
        return redirect("authView")

    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    # Filter for closed Ticket
    year_2023 = SRTicket.objects.filter(created__range=(start_date, end_date), status='Closed')

    # This is for searching
    q = request.GET.get('y_2023') if request.GET.get('y_2023') is not None else ''
    closedQuery = SRTicket.objects.filter(
        Q(tickets__icontains=q) |
        Q(member__username__icontains=q),
        status="Closed", created__range=(start_date, end_date)
    ).order_by("-created")

    # counting close ticket
    sr_count = INCTicket.objects.filter(status="Closed", created__range=(start_date, end_date)).count()

    content = {'year_2023': year_2023, 'sr_count': sr_count, 'sd': sd, 'closedQuery': closedQuery}

    return render(request, 'record/record_sr.html', content)

# End of Year 2023

