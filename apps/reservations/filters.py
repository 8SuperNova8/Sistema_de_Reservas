import django_filters
from .models import Reservation

class ReservationFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    room_id = django_filters.NumberFilter(field_name='room_id')
    document = django_filters.CharFilter(field_name='guest_document', lookup_expr='exact')
    start_date = django_filters.DateFilter(method='filter_range', help_text="Formato: YYYY-MM-DD (ej: 2026-03-22)")
    end_date = django_filters.DateFilter(method='filter_range', help_text="Formato: YYYY-MM-DD (ej: 2026-03-25)")

    class Meta:
        model = Reservation
        fields = ['status', 'room_id', 'document', 'start_date', 'end_date']

    def filter_range(self, queryset, name, value):
        start = self.data.get('start_date')
        end = self.data.get('end_date')

        if start and end:
            return queryset.filter(
                check_in__lt = end,
                check_out__gt = start
            )
        return queryset