from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="Home"),
    path('private/', views.private,name="Private"),
    path('public/', views.public,name="Public"),
    path('engineering/', views.engineering,name="Engineering"),
    path('agricultural/', views.agricultural,name="Agricultural"),
    path('general/', views.general,name="General"),
    path('science&technology/', views.science,name="Science&Technology"),
    path('details/<str:nick>/',views.individual,name='Individual'),
    path('search/',views.search,name='Search'),
]