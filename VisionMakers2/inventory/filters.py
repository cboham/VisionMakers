from .models import Type
import django_filters


class TypeFilter(django_filters.FilterSet):
    sku = django_filters.NumberFilter(lookup_expr = 'startswith')
    retail = django_filters.RangeFilter(field_name = 'retail')
    #returns a list of tuples
    vendor_list = Type.objects.order_by().values_list('vendor').distinct()
    #creates a tuple
    o = django_filters.OrderingFilter(
        fields = (
            ('retail', 'Retail'),
            ('cost', 'Cost'),
            ('on_hand', 'On hand')
        ),
        field_labels = {
            'retail': 'Retail',
            'cost':'Cost',
            'on_hand':'On Hand'
        }
    )
    VENDOR_CHOICES = ()
    for i in range(len(vendor_list)):
        #very obnoxious code that I can't figure out a way around
        VENDOR_CHOICES = VENDOR_CHOICES + ((vendor_list[i][0], vendor_list[i][0]),)
    vendor = django_filters.ChoiceFilter(field_name = 'vendor', choices = VENDOR_CHOICES)
    eye = django_filters.NumberFilter()

    color_list = Type.objects.order_by().values_list('color').distinct()
    COLOR_CHOICES = ()
    for i in range(len(color_list)):
        #very obnoxious code that I can't figure out a way around
        COLOR_CHOICES = COLOR_CHOICES + ((color_list[i][0], color_list[i][0]),)
    vendor = django_filters.ChoiceFilter(field_name = 'color', choices = COLOR_CHOICES)
    wholesale = django_filters.RangeFilter(field_name = 'retail')
    cost = django_filters.RangeFilter(field_name = 'cost', label = 'Cost')
    on_hand = django_filters.RangeFilter(field_name = 'on_hand', label = 'On Hand')

    desc_list = Type.objects.order_by().values_list('desc').distinct()
    # print(desc_list)
    DESC_CHOICES = ()
    for i in range(len(desc_list)):
        #very obnoxious code that I can't figure out a way around
        DESC_CHOICES = DESC_CHOICES + ((desc_list[i][0], desc_list[i][0]),)
    desc = django_filters.ChoiceFilter(field_name = 'desc', choices = DESC_CHOICES)


    class Meta:
        model = Type
        fields = []
