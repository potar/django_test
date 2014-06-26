
from django.views.generic import TemplateView, ListView, View, CreateView
from django.shortcuts import render

from braces import views

from .models import dynamic_models


# Create your views here.
class UsersListView(views.JsonRequestResponseMixin, views.AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        json_dict = (
            {
                'id': x.id,
                'name': x.name,
                'paycheck': x.paycheck,
                'date_joined': x.date_joined
            }
            for x in dynamic_models['users'].objects.all()
        )
        return self.render_json_response(list(json_dict))


class RoomsListView(views.JsonRequestResponseMixin, views.AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        json_dict = (
            {
                'id': x.id,
                'department': x.department,
                'spots': x.spots,
            }
            for x in dynamic_models['rooms'].objects.all()
        )
        return self.render_json_response(list(json_dict))


class CreateUsersView(CreateView):
    model = dynamic_models['users']
    template = "dynamic_models/users.html"
    template_name_suffix = ''


class CreateRoomsView(CreateView):
    model = dynamic_models['rooms']
    template = "dynamic_models/rooms.html"
    template_name_suffix = ''


class UpdateBaseView(views.CsrfExemptMixin, views.JsonRequestResponseMixin, View):
    require_json = True
    # Please set up a model before using this class.
    model = None

    def post(self, request, *args, **kwargs):
        try:
            pk = self.request_json["id"]
        except KeyError:
            error_dict = {u"message": u"Your data must include 'id'"}
            return self.render_bad_request_response(error_dict)

        self.model.objects.filter(id=pk).update(**self.request_json)
        return self.render_json_response(
            {u"message": u"Updating was successful"}
        )


class UpdateRoomsView(UpdateBaseView):
    model = dynamic_models["rooms"]

class UpdateUsersView(UpdateBaseView):
    model = dynamic_models["users"]
