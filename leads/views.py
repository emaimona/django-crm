from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.
    

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid(): 
            form.save()

            return redirect('/leads')

    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context=context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')
   

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})
    
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, "leads/lead_list.html", context={'lead': leads})


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    ''' When updating we need to pass the instance of the obj in case'''
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')


    return render(request, 'leads/lead_update.html', {'form':form, 'lead':lead})

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect('/leads')

#     return render(request, 'leads/lead_update.html', {'lead': lead, 'form':form})

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