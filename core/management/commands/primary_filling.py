from django.core.management.base import BaseCommand
from core.models import Tab, Evaporator, Liquid, Producer, Person
from random import choice, randrange, randint
from decimal import Decimal


class Command(BaseCommand):
    help = 'Add persons, tastes, producers, tabs and evaporators to database'
    tastes = ['apple', 'mint', 'banana', 'strawberry', 'melon', 'watermelon', 'amol']
    first_names = ['Yarik', 'Igor', 'Tima', 'Zhenya']
    last_names = ['Yatsenko', 'Savenok', "Il'ich", 'Savich']
    producer_names = ['Envii', 'Aspire', 'Kits & Tanks', 'GeekVApe', 'HexOhm', 'Joyetech', 'KangerTech', 'Lost Vape',
                       'Suorin', 'UWELL', 'Vaporesso', 'Vision', 'VOOPOO', 'WISMEC']
    street_names = ['Midland Willows', 'St Annes Estate', 'Sea View Garden', 'West View Mill', 'Cornwall Barton',
                    'Grampian Mill', "St Martin's End", 'Cornwall Cedars', 'Parkstone Vale', 'Foxwood Lane',
                    'Sovereign View', 'Frithwood Crescent', 'Grace Dale', "St Paul's Wood", "Dean Meadow"]

    def handle(self, *args, **kwargs):
        for first_name in self.first_names:
            for last_name in self.last_names:
                person = Person(first_name=first_name, last_name=last_name)
                person.save()
        for producer_name in self.producer_names:
            prod = Producer(address=choice(self.street_names) + ' ' + str(randint(1, 200)) + '-' + str(randint(1, 500)), name=producer_name)
            prod.save()
        for taste in self.tastes:
            liquid = Liquid(producer=choice(Producer.objects.all()), price=Decimal(randrange(10, 100) / 10), taste=taste)
            liquid.save()
        for _ in range(100):
            tab = Tab(producer=choice(Producer.objects.all()), price=Decimal(randrange(20, 300) / 10), power=randint(50, 300))
            tab.save()
        for _ in range(70):
            evaporator = Evaporator(producer=choice(Producer.objects.all()), price=Decimal(randrange(50, 600) / 10))
            evaporator.save()
