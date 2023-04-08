from django.shortcuts import render, redirect
from django.contrib.gis.geos import Polygon

from .models import myProject
from django.contrib.gis.geos import GEOSGeometry

from django.http import JsonResponse
from django.contrib.gis.geos import Point
from .forms import *

def add_project(request):
    projects = myProject.objects.all()
    clients = client.objects.all()
    if request.method == 'POST':

        formulairep = Form_project(request.POST)
        # Get the other data from the form data
        nomp = request.POST.get('nomp')
        descp = request.POST.get('descp')
        debutp = request.POST.get('debutp')
        finp = request.POST.get('finp')
        cityp = request.POST.get('cityp')
        # clientp = request.POST.get('clientp')

        if formulairep.is_valid():
            # Get the selected client from the form
            selected_client_id = request.POST.get('clientp')

            # Get the client object based on the selected ID
            selected_client = client.objects.get(id=selected_client_id)
                 
            formulairep.enregistrerProj()
            polygonString = request.POST.get('points')
            print(polygonString)
            polygon = GEOSGeometry(polygonString, srid=4326)
            instance = myProject(nomp=nomp,descp=descp,debutp=debutp,finp=finp,cityp=cityp,geomp=polygon,clientp=selected_client)
            instance.save()
                    
            return redirect('add_client')
        return render(request, 'addproj.html', {'form': formulairep,'projects':projects})
    return render(request, 'addproj.html', {'form': Form_project(),'projects':projects})


def add_client(request):
        
        if request.method == 'POST':
            formulaire = Form_client(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'client'

                return redirect('display_polygone')
            return render(request, 'addclient.html', {'form': formulaire})
        return render(request, 'addclient.html', {'form': Form_client()})

        

def display_polygone(request):
    projects = myProject.objects.all()

    if request.method == 'POST':

       
        return redirect('home')
    return render(request, 'displaypoly.html', {'projects':projects})
