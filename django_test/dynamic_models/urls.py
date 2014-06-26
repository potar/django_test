
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import (
    UsersListView, RoomsListView, CreateUsersView, CreateRoomsView,
    UpdateRoomsView, UpdateUsersView
)

urlpatterns = patterns('',
    url(
        r'^users$',
        CreateUsersView.as_view(),
        name="users_partial_view"),
    url(
        r'^rooms$',
        CreateRoomsView.as_view(),
        name="rooms_partial_view"),
    url(
        r'^list_users',
        UsersListView.as_view(),
        name="list_users"),
    url(
        r'^list_rooms',
        RoomsListView.as_view(),
        name="list_rooms"),
    url(
        r'^update_room',
        UpdateRoomsView.as_view(),
        name="update_room"),
    url(
        r'^update_user',
        UpdateUsersView.as_view(),
        name="update_user"),
)
