from django.urls import path
from .views import PartyListPage


list_parties_urlpatterns = [
    path("", PartyListPage.as_view(), name="page_party_list"),
]


urlpatterns = list_parties_urlpatterns
    
    

