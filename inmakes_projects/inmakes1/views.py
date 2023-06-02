from django.http import HttpResponse
from django.shortcuts import render
from inmakes1.models import Place, Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    per = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': per})
# def calculation(request):
#   x = int(request.GET['num1'])
#  y = int(request.GET['num2'])
# sum1 = x+y
# sub = x-y
# mult = x*y
# div = x/y

# return render(request,"result.html",{'result':sum1,'result1':sub,'result2':mult,'result3':div})
