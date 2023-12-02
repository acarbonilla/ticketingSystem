
from baseApp.models import INCTicket, SRTicket


def monthClosed():
    incClosed = INCTicket.objects.filter(status="Closed").count()
    srClosed = SRTicket.objects.filter(status="Closed").count()
    totalClosed = incClosed + srClosed
    return totalClosed


class Ticket:
    def __init__(self, inc, sr):
        self.inc = inc
        self.sr = sr

    def monthTicket(self):
        return self.inc + self.sr


i = INCTicket.objects.all()
s = SRTicket.objects.all()
incTicket = Ticket(i, s)


