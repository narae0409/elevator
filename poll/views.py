from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
from time import mktime, strptime
from .forms import *
from elevator_api.models import Elevator
import requests, json, math

class eAPIView(APIView):
	authentication_classes = []
	permission_classes = []
	
	def get(self, request):
		acceleration_list = []
		altitude_list = []
		date_list = []
		stocks = Elevator.objects.all().order_by('date')

		for stock in stocks:
			utc_now = mktime(strptime(str(stock.date), '%Y-%m-%d %H:%M:%S')) * 1000
			date_list.append(stock.date)
			acceleration_list.append([utc_now, stock.acceleration_z])
			altitude_list.append([utc_now, stock.current_altitude])
			
		data = {
			'acceleration': acceleration_list,
			'altitude': altitude_list,
			'date': date_list
		}
		
		return Response(data)

def chart(request):
	context = {}
	return render(request, 'poll/le.html', context)

class ElvtAPIVIEW_A(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request):
		date_list = []
		acceleration_list = []
		altitude_list = []

		url = "http://210.119.145.22/data/"
		d = {"number": number}
		res = requests.post(url, d)
		mybytes = res.text
		mybytes = json.loads(mybytes)

		for i in mybytes:
			utc_now = mktime(strptime(str(i['date']), '%Y-%m-%d %H:%M:%S')) * 1000
			date_list.append(i['date'])
			acceleration_list.append([utc_now, i['acceleration_z']])
			altitude_list.append([utc_now, i['current_altitude']])

		context = {
			'acceleration': acceleration_list,
			'altitude': altitude_list,
			'date': date_list
		}
		return Response(context)

class ElvtAPIVIEW_T(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request):
		date_list = []
		acceleration_list = []
		altitude_list = []

		url = "http://210.119.145.22/data/"
		d = {"number": number}
		res = requests.post(url, d)
		mybytes = res.text
		mybytes = json.loads(mybytes)

		for i in mybytes:	# 한시간
			date_now = datetime.now()
			date_now = (date_now - timedelta(hours=1))
			date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")
			date_now = datetime.strptime(date_now, "%Y-%m-%d %H:%M:%S").date()
			date_res = datetime.strptime(i['date'], "%Y-%m-%d %H:%M:%S").date()
			if date_res > date_now:
				utc_now = mktime(strptime(str(i['date']), '%Y-%m-%d %H:%M:%S')) * 1000
				date_list.append(i['date'])
				acceleration_list.append([utc_now, i['acceleration_z']])
				altitude_list.append([utc_now, i['current_altitude']])
			else :	# 한시간 이후(지난) 데이터
				pass

		context = {
			'acceleration': acceleration_list,
			'altitude': altitude_list,
			'date': date_list
		}
		return Response(context)

class ElvtAPIVIEW_D(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request):
		date_list = []
		acceleration_list = []
		altitude_list = []

		url = "http://210.119.145.22/data/"
		d = {"number": number}
		res = requests.post(url, d)
		mybytes = res.text
		mybytes = json.loads(mybytes)

		for i in mybytes:	# 하루
			date_now = datetime.now()
			date_now = (date_now - timedelta(days=1))
			date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")
			date_now = datetime.strptime(date_now, "%Y-%m-%d %H:%M:%S").date()
			date_res = datetime.strptime(i['date'], "%Y-%m-%d %H:%M:%S").date()
			if date_res > date_now:
				utc_now = mktime(strptime(str(i['date']), '%Y-%m-%d %H:%M:%S')) * 1000
				date_list.append(i['date'])
				acceleration_list.append([utc_now, i['acceleration_z']])
				altitude_list.append([utc_now, i['current_altitude']])
			else :	# 하루 이후(지난) 데이터
				pass
		context = {
			'acceleration': acceleration_list,
			'altitude': altitude_list,
			'date': date_list
		}
		return Response(context)

