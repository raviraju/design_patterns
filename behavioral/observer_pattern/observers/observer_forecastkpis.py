from observers import AbstractObserver


class ForecastKPIsObserver(AbstractObserver):
    forecast_open_tickets = -1
    forecast_closed_tickets = -1
    forecast_new_tickets = -1

    def __init__(self, subject_ticket):
        self._subject_ticket = subject_ticket
        subject_ticket.attach(self)

    def update(self):        
        print('\tUpdating Tickets of ForecastKPIsObserver')
        self.forecast_open_tickets = self._subject_ticket.open_tickets
        self.forecast_closed_tickets = self._subject_ticket.closed_tickets
        self.forecast_new_tickets = self._subject_ticket.new_tickets
        self.display()

    def display(self):
        print('\tForecast open tickets: {}'.format(self.forecast_open_tickets))
        print('\tNew tickets expected in next hour: {}'.format(
            self.forecast_closed_tickets))
        print('\tTickets expected to be closed in next hour: {}'.format(
            self.forecast_new_tickets))
        print('\t*****')

    def __exit__(self, exc_type, exc_value, traceback):
        self._subject_ticket.detach(self)
