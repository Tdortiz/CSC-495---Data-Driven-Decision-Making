from django.conf import settings
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from . models import HospitalRankingAlgorithm, Hospital, RankingForm
from pprint import pprint
import json


# Create your views here.
def submit_ranking_form(request):
    if request.method == 'POST':

        # Example of how to get the form values
        ranking_form = RankingForm()
        ranking_form.location = request.POST['location']
        ranking_form.cost_of_care = request.POST['CostOfCare']
        ranking_form.timely_effective_care = request.POST['TimelyEffectiveCare']
        ranking_form.complications_and_deaths = request.POST['ComplicationsAndDeaths']
        ranking_form.hospital_returns = request.POST['HospitalReturns']
        ranking_form.doctor_ranking = request.POST['DoctorRank']

        context = {
            'location_options': {
                'Location': str(ranking_form.location),
            },
            'priorities': {
                'Cost of Care': str(ranking_form.cost_of_care),
                'Timely and Effective Care': str(ranking_form.timely_effective_care),
                'Complications and Death': str(ranking_form.complications_and_deaths),
                'Hospital Returns': str(ranking_form.hospital_returns),
                'Doctor Ranking': str(ranking_form.doctor_ranking)
            },
            'hospitals': []
        }

        # Create algorithm, run it, save it
        ranked_hospitals = HospitalRankingAlgorithm(ranking_form).rank_hospitals_by_filters()
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

