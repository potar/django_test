
import json
import datetime

from django.core.urlresolvers import reverse

from django.test import TestCase, Client
from django.utils.timezone import utc

from dynamic_models.models import dynamic_models


User = dynamic_models['users']
Room = dynamic_models['rooms']


class AJAXRequestTestMixin(object):
    def get(self, url, data={}):
        response = self.client.get(url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200, "Check AJAX request.")
        self.assertTrue(response.content, "Check response.")
        return True

    def post(self, url, data):
        response = self.client.post(url, json.dumps(data), "text/json", HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200, "Check AJAX request.")
        self.assertTrue(response.content, "Check response.")
        return True


class UsersTestCase(TestCase, AJAXRequestTestMixin):
    def setUp(self):
        User.objects.create(
            name="john",
            paycheck=1,
            date_joined=datetime.datetime.utcnow().replace(tzinfo=utc)
        )
        self.client = Client()

    def test_manager(self):
        user = User.objects.get(name="john")
        self.assertEqual(user.paycheck, 1, "Check user's attributes")

    def test_list_view(self):
        self.assertTrue(
            self.get(reverse("dynamic_models:list_users")),
            "Check the ajax view"
        )

    def test_update_view(self):
        user = User.objects.create(
            name="jane",
            paycheck=1,
            date_joined=datetime.datetime.utcnow().replace(tzinfo=utc)
        )
        user_id = user.id
        self.assertTrue(
            self.post(
                reverse("dynamic_models:update_user"),
                {
                    "id": user_id ,
                    "name": 'peter',
                    "paycheck": 100,
                }
            ),
            "Update the user."
        )
        user = User.objects.get(name="peter")
        self.assertEqual(user_id, user.id, "ID is still the same but the data is different.")


class RoomsTestCase(TestCase, AJAXRequestTestMixin):
    def setUp(self):
        Room.objects.create(
            department="one",
            spots=100,
        )
        self.client = Client()

    def test_manager(self):
        room = Room.objects.get(department="one")
        self.assertEqual(room.spots, 100, "Check room attributes")

    def test_list_view(self):
        self.assertTrue(
            self.get(reverse("dynamic_models:list_rooms")),
            "Check the ajax call"
        )

    def test_update_view(self):
        room = Room.objects.create(
            department="two",
            spots=100,
        )
        room_id = room.id
        self.assertTrue(
            self.post(
                reverse("dynamic_models:update_room"),
                {
                    "id": room_id ,
                    "department": 'test',
                }
            ),
            "Update the room."
        )
        room = Room.objects.get(department="test")
        self.assertEqual(room_id, room.id, "ID is still the same but data is different.")

# TODO: write more test cases. For example, write some for migrations. The idea might be taken here:
# http://micknelson.wordpress.com/2013/03/01/testing-django-migrations/
