from django.conf import settings
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from . models import HospitalRankingAlgorithm
import json


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
            'filters': {
                'location': str(location),
                'distanceInMiles': str(distance_in_miles),
                'pe1': str(pe_1),
                'pe2': str(pe_2),
                'pe3': str(pe_3),
                'pe4': str(pe_4),
            },
            'hospitals': []
        }

        # Create algorithm, run it, save it
        ranked_hospitals = HospitalRankingAlgorithm(context['filters']).rank_hospitals_by_filters()
        print(str(ranked_hospitals))
        context['hospitals'] = ranked_hospitals

        # Print context
        #print(str(json.dumps(context, indent=4, sort_keys=True)))

        return render(request, 'hospitalRanking/results.html', {'context': context})
    else:
        raise Http404("Invalid request")


def get_hospital(request, hospital_id):
    print("\tHospital ID = " + str(hospital_id))

    hospital_info = {
        'name': 'Duke Regional Hospital'
    }

    return render(request, 'hospitalRanking/hospital.html', hospital_info)
