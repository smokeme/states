from django.shortcuts import render
from django.http import HttpResponse
from main.models import State, StateCapital, StateCities
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse 
from django.views.generic.list import ListView  
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
#forms
from main.forms import CitySearchForm, CreateCityForm, CityEditForm


# Create your views here.

@csrf_exempt
def get_search(request):

	get_var = request.GET.get('q', None)
	print request.GET
	print request.POST

	text_string = ''

	text_string += 'Search Term: %s <br>' % get_var

	text_string += """
	<form action="/get_search/" method="GET">

	Search Cities:
	<input type='text' name='q'>
	<br>

	<input type='submit' value="Submit">

	</form>

	""" 

	if get_var != None:
		cities =  StateCities.objects.filter(city__icontains=get_var)
		for city in cities:
			text_string += '%s <br>' % city.city

	return HttpResponse(text_string)

@csrf_exempt
def get_post(request):

	get_var = request.GET.get('q', None)

	post_var = request.POST.get('q', None)

	print request.GET
	print request.POST

	text_string = ''

	text_string += 'Get Var: %s <br>' % get_var
	text_string += 'Post Var: %s <br>' % post_var


	text_string += """
	<form action="/get_post/" method="POST">

	Enter Var:
	<input type='text' name='q'>
	<br>

	<input type='submit' value="Submit">

	</form>

	""" 

	return HttpResponse(text_string)

def state_view(request, name):
	state_list = []
	state = State.objects.get(name=name)
	state_list.append("name: %s </br>" % state.name)
	state_list.append("abbrev: %s</br>" % state.abbreviation)
	state_list.append("capital: %s</br>" % state.statecapital.name)
	state_list.append("latiude: %s</br>" % state.statecapital.latitude)
	state_list.append("longitude: %s</br>" % state.statecapital.longitude)
	state_list.append("capital population: %s</br>" % state.statecapital.population)
	state_list.append("<b>Cities:-</b></br></br>")
	cities = state.statecities_set.all()
	i = 0
	for x in cities:
		i += 1
		state_list.append("%d - <i>%s</i> </br>" % (i,x.city))

	return HttpResponse(state_list)

def state_list(request):
	state_list = []
	states = State.objects.all()
	for state in states:
		try:
			name = state.name
			capital = state.statecapital
			state_list.append("<a href='/state_view/%s'> %s -- %s</a> </br>" % (name,name,capital)) 
		except Exception, e:
			print e
	return HttpResponse(state_list)

def template_view(request):

	context = {}

	states = State.objects.all()

	context['states'] = states

	return render(request, 'state_list.html', context)

def details_view(request, name):
	context = {}
	state = State.objects.get(name=name)
	context['state'] = state
	return render(request, 'state_details.html', context)



class StateListView(ListView):
	model = State
	template_name = 'state_list.html'
	context_object_name = 'states'

class StateDetailView(DetailView):
	model = State
	template_name = 'state_details.html'
	context_object_name = 'state'

@login_required
def city_create(request):
	request_context = RequestContext(request)
	context = {}
	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form'] = form
		if form.is_valid():
			form.save()
			return render_to_response('city_create.html', context, context_instance=request_context)
		else:
			context['form'] = form
			return render_to_response('city_create.html', context, context_instance=request_context)
	else:
		form = CreateCityForm()
		context['form'] = form

		return render_to_response('city_create.html', context, context_instance=request_context)

@login_required
def city_search(request):
	request_context = RequestContext(request)
	context = {}
	if request.method == 'POST':
		form = CitySearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			city = '%s' % form.cleaned_data['city']
			state = form.cleaned_data['state']
			context['city_list'] = StateCities.objects.filter(city__startswith=city, state__name__startswith=state)

			return render_to_response('city_search.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors
			return render_to_response('city_search.html', context, context_instance=request_context)
	else:
		form = CitySearchForm()
		context['form'] = form

		return render_to_response('city_search.html', context, context_instance=request_context)

@login_required
def city_delete(request, pk):
	StateCities.objects.get(pk=pk).delete()

	return redirect('/city_search/')

@login_required
def city_edit(request, pk):
	print 'REQUEST TYPE -- %s' % request.method
	request_context = RequestContext(request)
	context = {}

	city = StateCities.objects.get(pk=pk)
	context['city'] = city
	form = CityEditForm(request.POST or None, instance=city)
	context['form'] = form
	if form.is_valid():
		form.save()
		return redirect('/city_search/')
	return render_to_response('city_edit.html', context, context_instance=request_context)





















