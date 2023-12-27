from baseApp.models import INCTicket, SRTicket


class Tickets:
    def __init__(self, inc, sr):
        self.inc = inc
        self.sr = sr

    def get_add(self):
        add = self.inc + self.sr
        return add


i = INCTicket.objects.all()
s = SRTicket.objects.all()


def getINC(self):
    self.inc = i
    return self.inc


def getSR(self):
    self.sr = s
    return self.sr
