# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User #Módulo para usuarios
from django.contrib.auth import authenticate, login
#Vistas

def authentication(request):
    if request.method == 'POST': # Se asegura de que la acción es un POST
        action = request.POST.get('action', None) #LLamada de metodos de POST, tanto para username como password
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'singup':
            user = User.objects.create_user(username=username, password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password) #Función interna de authenticate
            # Compara lo enviado por el usuario con sus datos de username y password
            login(request, user)# Función interna de Django
        return redirect('/') # Función de Django

    return render(request, 'login.html', {})

def hello(request):
    return render(request, 'hello.html',{})