class ElvtAPIVIEW_W(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request):
		date_list = []
		acceleration_list = []
		altitude_list = []

		url = "http://210.119.145.22/data/"
		d = {"number": number}
		res = requests.post(url, d)
		mybytes = res.text
		mybytes = json.loads(mybytes)

		for i in mybytes:	# 일주일
			date_now = datetime.now()
			date_now = (date_now - timedelta(days=7))
			date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")
			date_now = datetime.strptime(date_now, "%Y-%m-%d %H:%M:%S").date()
			date_res = datetime.strptime(i['date'], "%Y-%m-%d %H:%M:%S").date()
			if date_res > date_now:
				utc_now = mktime(strptime(str(i['date']), '%Y-%m-%d %H:%M:%S')) * 1000
				date_list.append(i['date'])
				acceleration_list.append([utc_now, i['acceleration_z']])
				altitude_list.append([utc_now, i['current_altitude']])
			else:  # 일주일 이후(지난) 데이터
				pass
		context = {
			'acceleration': acceleration_list,
			'altitude': altitude_list,
			'date': date_list
		}
		return Response(context)

def index(request):
	url = "http://210.119.145.22/user/"
	if request.method == "POST":
		form = ElvtLogin(request.POST)
		if form.is_valid():
			my_id = form.cleaned_data['ID']
			password = form.cleaned_data['password']
			i = {
				'my_id': my_id,
				'password': password
			}
			res = requests.post(url, data=i)
			mybytes = res.text
			mybytes = json.loads(mybytes)

		if mybytes['msg'] == 'success':
			return HttpResponseRedirect('/poll/search/')
		else:
			return render(request, 'poll/index_Err.html')
	else:
		form = ElvtLogin()
	return render(request, 'poll/index_LG.html', {'form': form})

def index_GET(request):	# param_example : {"sensor":"test"}
	url = "http://210.119.145.22/data/"
	res = requests.get(url)
	mybytes = res.text
	context = {'mybytes': mybytes}
	return render(request, 'poll/index_GET.html', context)

def index_POST(request):
	global number
	global address
	if request.method == "POST":
		form0 = ElvtNumber(request.POST)
		form1 = ElvtAddress(request.POST)
		if form0.is_valid():
			number = form0.cleaned_data['elvtNumber']
			if number:
				return HttpResponseRedirect('/poll/main/number/')
		if form1.is_valid():
			address = form1.cleaned_data['elvtAddress']
			if address:
				return HttpResponseRedirect('/poll/address/')
	else:
		form0 = ElvtNumber()
		form1 = ElvtAddress()
	return render(request, 'poll/index_POST.html', {'form0': form0, 'form1': form1})
	url = "http://210.119.145.22/data/details/"
	'''d = { 'number' : '5057510'}
	res = requests.post(url, data=d)
	mybytes = res.text
	context = {'mybytes': mybytes }
	return render(request, 'poll/index_POST.html', context)'''

def index_Search(request):
	global number
	global address
	if request.method == "POST":
		form0 = ElvtNumber(request.POST)
		form1 = ElvtAddress(request.POST)
		if form0.is_valid():
			number = form0.cleaned_data['elvtNumber']
			if number:
				return HttpResponseRedirect('/poll/main/number/')
		if form1.is_valid():
			address = form1.cleaned_data['elvtAddress']
			if address:
				return HttpResponseRedirect('/poll/address/')
	else:
		form0 = ElvtNumber()
		form1 = ElvtAddress()
	return render(request, 'poll/index_SR.html', {'form0': form0, 'form1': form1})

def index_Tables(request):
	url = "http://210.119.145.22/data/details/"
	d = {'number': number}
	res = requests.post(url, data=d)
	mybytes = res.text
	mybytes = json.loads(mybytes)
	context = {'mybytes': mybytes}
	return render(request, 'poll/index_TB.html', context)

def index_Address(request):
	global number
	context = []

	url = "http://210.119.145.22/data/address/"
	d = {'address': address}
	res = requests.post(url, data=d)
	mybytes = res.text
	mybytes = json.loads(mybytes)

	for op in mybytes:
		context.append(op['address'])

	if request.method == "POST":
		result = request.POST.get('address', 'False')
		result = requests.post(url, {'address': result})
		result = result.text
		result = json.loads(result)

		for op in result:
			number = op['number']
		return HttpResponseRedirect('/poll/main/number/')

	# context = {'context': context}
	return render(request, 'poll/index_AR.html', {'context': context})

