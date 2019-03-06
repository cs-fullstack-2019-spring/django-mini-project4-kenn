from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newCollector/', views.newCollector, name="newCollector"),
    path('addGame/', views.addGame, name="addGame"),
    path('gotGameInfo/', views.gotGameInfo, name="gotGameInfo"),
    # path('gotEditGameInfo/', views.gotEditGameInfo, name="gotEditGameInfo"),
    path('editGame/<int:gameID>/', views.editGame, name="editGame"),
    path('deleteGame/<int:gameID>/', views.deleteGame, name="deleteGame"),
]