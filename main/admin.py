from django.contrib import admin
from main.models import State, StateCapital, StateCities
# Register your models here.

class Stateadmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation')
	search_fields = ['name']
class StateCapitalAdmin(admin.ModelAdmin):
	list_display = ('name', 'population')
	search_fields = ['name',]
class StateCitiesAdmin(admin.ModelAdmin):
	list_display = ('city', 'zip_code')
	search_fields = ['city',]
admin.site.register(State, Stateadmin)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(StateCities, StateCitiesAdmin)