from django.shortcuts import render
from .models import Products,Laundry,Land
# Create your views here.
def index(request):
    products=Products.objects.all()
    laundry=Laundry.objects.all()
    land=Land.objects.all()
    data={'products':products,'laundry':laundry,'land':land}
    return render(request,'services/index.html',data)
