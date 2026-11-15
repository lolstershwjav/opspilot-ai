from app import *
items=[triage(Ticket('T-100','Exposed token in container logs')),triage(Ticket('T-101','GPU quota request'))]
print(items)
print(summarize(items))
