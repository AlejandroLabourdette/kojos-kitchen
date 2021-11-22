import math
from enum import Enum
from random_variables import Ud


class Products(Enum):
    Sandwich = 1
    Sushi = 2


class Client:
    def __init__(self, arrive):
        self.arrive = arrive
        self.petition = self.generate_petition()
        self.petition_time = self.generate_petition_time()
        self.departure = 0

    @staticmethod
    def generate_petition():
        x = Ud(0, 1)
        if x == 0:
            return Products.Sushi
        return Products.Sandwich

    def generate_petition_time(self):
        if self.petition == Products.Sushi:
            x = Ud(5, 8)
            return x
        x = Ud(3, 5)
        return x

    def clone(self):
        copy = Client(self.arrive)
        copy.petition = self.petition
        copy.petition_time = self.petition_time
        copy.departure = self.departure
        return copy


class Kitchen:
    def __init__(self, with_3_cookers):
        self.is_case_2 = with_3_cookers
        self.clients_being_attended = []

    def can_attend_client(self, client, current_time):
        if self.is_case_2 and ((90 <= current_time <= 210) or (420 <= current_time <= 540)):
            chefs_amount = 3
        else:
            chefs_amount = 2

        if len(self.clients_being_attended) < chefs_amount:
            client.departure = current_time + client.petition_time
            self.clients_being_attended.append(client)
            return True, self.next_deliver_client()
        else:
            return False, self.next_deliver_client()

    def next_deliver_client(self):
        minimum = math.inf
        to_return = None
        for c in self.clients_being_attended:
            if c.departure < minimum:
                minimum = c.departure
                to_return = c
        return to_return

    def can_deliver_food(self):
        client = self.next_deliver_client()
        if len(self.clients_being_attended) > 0:
            self.clients_being_attended.remove(client)
            return True, client
        return False, client


class Restaurant:
    def __init__(self, with_3_cookers=False):
        self.kitchen = Kitchen(with_3_cookers)
        self.queue = []
        self.t = 0
        self.client_list = []

    def new_client_event(self, client: Client):
        """
        Add a new client to the restaurant queue
        :param client:
        Client to be added
        :return:
        Next food completion time
        """
        self.t = client.arrive
        self.queue.append(client)
        self.client_list.append(client)
        client = self.queue[0]
        any_new_petition, next_client = self.kitchen.can_attend_client(client, self.t)
        if any_new_petition:
            self.queue.pop(0)
        return next_client.departure

    def petition_completed_event(self):
        """
        Deliver a plate from the kitchen
        :return:
        Next food completion time
        """
        extraction, finished_client = self.kitchen.can_deliver_food()
        if not extraction:
            raise Exception('There was no client being attended in kitchen')
        self.t = finished_client.departure

        if len(self.queue) > 0:
            client = self.queue[0]
            any_new_petition, next_client = self.kitchen.can_attend_client(client, self.t)
            if any_new_petition:
                self.queue.pop(0)
            return next_client.departure
        if self.kitchen.next_deliver_client() is None:
            return math.inf
        return self.kitchen.next_deliver_client().departure