def index_GraphA(request):
	context = {}
	return render(request, 'poll/index_GPA.html', context)

def index_GraphT(request):
	context = {}
	return render(request, 'poll/index_GPT.html', context)

def index_GraphD(request):
	context = {}
	return render(request, 'poll/index_GPD.html', context)

def index_GraphW(request):
	context = {}
	return render(request, 'poll/index_GPW.html', context)

def index_Graphic(request):
	url = "http://210.119.145.22/data/"
	d = {"number": "5057510"}
	res = requests.post(url, d)
	mybytes = res.text
	mybytes = json.loads(mybytes)
	latest = mybytes[-1]
	late = mybytes[-2]

	layer = ((float)(latest['current_altitude']) - (float)(latest['base_altitude']))/(float)(latest['height'])
	acceleration = ((int)(latest['acceleration_z']) - (int)(late['acceleration_z']))/10

	context = {
		"layer": math.floor(layer),
		"acceleration": acceleration
	}

	if latest['ir'] == 1:
		return render(request, 'poll/index_GRPT.html', context)
	else :
		return render(request, 'poll/index_GRPF.html', context)

def index_NumberMain(request):	# 한시간
	url = "http://210.119.145.22/data/"
	d = {'number': number}
	res = requests.post(url, data=d)
	mybytes = res.text
	mybytes = json.loads(mybytes)

	latest = mybytes[-1]
	late = mybytes[-2]

	layer = ((float)(latest['current_altitude']) - (float)(latest['base_altitude']))/(float)(latest['height'])
	acceleration = ((int)(latest['acceleration_z']) - (int)(late['acceleration_z']))/10

	context = {
		"layer": math.floor(layer),
		"acceleration": acceleration
	}

	if latest['ir'] == 1:
		return render(request, 'poll/index_MNT.html', context)
	else :
		return render(request, 'poll/index_MNF.html', context)

def index_NumberMain_D(request):	# 하루
	url = "http://210.119.145.22/data/"
	d = {'number': number}
	res = requests.post(url, data=d)
	mybytes = res.text
	mybytes = json.loads(mybytes)

	latest = mybytes[-1]
	late = mybytes[-2]

	layer = ((float)(latest['current_altitude']) - (float)(latest['base_altitude']))/(float)(latest['height'])
	acceleration = ((int)(latest['acceleration_z']) - (int)(late['acceleration_z']))/10

	context = {
		"layer": math.floor(layer),
		"acceleration": acceleration
	}

	if latest['ir'] == 1:
		return render(request, 'poll/index_MNTD.html', context)
	else :
		return render(request, 'poll/index_MNFD.html', context)

def index_NumberMain_W(request):	# 일주일
	url = "http://210.119.145.22/data/"
	d = {'number': number}
	res = requests.post(url, data=d)
	mybytes = res.text
	mybytes = json.loads(mybytes)

	latest = mybytes[-1]
	late = mybytes[-2]

	layer = ((float)(latest['current_altitude']) - (float)(latest['base_altitude']))/(float)(latest['height'])
	acceleration = ((int)(latest['acceleration_z']) - (int)(late['acceleration_z']))/10

	context = {
		"layer": math.floor(layer),
		"acceleration": acceleration
	}

	if latest['ir'] == 1:
		return render(request, 'poll/index_MNTW.html', context)
	else :
		return render(request, 'poll/index_MNFW.html', context)

def index_NumberMain_A(request):	# 전부
	url = "http://210.119.145.22/data/"
	d = {'number': number}
	res = requests.post(url, data=d)
	mybytes = res.text
	mybytes = json.loads(mybytes)

	latest = mybytes[-1]
	late = mybytes[-2]

	layer = ((float)(latest['current_altitude']) - (float)(latest['base_altitude']))/(float)(latest['height'])
	acceleration = ((int)(latest['acceleration_z']) - (int)(late['acceleration_z']))/10

	context = {
		"layer": math.floor(layer),
		"acceleration": acceleration
	}

	if latest['ir'] == 1:
		return render(request, 'poll/index_MNTA.html', context)
	else :
		return render(request, 'poll/index_MNFA.html', context)