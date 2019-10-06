from django.db import models


class Task(models.Model):
    name = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=False, max_length=500)
    rezult = models.CharField(blank=False, default="", max_length=300)
    status = models.BooleanField(blank=False, default=False)

    def make_done(self):
        self.status = True
        self.save()

    def __str__(self):
        return self.name if self.name else 'Tusk ' + str(self.id)


class Vape(models.Model):
    TYPE_CHOICES = [(1, 'Starter Kit'), (2, 'Kit'), (3, 'SKRR-S Tank'), (4, 'TC Box Mod'), (5, 'AIO Vape'), (6, 'Pod System')]
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=1)
    tab = models.ForeignKey('Tab', models.CASCADE, 'vapes')
    evaporator = models.ForeignKey('Evaporator', models.CASCADE, 'vapes')
    liquids = models.ManyToManyField('Liquid', 'vapes')
    owner = models.ForeignKey('Person', models.CASCADE, 'vapes')

    @property
    def name(self):
        return self.evaporator.name + ' ' + str(self.tab.power) + 'W | ' + self.type

    @property
    def price(self):
        return self.tab.price + self.evaporator.price + self.liquid.price

    @property
    def producers(self):
        return list(set([self.tab.producer.name, self.evaporator.producer.name] + self.liquids.all().value_list('producer')))

    def __str__(self):
        return self.name


class Tab(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    producer = models.ForeignKey('Producer', models.CASCADE, 'tabs')
    power = models.PositiveSmallIntegerField(blank=False, null=False)


class Evaporator(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    producer = models.ForeignKey('Producer', models.CASCADE, 'evaporators')


class Liquid(models.Model):
    taste = models.CharField(blank=False, max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    producer = models.ForeignKey('Producer', models.CASCADE, 'liquids')

    def __str__(self):
        return self.taste


class Producer(models.Model):
    name = models.CharField(blank=False, max_length=100)
    address = models.CharField(blank=False, max_length=150)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
