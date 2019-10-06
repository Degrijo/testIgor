from django.core.management.base import BaseCommand
from core.models import Vape, Tab, Evaporator, Liquid, Person
from random import choice, randint
from django.db.models import QuerySet


class Command(BaseCommand):
    help = 'Add 10 vapes to database'

    def handle(self, *args, **kwargs):
        type(Vape)
        for _ in range(10):
            vape = Vape.objects.create(type=choice(Vape.TYPE_CHOICES)[0],
                                tab=choice(Tab.objects.all()),
                                evaporator=choice(Evaporator.objects.all()),
                                owner=choice(Person.objects.all()))
            vape.liquids.set([choice(Liquid.objects.all()) for _ in range(randint(1, 3))])
