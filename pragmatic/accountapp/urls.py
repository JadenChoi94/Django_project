from django.urls import path
from pragmatic.accountapp.views import hello_world

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]
