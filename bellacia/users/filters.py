# -*- coding: utf-8 -*-
import django_filters
from django.db.models import Q
from rest_framework.filters import FilterSet

from .models import User, Group, Permission


class UserFilter(FilterSet):
    name = django_filters.MethodFilter()
    email = django_filters.CharFilter(name='email', lookup_expr='icontains')

    def filter_name(self, queryset, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value)
        )

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'is_active')


class GroupFilter(FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Group
        fields = ('id', 'name')


class PermissionFilter(FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    codename = django_filters.CharFilter(name='codename', lookup_expr='icontains')

    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')
