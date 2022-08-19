from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, "leads/lead_list.html", context={'lead': leads})

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})



def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid(): 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent
            )

            return redirect('/leads')

    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context=context)


'''
    def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid(): 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent
            )

            return redirect('/leads')

    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context=context)
'''