from django.conf import settings
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse


# Create your views here.
def submit_ranking_form(request):
    if request.method == 'POST':
        # Example of how to get the form values
        pe_1 = request.POST.getlist('priorityExample1')[0]
        pe_2 = request.POST.getlist('priorityExample2')[0]
        pe_3 = request.POST.getlist('priorityExample3')[0]

        context = {
            'pe1': str(pe_1),
            'pe2': str(pe_2),
            'pe3': str(pe_3),
        }

        print(str(context))
        return render(request, 'hospitalRanking/results.html', context)
    else:
        raise Http404("Invalid request")

