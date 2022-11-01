from django.shortcuts import render

from .models import Brigada, City


def first_get(request):
    return {
        'cities': City.objects.all(),
        'brigadas': '',
        'object_list': '',
        'selected_city': '-- выберите город --',
        'selected_brigada': '',
        'selected_object': ''
    }


def city_chosen(request):
    selected_city = request.POST.get("city")
    city = City.objects.get(city_name=selected_city)
    return {
        'cities': City.objects.all(),
        'brigadas': city.brigadas.all().select_related('city'),
        'object_list': '',
        'selected_city': selected_city,
        'selected_brigada': '-- выберите бригаду --',
        'selected_object': ''
    }


def brigada_chosen(request):
    selected_brigada = request.POST.get("brigada")
    selected_city = request.POST.get("city")
    city = City.objects.get(city_name=selected_city)
    if city.brigadas.filter(brigada_name=selected_brigada).exists():
        brigada = Brigada.objects.get(brigada_name=selected_brigada)
        object_list = brigada.object_list.all().select_related('city',
                                                               'brigada')
        if len(object_list) > 0:
            selected_object = '-- выберите объект --'
        else:
            selected_object = '-- нет доступных объектов --'
    else:
        selected_brigada = '-- выберите бригаду --'
        object_list = ''
        selected_object = ''
    return {
        'cities': City.objects.all(),
        'brigadas': city.brigadas.all().select_related('city'),
        'object_list': object_list,
        'selected_city': selected_city,
        'selected_brigada': selected_brigada,
        'selected_object': selected_object
    }


def object_chosen(request):
    selected_brigada = request.POST.get("brigada")
    selected_city = request.POST.get("city")
    selected_object = request.POST.get("object")
    city = City.objects.get(city_name=selected_city)
    if city.brigadas.filter(brigada_name=selected_brigada).exists():
        brigada = Brigada.objects.get(brigada_name=selected_brigada)
        object_list = brigada.object_list.all().select_related('city',
                                                               'brigada')
        if not brigada.object_list.filter(object_name=selected_object
                                          ).exists():
            selected_object = '-- выберите объект --'
    else:
        selected_brigada = '-- выберите бригаду --'
        object_list = ''
        selected_object = ''
    return {
        'cities': City.objects.all(),
        'brigadas': city.brigadas.all().select_related('city'),
        'object_list': object_list,
        'selected_city': selected_city,
        'selected_brigada': selected_brigada,
        'selected_object': selected_object
    }


def index(request):

    if request.method == "GET":
        return render(request, 'objects/index.html', first_get(request))

    if (request.method == "POST"
       and request.POST.get("city") is not None
       and request.POST.get("brigada") is None
       and request.POST.get("object") is None):

        if request.POST.get("city") == '-- выберите город --':
            context = first_get(request)
        else:
            context = city_chosen(request)
        return render(request, 'objects/index.html', context)

    if (request.method == "POST"
       and request.POST.get("city") is not None
       and request.POST.get("brigada") is not None
       and request.POST.get("object") is None):

        if request.POST.get("brigada") == '-- выберите бригаду --':
            context = city_chosen(request)
        else:
            context = brigada_chosen(request)
        return render(request, 'objects/index.html', context)

    if (request.method == "POST"
       and request.POST.get("city") is not None
       and request.POST.get("brigada") is not None
       and request.POST.get("object") is not None):

        if request.POST.get("object") == '-- выберите объект --':
            context = brigada_chosen(request)
        else:
            context = object_chosen(request)
        return render(request, 'objects/index.html', context)
