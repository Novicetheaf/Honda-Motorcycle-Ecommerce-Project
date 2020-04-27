from django.shortcuts import render
from .models import Motorcycle

# Create your views here.
def all_motorcycles(request):
    motorcycles = Motorcycle.objects.all()
    return render(request, "products.html", {"motorcycles": motorcycles})
