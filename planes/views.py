from django.shortcuts import render
from planes.models import Curator, CustomUser, FinanceCosts, Quart, CuratorQuartCosts, Contract



def plane(request):
    finance_costs = FinanceCosts.objects.all()
    # finance_costs = FinanceCosts.objects.prefetch_related('quart').all()

    response = {}
    response['d'] = type(finance_costs)
    response['finance_costs'] = finance_costs

    return render(request, './planes/index.html', response)

# Create your views here.
