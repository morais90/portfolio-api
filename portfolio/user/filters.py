# -*- coding: utf-8 -*-
from django.db.models import Q
from django_filters import rest_framework as filters

from .models import User, Group, Permission


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(method='filter_name')
    email = filters.CharFilter(name='email', lookup_expr='icontains')

    def filter_name(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value)
        )

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'is_active')


class GroupFilter(filters.FilterSet):
    name = filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Group
        fields = ('id', 'name')


class PermissionFilter(filters.FilterSet):
    name = filters.CharFilter(name='name', lookup_expr='icontains')
    codename = filters.CharFilter(name='codename', lookup_expr='icontains')

    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')
