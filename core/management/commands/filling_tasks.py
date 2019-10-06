from django.core.management.base import BaseCommand
from core.models import Task


class Command(BaseCommand):
    help = 'Add tasks to database'

    def handle(self, *args, **kwargs):
        Task.objects.create(description="Select liquid tastes, that used in vapes with 'kit' type")
        Task.objects.create(description="Select producer addresses, that produce one detail type (only tabs, liquids or evaporators)")
        Task.objects.create(description="Select tab power from vapes, that used the chipest liquid (some if price the same)")
        Task.objects.create(description="Select vape names, that have tab power < 100 and less, that 3 liquids")
        Task.objects.create(description="Select addresses of producers of tab, evaporator and liquids if vape ouner name is Yarik or Igor")
