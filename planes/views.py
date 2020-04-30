from django.shortcuts import render,redirect
from planes.models import Curator, CustomUser, FinanceCosts, Quart, CuratorQuartCosts, Contract
from planes.forms import CuratorForm
from django.http import HttpResponse, HttpResponseRedirect



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


def show_all_curator(request, finance_cost_id):
    curators = Curator.objects.filter(finance_cost=finance_cost_id)
    response = {"curators": curators, 'finance_cost_id': finance_cost_id}
    total_curat_for_all_quart = 0
    for curator in curators:
        total_curat_for_all_quart = 0
        for info in curator.curat.all():
            total_curat_for_all_quart += info.total
        curator.total_for_all_quart = total_curat_for_all_quart
    return render(request, './planes/curators.html', response)


def add_curator(request, finance_cost_id):
    title_fin_cost = FinanceCosts.objects.get(pk = finance_cost_id).title
    cf = CuratorForm()
    response = {'form': cf,
                'finance_cost_id': finance_cost_id,
                'title_fin_cost': title_fin_cost
    }
    return render(request, 'planes/create.html', response)



def save_curator(request, finance_cost_id):
    cf = CuratorForm(request.POST)
    if cf.is_valid():
        obj = cf.save(commit=False)
        obj.finance_cost = FinanceCosts.objects.get(pk = finance_cost_id)
        obj.save()
        return redirect("/plane/" + str(finance_cost_id))
    return HttpResponse('bad')



