
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
from django.shortcuts import render
import csv


def index(request):
    return redirect(reverse('bus_stations'))

with open(BUS_STATION_CSV, newline='', encoding = "UTF-8") as File:  
    reader = csv.reader(File)
    CONTENT = []
    for i in reader:
        if i[1] =='Name' or i[4] == 'Street' or i[6] == 'District':
            continue 
        else:
            my_dict = {'Name': i[1],'Street': i[4], 'District':i[6]}
            CONTENT.append(my_dict)
            

def bus_stations(request):

    paginator = Paginator(CONTENT, 5)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)






