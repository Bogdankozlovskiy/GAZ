from django.shortcuts import render,redirect
from planes.models import Curator, CustomUser, FinanceCosts, Quart, CuratorQuartCosts, Contract
from planes.forms import CuratorForm, CuratorQuartCostsForm
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
    fin_cost_obj = FinanceCosts.objects.get(pk = finance_cost_id)
    quarts = Quart.objects.filter(finance_cost=fin_cost_obj)
    if cf.is_valid():
        obj = cf.save(commit=False)
        obj.finance_cost = fin_cost_obj
        obj.save()
        for i in range(4):
            curat_quart_cost = CuratorQuartCosts()
            curat_quart_cost.curator = obj
            curat_quart_cost.quart = quarts[i]
            curat_quart_cost.total = 0
            curat_quart_cost.save()
        return redirect("/plane/" + str(finance_cost_id))
    return HttpResponse('bad')


def edit_cqc(request, curator_id):
    quarts = CuratorQuartCosts.objects.filter(curator=curator_id)

    cqc_form = CuratorQuartCostsForm(initial={'curator':curator_id,
                                     'quart_0':quarts[0].total,
                                     'quart_1':quarts[1].total,
                                     'quart_2':quarts[2].total,
                                     'quart_3':quarts[3].total
                                     })
    response = {'cqc_form': cqc_form, 'curator_id':curator_id}
    return render(request, 'planes/edit_cqc.html', response)


def cqc_save(request, curator_id):
    cqc_form = CuratorQuartCostsForm(request.POST)
    print(request.POST)
    if cqc_form.is_valid():
        id_fin_cost = Curator.objects.get(pk=curator_id).finance_cost.id
        quarts = CuratorQuartCosts.objects.filter(curator=curator_id)
        if cqc_form.cleaned_data.get('delete'):
            for q in quarts:
                q.delete()
            curator = Curator.objects.get(pk=curator_id)
            curator.delete()
            return redirect('/plane/' + str(id_fin_cost))
        
        for q, q_in_form in zip(quarts, ['quart_0', 'quart_1', 'quart_2', 'quart_3']):
            q.total = cqc_form.cleaned_data[q_in_form]
            q.save()
        return redirect('/plane/' + str(id_fin_cost))
    return HttpResponse('bad')



