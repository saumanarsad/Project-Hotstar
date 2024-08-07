from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page")
    friends = [
        'sauman',
        'izza',
        'mohid'
    ]
    return JsonResponse(friends,safe=False)