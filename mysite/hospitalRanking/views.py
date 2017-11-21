from django.conf import settings
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from . models import HospitalRankingAlgorithm, Hospital
from pprint import pprint
import json


# Create your views here.
def submit_ranking_form(request):
    if request.method == 'POST':

        # Example of how to get the form values
        location = request.POST['location']
        distance_in_miles = request.POST['distanceInMiles']
        cost_of_care = request.POST['CostOfCare']
        timely_effective_care = request.POST['TimelyEffectiveCare']
        complications_and_deaths = request.POST['ComplicationsAndDeaths']
        hospital_returns = request.POST['HospitalReturns']
        doctor_ranking = request.POST['DoctorRank']

        context = {
            'filters': {
                'Location': str(location),
                'Distance In Miles': str(distance_in_miles),
                'Cost of Care': str(cost_of_care),
                'Timely and Effective Care': str(timely_effective_care),
                'Complications and Death': str(complications_and_deaths),
                'Hospital Returns': str(hospital_returns),
                'Doctor Ranking': str(doctor_ranking)
            },
            'hospitals': []
        }

        # Create algorithm, run it, save it
        ranked_hospitals = HospitalRankingAlgorithm(context['filters']).rank_hospitals_by_filters()
        #pprint(ranked_hospitals)
        context['hospitals'] = ranked_hospitals

        # Print context
        #print(str(json.dumps(context, indent=4, sort_keys=True)))

        return render(request, 'hospitalRanking/results.html', {'context': context})
    else:
        raise Http404("Invalid request")


def get_hospital(request, hospital_id):
    hospitals = Hospital.objects.filter(provider_id=hospital_id)
    if hospitals.exists():
        context = {
            'hospital': hospitals[0]
        }
        return render(request, 'hospitalRanking/hospital.html', context)
    else:
        raise Http404("Invalid request")

