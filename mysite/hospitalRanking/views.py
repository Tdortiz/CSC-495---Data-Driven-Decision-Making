from django.conf import settings
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse


# Create your views here.
def submit_ranking_form(request):
    if request.method == 'POST':

        # Example of how to get the form values
        location = request.POST['location']
        distance_in_miles = request.POST['distanceInMiles']
        pe_1 = request.POST['priorityExample1']
        pe_2 = request.POST['priorityExample2']
        pe_3 = request.POST['priorityExample3']
        pe_4 = request.POST['priorityExample4']

        context = {
            'location': str(location),
            'distanceInMiles': str(distance_in_miles),
            'pe1': str(pe_1),
            'pe2': str(pe_2),
            'pe3': str(pe_3),
            'pe4': str(pe_4),
        }
        print(str(context))

        return render(request, 'hospitalRanking/results.html', {'context': context})
    else:
        raise Http404("Invalid request")

