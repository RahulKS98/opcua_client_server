from django.http import HttpResponse
from .opc_server import main as start_opcua_server
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
async def start_opcua(request):
    # Start the OPC UA server
    await start_opcua_server()
    return HttpResponse("OPC UA Server started successfully.")

@csrf_exempt
def register_users(request):
    if request.method == 'POST':
        data  = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')

        # Create a new user
        user = User.objects.create_user(username=username, password=password)

        if user is not None:
            return JsonResponse({'status': 'success', 'message': 'user created successfully'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'user creation failed'},status=422)
        
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data  = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')

        # Create a new user
        user = authenticate(username=username, password=password)

        if user is not None:
            return JsonResponse({'status': 'success', 'message': 'user logged in successfully'},status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'user login failed'}, status=422)

