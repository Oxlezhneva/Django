from django_filters import rest_framework as filters
from advertisements.models import Advertisement
from django_filters.rest_framework import DateFromToRangeFilter

class AdvertisementFilter(filters.FilterSet):    
    created_at = DateFromToRangeFilter()    

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at',]
