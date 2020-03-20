from django.views import generic
from django.shortcuts import render
from keckdatabase.models import Object, Measurements, Observations

def index(request):
    num_objects = Object.objects.all().count()
    object_list = Object.objects.all()

    context = {
        'num_objects' : num_objects,
        "home_page" : "active"
    }

    return render(request, 'index.html', context=context)

class ObjectListView(generic.ListView):
    model = Object

    def get_context_data(self, **kwargs):
        context = super(ObjectListView, self).get_context_data(**kwargs)
        context['measurement'] = Measurements.objects.all()
        context['observation'] = Observations.objects.all()
        context["list_page"] = "active"

        return context

class ObjectDetailView(generic.DetailView):
    model = Object
    context_object_name = "object-detail"

    def get_context_data(self, **kwargs):
        context = super(ObjectDetailView, self).get_context_data(**kwargs)
        obj_id = self.kwargs['pk']
        context['measurement'] = Measurements.objects.get(obj=obj_id)
        context['observation'] = Observations.objects.get(obj=obj_id)
        context["list_page"] = "active"

        return context