
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def login_view(request):
    with open('request_log.txt', 'a') as log_file:
        log_file.write(f"Method: {request.method}\n")
        log_file.write(f"Path: {request.path}\n")
        log_file.write(f"GET parameters: {request.GET}\n")
        log_file.write(f"POST parameters: {request.POST}\n")
        log_file.write(f"Headers: {dict(request.headers)}\n")
        log_file.write("\n")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bboard:my_view')
        else:
            return redirect('bboard:invalid_login_view')
    return render(request, 'login.html')
def invalid_login_view(request):
    return HttpResponse('<h1>Invalid login</h1>')
def my_view(request):
    return HttpResponse('<h1>Welcome</h1>')


