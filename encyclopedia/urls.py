from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:entry>', views.entry, name="entry"),
    path('results',views.results, name='results'),
    path('create', views.create, name='create'),
    path('edit/<str:page>', views.edit, name='edit'),
    path('random', views.random, name='random')
]
