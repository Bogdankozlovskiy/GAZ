from django.shortcuts import render
from planes.models import Curator, CustomUser, FinanceCosts, Quart, CuratorQuartCosts, Contract



def plane(request):

    finance_costs = FinanceCosts.objects.all()
    
    for fin_cost in finance_costs:
        sum_all_quart = 0
        for quart in fin_cost.quart.all():
            sum_all_quart += quart.total
        fin_cost.total = sum_all_quart
        fin_cost.save()
    # finance_costs = FinanceCosts.objects.prefetch_related('quart').all()

    response = {}
    response['d'] = type(finance_costs)
    response['finance_costs'] = finance_costs

    return render(request, './planes/index.html', response)

# Create your views here.
