from django.contrib import admin
from keckdatabase.models import Object, Observations, Measurements

class ObservationsInLine(admin.StackedInline):
    model = Observations
    fields = ['followup', 'candidates', 'reductionnotes', 'comment']

class MeasurementsInLine(admin.StackedInline):
    model = Measurements
    fields = ['mtype', 'distance', 'gaiadistance', 'sptype', 'propermotion', 'vmag', 'bminusv']

class ObjectAdmin(admin.ModelAdmin):
    list_filter = ['champion']
    list_per_page = 300
    ordering = ['obj_id']
    list_display = ['name', 'champion']
    fields = ['name', 'ra', 'dec', 'champion']
    inlines = [
        ObservationsInLine,
        MeasurementsInLine
    ]

admin.site.register(Object, ObjectAdmin)