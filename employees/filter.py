import django_filters
from .models import employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    id_min = django_filters.CharFilter(method='filter_by_id_range',label='FROM EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range',label='TO EMP ID')

    class Meta:
        model = employee
        fields = ['designation','name','id_min','id_max']

    def filter_by_id_range(self,queryset,name,value):
        if name == 'id_min':
            return queryset.filter(employee_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(employee_id__lte=value)
        return queryset