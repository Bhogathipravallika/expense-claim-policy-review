from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_claim, name='create_claim'),
    path(
        'success/',
        views.claim_success,
        name='claim_success'
    ),
]