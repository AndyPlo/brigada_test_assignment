from django.shortcuts import render

from .models import Brigada, City


def index(request):
    cities = City.objects.all()
    print(
        request.POST.get("city"),
        request.POST.get("brigada"),
        request.POST.get("object")
    )

    if (
        request.method == "POST"
        and request.POST.get("city") is not None
        and request.POST.get("brigada") is None
        and request.POST.get("object") is None
    ):
        selected_city = request.POST.get("city")
        city = City.objects.get(city_name=selected_city)
        brigadas = city.brigadas.all()
        selected_brigada = '-- выберите бригаду --'
        object_list = ''
        selected_object = ''
        return render(
            request,
            'objects/index.html',
            {
                'cities': cities,
                'brigadas': brigadas,
                'object_list': object_list,
                'selected_city': selected_city,
                'selected_brigada': selected_brigada,
                'selected_object': selected_object
            }
        )

    if (
        request.method == "POST"
        and request.POST.get("city") is not None
        and request.POST.get("brigada") is not None
        and request.POST.get("object") is None
    ):
        selected_brigada = request.POST.get("brigada")
        selected_city = request.POST.get("city")
        city = City.objects.get(city_name=selected_city)
        brigadas = city.brigadas.all()
        brigada = Brigada.objects.get(brigada_name=selected_brigada)
        object_list = brigada.object_list.all()
        selected_object = '-- выберите объект --'
        return render(
            request,
            'objects/index.html',
            {
                'cities': cities,
                'brigadas': brigadas,
                'object_list': object_list,
                'selected_city': selected_city,
                'selected_brigada': selected_brigada,
                'selected_object': selected_object
            }
        )

    if (
        request.method == "POST"
        and request.POST.get("city") is not None
        and request.POST.get("brigada") is not None
        and request.POST.get("object") is not None
    ):
        selected_brigada = request.POST.get("brigada")
        selected_city = request.POST.get("city")
        selected_object = request.POST.get("object")
        city = City.objects.get(city_name=selected_city)
        brigadas = city.brigadas.all()
        brigada = Brigada.objects.get(brigada_name=selected_brigada)
        object_list = brigada.object_list.all()
        return render(
            request,
            'objects/index.html',
            {
                'cities': cities,
                'brigadas': brigadas,
                'object_list': object_list,
                'selected_city': selected_city,
                'selected_brigada': selected_brigada,
                'selected_object': selected_object
            }
        )

    selected_city = ''
    selected_brigada = ''
    selected_object = ''
    brigadas = ''
    object_list = ''
    return render(
        request,
        'objects/index.html',
        {
            'cities': cities,
            'brigadas': brigadas,
            'object_list': object_list,
            'selected_city': selected_city,
            'selected_brigada': selected_brigada,
            'selected_object': selected_object
        }
    )
