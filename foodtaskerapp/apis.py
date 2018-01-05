from django.http import JsonResponse

from foodtaskerapp.models import Restaurant
from foodtaskerapp.serializers import RestaurantSerializer

def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("-id"),
        many = True,
        context = {"request": request}
    ).data

    return JsonResponse({"restaurants": restaurants})

def customer_get_meals(request, restaurant_id):
    meals = MealSerializer(
        Meal.objects.filter(restaurant_id = restaurant_id).order_by("-id"),
        many = True,
        context = {"request": request}
    ).data
    return JsonResponse({"meals": meals})

def customer_add_order(request, restaurant_id):
    return JsonResponse({})

def customer_get_latest_order(request):
    return JsonResponse({})