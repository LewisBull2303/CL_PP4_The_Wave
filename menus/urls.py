# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal:
from menus import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Urls for the food and drinks menu
urlpatterns = [
    path('food_menu', views.food_menu, name='food_menu'),
    path('drinks_menu', views.drink_menu, name='drink_menu'),
]