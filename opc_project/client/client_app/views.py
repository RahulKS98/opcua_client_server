from django.shortcuts import render, redirect
from .forms import LoginForm, registerForm, nodeForm
from asyncua import Client
import asyncio
import requests
import tkinter as tk
from tkinter import messagebox
from django.http import HttpResponse, JsonResponse 
import socket
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import json
import plotly.express as px
import plotly

# Create your views here.
target_url = 'http://192.168.29.84:8000'
header = {"Content-type":"application/json"}
opc_url = "opc.tcp://192.168.29.84:5001"

# login user
async def home(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = {'username': form.cleaned_data['username'], 'password': form.cleaned_data['password']}
            response  = requests.post(target_url+"/login-user", json=data, headers=header)
            if response.status_code == 200:
                return redirect('/node/')
            else:   
                return HttpResponse("Login failed")
    else:
        form = LoginForm()   
    return render(request, 'login.html', {'form': form})

# register user
def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            data = {'username': form.cleaned_data['username'], 'password': form.cleaned_data['password']}
            response  = requests.post(target_url+"/register-users", json=data, headers=header)
            if response.status_code == 200:
                return redirect('/login/')
            else:   
                return HttpResponse("Registration failed")
    else:
        form = registerForm()   

    return render(request, 'register.html', {'form': form})

# Node selection logic
async def select_node(request):
    if request.method == 'POST':
        data = await connect_client()
        form = nodeForm(request.POST)
        if form.is_valid():
            # Show data in graphical format
            graph_value =  load_graph(data[form.cleaned_data['dropdown']])
            return render(request, 'graph.html', {'data': graph_value})
    else:
        form = nodeForm()
        return render(request, 'node.html', {'form': form})

def load_graph(graph_data):
    return json.dumps(graph_data)

# connect opc ua client to server
async def connect_client(url=opc_url):

    async with Client(url=url) as client:
        try:
            nsidx = await client.get_namespace_index("OPC UA SIMULATION SERVER")

            available_sensors = ['ns=2;i=1', 'ns=2;i=22']
            mapping_data = [
  {'label': 'VVB001', 'keys': ['Value', 'Fatigue', 'Impact','Friction', 'Temperature', 'Crest', 'Status', 'OUT1', 'OUT2']},
  {'label': 'O5D100', 'keys': ['Value', 'Distance', 'Switch State']}
]
            sensor_data =  {}
            sensor_objects = await client.nodes.objects.get_children()
            for key, sensor_object in enumerate(sensor_objects):
                if key == 2 or key == 3:
                    key-=2
                    sensor_entries = await sensor_object.get_children()
                    final_array =  []
                    for entry_object in sensor_entries:
                        keys  = mapping_data[key]['keys']
                        variables = await entry_object.get_variables()
                        param_value = []
                        for variable in variables:
                            variable_value = await variable.read_value()
                            param_value.append(variable_value)
                        mapped_dict = dict(zip(keys, param_value))
                        final_array.append(mapped_dict)
                    sensor_data[mapping_data[key]['label']] = final_array
                

            i = 0
            while True:
                try:
                    i += 1
                    if i == 5:
                        return sensor_data
                    await asyncio.sleep(1)
                except asyncio.TimeoutError:
                    print("Timed out during sleep operation.")
                except Exception as e:
                    print(f"Unexpected error: {e}")
                except asyncio.CancelledError:
                    print("Task cancelled.")
                    return

        except ClientError as e:
            print(f"Client error: {e}")
            raise ClientError from e  # Re-raise for clarity
        except TimeoutError as e:
            print(f"Connection or server response timed out: {e}")
            raise TimeoutError from e  # Re-raise for clarity
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise RuntimeError from e  # Re-raise to allow specific handling

    return sensor_data


