from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomerQuery
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def submitform(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            name = request.POST['name']
            message = request.POST['message']
            if len(email)==0 or len(name)==0 or len(message)==0:
                return HttpResponse({'failed'})
        
            custQuery = CustomerQuery.objects.create(name=name, email=email,message=message)
            return HttpResponse({'success'})
    except Exception as e:
        print(str(e))
        return HttpResponse({'failed'})

