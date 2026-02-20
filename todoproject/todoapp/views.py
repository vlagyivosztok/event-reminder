from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Event, Person, MainCategory, SubCategory
from .forms import EventForm, PersonForm, MainCategoryForm, SubCategoryForm

class EventListView(ListView):
    model = Event
    template_name = 'todoapp/event_list.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'todoapp/event_form.html'
    success_url = reverse_lazy('event_list')

def ajax_create_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return JsonResponse({"id": person.id, "name": person.full_name}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

def ajax_create_main_category(request):
    if request.method == "POST":
        form = MainCategoryForm(request.POST)
        if form.is_valid():
            cat = form.save()
            return JsonResponse({"id": cat.id, "name": cat.name}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

def ajax_create_subcategory(request):
    if request.method == "POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            sub = form.save()
            return JsonResponse({"id": sub.id, "name": str(sub)}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
