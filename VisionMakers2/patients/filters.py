from .models import Patient
import django_filters

class PatientFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='startswith')
    birthdate = django_filters.DateFilter(label='Date of Birth')
    first = django_filters.CharFilter(label = 'First Name', lookup_expr='startswith')
    last = django_filters.CharFilter(label = 'Last Name', lookup_expr='startswith')

    class Meta:
        model = Patient
        fields = []
