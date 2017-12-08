from subject.subject_ticket import SubjectTicket
from observers.observer_currentkpis import CurrentKPIsObserver
from observers.observer_forecastkpis import ForecastKPIsObserver

with SubjectTicket() as subject_ticket:
    with CurrentKPIsObserver(subject_ticket), ForecastKPIsObserver(subject_ticket):
        subject_ticket.set_tickets(25, 10, 5)
        subject_ticket.set_tickets(100, 50, 30)
        subject_ticket.set_tickets(50, 10, 20)
print('***All observers are detached. No more updates shall be notified to observers***')
subject_ticket.set_tickets(150, 110, 120)
