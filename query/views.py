from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.

def home(request):
	
	ID = request.GET.get('identity')
	data=[]
	for x in database.objects.all():
		temp = x.CAMPUS_ID[0:4]+x.CAMPUS_ID[8:]
		print(temp)
		if(ID!=None and (ID + "G"==temp or ID==x.CAMPUS_ID) and x.Course_ID!='0'):
			data.append(x)
	context={'datas': data, 'refdata': reference.objects.all()	}

	return render(request, 'query/home.html', context)

	
