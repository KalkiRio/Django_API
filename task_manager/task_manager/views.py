from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Task Manager API</h1><p>Go to <a href='/api/docs/'>API Docs</a></p>")
