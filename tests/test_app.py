from app import Ticket,triage,summarize

def test_security_priority():
    result=triage(Ticket('T1','Exposed API token in deployment logs'))
    assert result['priority']=='P1' and result['category']=='security'

def test_metrics():
    results=[triage(Ticket('T2','GPU quota request'))]
    assert summarize(results)['estimated_minutes_saved']==12
