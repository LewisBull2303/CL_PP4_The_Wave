# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodItem, DrinkItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def food_menu(request):
    """
    a view to display the food menu
    """
    food_list = FoodItem.objects.all()
    return render(
        request, 'menus/food_menu.html', {'food_list': food_list})


def drink_menu(request):
    """
    a view to display the drinks menu
    """
    drink_list = DrinkItem.objects.all()
    return render(
        request, 'menus/drinks_menu.html', {'drink_list': drink_list})