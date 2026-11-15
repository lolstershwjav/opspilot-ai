from dataclasses import dataclass
from collections import Counter

@dataclass
class Ticket:
    ticket_id: str
    description: str
    minutes_manual: int = 15

RULES = {
 'security': ('credential','breach','unauthorized','exposed','token'),
 'capacity': ('gpu','quota','capacity','out of memory'),
 'billing': ('invoice','billing','charge'),
 'deployment': ('deploy','container','build','release')
}

def triage(ticket: Ticket) -> dict:
    text=ticket.description.lower()
    scores={category:sum(word in text for word in words) for category,words in RULES.items()}
    category=max(scores,key=scores.get) if max(scores.values()) else 'general'
    urgent=category=='security' or 'outage' in text
    return {'id':ticket.ticket_id,'category':category,'priority':'P1' if urgent else 'P3',
            'recommendation': 'Escalate for human review; verify evidence before action' if urgent else 'Route to appropriate operations queue',
            'estimated_minutes_saved':max(0,ticket.minutes_manual-3)}

def summarize(results: list[dict]) -> dict:
    return {'tickets':len(results),'by_category':dict(Counter(x['category'] for x in results)),
            'estimated_minutes_saved':sum(x['estimated_minutes_saved'] for x in results)}
