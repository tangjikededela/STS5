import django_filters
from .models import *
from django_filters import CharFilter
from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr = 'icontains')

    class Meta:
        model = User
        fields = ('username',)

class EntryFilter(django_filters.FilterSet):
     locations = CharFilter(field_name='locations', lookup_expr = 'icontains')

     class Meta:
        model = Entry
        fields = ('locations',)
