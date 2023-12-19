from datetime import datetime
from baseApp.models import INCTicket, SRTicket


# Adding for open ticket. Location right upper(bottom)

def getINC():
    i = INCTicket.objects.all()
    return i


def getSR():
    s = SRTicket.objects.all()
    return s


# Getting all open ticket
def getAllOpenCount():
    i = getINC().filter(status="Open").count()
    s = getSR().filter(status="Open").count()
    return i + s


# Adding all closed ticket within the day.

def getCloseDayCount():
    i = getINC().filter(status="Closed").filter(updated=datetime.today()).count()
    sr = getSR().filter(status="Closed").filter(updated=datetime.today()).count()
    return i + sr

