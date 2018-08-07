from django import forms
from .models import Type


class ExportForm(forms.Form):
    OFFICE_CHOICES = (
        ('Beavercreek' , 'Beavercreek'),
        ('Woodman' , 'Woodman'),
        ('Pittsburgh' , 'Pittsburgh'),
        ('All Locations', 'All Locations')
        )
    location = forms.ChoiceField(choices = OFFICE_CHOICES)
    file_name = forms.CharField(max_length = 50)

    def clean_file_name(self):
        file_name = self.cleaned_data['file_name']
        if ' ' in file_name:
            raise forms.ValidationError('Do not include spaces in the file name')
        return file_name

class PairForm(forms.Form):
    type_list = Type.objects.all().order_by().values_list('sku')
    TYPE_CHOICES = ()
    for i in range(len(type_list)):
        #very obnoxious code that I can't figure out a way around
        TYPE_CHOICES = TYPE_CHOICES + ((type_list[i][0], type_list[i][0]),)
    type = forms.ChoiceField(choices = TYPE_CHOICES)

    OFFICE_CHOICES = (
        ('BV' , 'BV'),
        ('WD' , 'WD'),
        ('PA' , 'PA')
        )
    location = forms.ChoiceField(choices = OFFICE_CHOICES)
    comments = forms.CharField(required = False)
    date_added = forms.DateField()

# class TypeForm(forms.Form):
#     sku = forms.IntegerField()
#     vendor = forms.CharField(max_length = 30)
#     comments = forms.CharField(widget = forms.Textarea, required = False)
#     color = forms.CharField(max_length = 30)
#     STYLE_CHOICES = (
#         ('M' , 'Men\'s'),
#         ('W' , 'Women\'s')
#     )
#     style = forms.ChoiceField(choices = STYLE_CHOICES)
#     desc = forms.CharField(max_length = 30)
#     '''price data'''
#     VID = forms.IntegerField()
#     HCFA = forms.CharField(max_length = 30, initial = 'V2020')
#     wholesale = forms.FloatField()
#     retail = forms.FloatField()
#     cost = forms.FloatField()
#     taxable = forms.BooleanField(required = False)
#
#     '''stock data'''
#     on_hand = forms.IntegerField(initial = 0)
#     on_order = forms.IntegerField(initial = 0)
#     reorder_point = forms.IntegerField(initial = 0)
#     lead_time = forms.IntegerField(initial = 0)
#
#     '''measurements'''
#     eye = forms.IntegerField(initial = 15)
#     bridge = forms.IntegerField(initial = 15)
#     temple = forms.IntegerField(initial = 15)
#     A = forms.IntegerField(initial = 15)
#     B = forms.IntegerField(initial = 15)
#     ED = forms.IntegerField(initial = 15)
#     DBL = forms.IntegerField(initial = 15)
#     size = forms.CharField(max_length = 10)
#
#     '''statistics'''
#     sold_this_week = forms.IntegerField(initial = 0)
#     sold_this_month = forms.IntegerField(initial = 0)
#     sold_this_year = forms.IntegerField(initial = 0)

class MultiTypeForm(forms.Form):

    vendor = forms.CharField(max_length = 30, required = False)
    color = forms.CharField(max_length = 30, required = False)
    STYLE_CHOICES = (
        ('', '------'),
        ('M' , 'Men\'s'),
        ('W' , 'Women\'s')
    )
    style = forms.ChoiceField(choices = STYLE_CHOICES, required = False)
    desc = forms.CharField(max_length = 30, required = False)
    '''price data'''
    VID = forms.IntegerField(required = False)
    HCFA = forms.CharField(max_length = 30, required = False)
    wholesale = forms.FloatField(required = False)
    retail = forms.FloatField(required = False)
    cost = forms.FloatField(required = False)
    TAXABLE_CHOICES = (
        ('', '-------'),
        ('yes' , 'Yes'),
        ('no' , 'No')
    )
    taxable = forms.ChoiceField(choices = TAXABLE_CHOICES, required = False)

    '''stock data'''
    on_order = forms.IntegerField(required = False)
    reorder_point = forms.IntegerField(required = False)
    lead_time = forms.IntegerField(required = False)

    '''measurements'''
    eye = forms.IntegerField(required = False)
    bridge = forms.IntegerField(required = False)
    temple = forms.IntegerField(required = False)
    A = forms.IntegerField(required = False)
    B = forms.IntegerField(required = False)
    ED = forms.IntegerField(required = False)
    DBL = forms.IntegerField(required = False)

    comments = forms.CharField(required = False)
