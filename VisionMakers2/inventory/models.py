from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Type(models.Model):

    vendor = models.CharField(max_length = 30)
    comments = models.CharField(max_length = 264, blank = True)
    STYLE_CHOICES = (
        ('M' , 'Men\'s'),
        ('W' , 'Women\'s')
    )
    style = models.CharField(choices = STYLE_CHOICES,
                             default = True, max_length = 5)
    desc = models.CharField(max_length = 30)
    sku = models.IntegerField(primary_key = True)
    color = models.CharField(max_length = 30, default = 'BLACK')

    '''price data'''
    VID = models.IntegerField(default= 1753674)
    HCFA = models.CharField(max_length = 30, default = 'V2020')
    wholesale = models.FloatField()
    retail = models.FloatField()
    cost = models.FloatField()
    taxable = models.BooleanField()

    '''stock data'''
    on_hand = models.IntegerField()
    on_order = models.IntegerField(default = 0)
    reorder_point = models.IntegerField()
    lead_time = models.IntegerField()

    '''measurements'''
    eye = models.IntegerField()
    bridge = models.IntegerField()
    temple = models.IntegerField()
    A = models.IntegerField()
    B = models.IntegerField()
    ED = models.IntegerField()
    DBL = models.IntegerField()


    '''statistics'''
    sold_this_week = models.IntegerField(default = 0)
    sold_this_month = models.IntegerField(default = 0)
    sold_this_year = models.IntegerField(default = 0)

    def size(self):
        return str(self.eye) + "/" + str(self.bridge)

    def __str__(self):
        return str(self.sku)

    def get_string(self):
        return str(self.vendor).capitalize() + ' ' + str(self.desc).capitalize()

    def update_on_hand(self):
        self.on_hand = self.pair_set.count()
        self.save()

    def get_absolute_url(self):
        return reverse('inventory:detail-type', kwargs = {'pk': self.pk})

    def get_stock_bv(self):
        return self.pair_set.filter(location = 'BV').count()

    def get_stock_wd(self):
        return self.pair_set.filter(location = 'WD').count()

    def get_stock_pa(self):
        return self.pair_set.filter(location = 'PA').count()

    def locations(self):
        locations = ''
        for pair in self.pair_set.all():
            if (pair.location == 'BV' and locations.find('BV') < 0):
                locations += 'BV '
            if (pair.location == 'WD' and locations.find('WD') < 0):
                locations += 'WD '
            if (pair.location == 'PA' and locations.find('PA') < 0):
                locations += 'PA '
        locations.strip()
        if locations == '':
            locations = 'None'
        return locations

class Pair(models.Model):
    type = models.ForeignKey(Type, on_delete = models.CASCADE)
    OFFICE_CHOICES = (
        ('BV' , 'BV'),
        ('WD' , 'WD'),
        ('PA' , 'PA')
        )
    location = models.CharField(max_length = 5, choices = OFFICE_CHOICES)
    comments = models.CharField(max_length = 264)
    date_added = models.DateField()


    def change_location(self, location):
        #changes the location of a pair of glasses
        self.location = location

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('inventory:index')
