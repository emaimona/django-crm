from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

from django.core.mail import send_mail



#from django.views import generics
#class testListView(generics.ListView):
 #   pass



# Create your views here.

class LandingPageView(TemplateView):
    template_name = 'landing.html'

def landing_page(request):
    return render(request, 'landing.html')


class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    
    def get_success_url(self):
        #return '/leads'
        return reverse('leads:lead-list')

    def form_valid(self, form):
        # Todo send Email
        send_mail(
            subject = 'A lead has been created!',
            message = 'Go to the site to see a new lead',
            from_email= 'test@test.com',
            recipient_list = ['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)


def lead_create(request):  # sourcery skip: instance-method-first-arg-name
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


class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse('leads:lead-list')


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')
   

class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})
    


class LeadListView(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    # Once we djanog the quer7set instead of lead it will be object_list
    # below is how to customize
    context_object_name = "leads"


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, "leads/lead_list.html", context={'lead': leads})

class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')

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