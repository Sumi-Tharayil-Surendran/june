from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.core import serializers
from mainapp.models import Product
from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


def index(request):
    # bag_data= Bag.objects.all().count()
    context = {
        # 'bag_data': bag_data
    }

    return render(request, 'home.html', context)

@login_required
def reserve(request):
    # bag_data= Bag.objects.all().count()
    context = {
        # 'bag_data': bag_data
    }
    return render(request, 'reserve.html', context)


def login(request):
    # response=requests.get('').json()
    # area_data= Area.objects.all().count()
    # city_data = City.objects.all().count()
    # office_data = Office.objects.all().count()
    # route_data = Route.objects.all().count()
    # bag_data= Bag.objects.all().count()

    context = {
        # 'area_data':area_data,
        # 'city_data': city_data,
        # 'office_data':office_data,
        # 'route_data':route_data,
        # 'bag_data': bag_data
    }

    return render(request, 'login.html', context)


def getProducts(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            search_text = request.GET.get("search_text", None)
            if search_text == "":
                products = list(Product.objects.all().values())
            else:
                products = list(Product.objects.filter(
                    Title__icontains=search_text).values())
            return JsonResponse({'result': products})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')


def getProductDetail(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            productID = request.GET.get("productID", None)
            product = list(Product.objects.filter(ID=productID).values())
            return JsonResponse({'result': product})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

@login_required
def reserveProduct(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            productID = request.GET.get("productID", None)
            print(productID)
            product = Product.objects.filter(ID=productID)
            print(product)
            users = CustomUser.objects.filter(email=request.user.email)
            user = users[0]
            print(user)
            user.products.add(product[0])
            return JsonResponse({'result': 'success'})
        return JsonResponse({'result': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

@login_required
def reserveProductCount(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            users = CustomUser.objects.filter(email=request.user.email)
            user = users[0]
            productCount = user.products.count()
            return JsonResponse({'result': productCount})
        return JsonResponse({'result': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

@login_required
def reserveProductList(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            users = CustomUser.objects.filter(email=request.user.email)
            user = users[0]
            products = list(user.products.all().values())
            return JsonResponse({'result': products})
        return JsonResponse({'result': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

@login_required
def reserveProductRemove(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            productID = request.GET.get("productID", None)
            product = Product.objects.filter(ID=productID).first()
            user = CustomUser.objects.filter(email=request.user.email).first()
            user.products.remove(product)
            return JsonResponse({'result': 'success'})
        return JsonResponse({'result': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
