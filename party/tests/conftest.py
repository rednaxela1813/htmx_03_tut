#party/test/conftest.py

import datetime
from operator import ge
import pytest
from django.test import Client
from party.models import Gift, Guest, Party

@pytest.fixture(scope='function')
def create_user(django_user_model):
    return django_user_model.objects.create_user(username="test-user", password="12345")


@pytest.fixture(scope='session')
def authenticated_client():
    def _authenticated_client(test_user):
        client = Client()
        client.force_login(test_user)

        return client
    return _authenticated_client

@pytest.fixture(scope='session')
def create_party():
    def _create_party(organizer,  **kwargs):
        return Party.objects.create(
            organizer=organizer,
            party_date=kwargs.get("party_date", datetime.date.today()),
            party_time=kwargs.get("party_time", datetime.datetime.now()),
            venue=kwargs.get("venue", "Amazing Castle"),
        )
    return _create_party

@pytest.fixture(scope='session')
def create_guest():
    def _create_guest(party, **kwargs):
        return Guest.objects.create(
            party=party,
            name=kwargs.get("name", "John Doe"),
            
            attending=kwargs.get("attending", True),
            
        )
    return _create_guest


@pytest.fixture(scope='session')
def create_gift():
    def _create_gift(party, **kwargs):
        return Gift.objects.create(
            party=party,
            gift=kwargs.get("test", "Gift"),
            price = kwargs.get("price", 100),
            link = kwargs.get("link", "https://www.amazon.com"),
            
        )
    return _create_gift
    

