from observers import AbstractObserver


class CurrentKPIsObserver(AbstractObserver):
    cur_open_tickets = -1
    cur_closed_tickets = -1
    cur_new_tickets = -1

    def __init__(self, subject_ticket):
        self._subject_ticket = subject_ticket
        subject_ticket.attach(self)

    def update(self):
        print('\tUpdating Tickets of CurrentKPIsObserver')
        self.cur_open_tickets = self._subject_ticket.open_tickets
        self.cur_closed_tickets = self._subject_ticket.closed_tickets
        self.cur_new_tickets = self._subject_ticket.new_tickets
        self.display()

    def display(self):
        print('\tCurrent open tickets: {}'.format(self.cur_open_tickets))
        print('\tNew tickets in last hour: {}'.format(self.cur_closed_tickets))
        print('\tTickets closed in last hour: {}'.format(self.cur_new_tickets))
        print('\t*****')

    def __exit__(self, exc_type, exc_value, traceback):
        self._subject_ticket.detach(self)
