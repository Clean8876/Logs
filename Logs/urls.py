from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/topic', views.topic, name='topic'),
    path('/addtopic', views.addtopic, name='addtopic'),
    path('/addentry/<topic_id>', views.addentry, name='addentry'),
    path('/editentry/<entry_id>', views.editentry, name='editentry'),
    path('<topic_id>', views.entry, name='entry'),

]
