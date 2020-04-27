from django.shortcuts import render
from motorcycles.models import Motorcycle

# Create your views here.
def do_search(request):
    motorcycles = Motorcycle.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"motorcycles":motorcycles})
