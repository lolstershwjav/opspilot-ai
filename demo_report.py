import json
from app import *
rows = [triage(Ticket('T-100','Exposed token in container logs')),triage(Ticket('T-101','GPU quota request')),triage(Ticket('T-102','Billing invoice question'))]
print(json.dumps(rows))
