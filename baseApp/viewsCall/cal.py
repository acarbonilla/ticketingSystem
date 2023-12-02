# For experiment to show the total of each week of ticket created.
# Convert Month from name to number

from datetime import datetime, timedelta
# This import is for Calendar Section
import calendar

from django.utils.datetime_safe import strftime

from baseApp.models import INCTicket


# This is the skeleton function
def skeleton():
    month = datetime.now().strftime('%B')
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    return month_number


def weekSkeleton():
    one_week_ago = datetime.today() - timedelta(days=7)
    dated = INCTicket.objects.filter(created__gte=one_week_ago).count()
    return dated


def get_week_format():
    week = strftime(datetime.today(), '%W')
    weeks = int(week)
    return weeks


def get_month_format():
    month = datetime.now().strftime('%B')
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    inc = INCTicket.objects.filter(
        created__month=month_number,
    )
    return inc


# This is for 3 days deadline on each ticket

def deadline():
    three_days = datetime.today() + timedelta(days=3)
    dated = INCTicket.objects.filter(created__gte=three_days, status="Open")
    return dated

