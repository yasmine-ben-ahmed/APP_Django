from .models import Post
from django.shortcuts import render

from .mqtt import start_mqtt_client
from django.http import JsonResponse
import pyowm




def start_mqtt(request):
    # Start the MQTT client / function created in mqtt.py
    start_mqtt_client()
    
    # Return a simple response to indicate that the client has started
    #return HttpResponse('MQTT client started successfully.')
    return render(request, 'dash/post_list.html', {})



def post_list(request):
    
    post = Post.objects.order_by('-id').first()
    post = Post.objects.all()

    for post_instance in post:
        print('_______',post_instance.temperature)

    # Render the template and pass the latest Post object as a context variable
    return render(request, 'dash/post_list.html', {'post': post,'post_instance':post_instance})


def getTemp(request):
    TEMP =Post.objects.all()
 
    return JsonResponse({"TEMP": list(TEMP.values())})



