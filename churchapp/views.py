from django.shortcuts import render
from django.http import HttpResponse
# importing contents for models 
from . models import Women_ministry
# view for the main page(home page)
def home(request):
    return render(request,'home.html')
#view for the contact_us page
def contact_us(request):
    return render(request,'contact_us.html')
#view for the church_library page
def church_library(request):
    return render(request,'church_library.html')
#view for women_ministry page 
def women_ministry(request):
    return render(request,'women_ministry.html')
#view for men_ministry page 
def men_ministry(request):
    return render(request,'men_ministry.html')
#view for youth_ministry page 
def youth_ministry(request):
    return render(request,'youth_ministry.html')
#view for prayer_request page 
def prayer_request(request):
    return render(request,'prayer_request.html') 
#view for prayer_request page 
def choir_ministry(request):
    return render(request,'choir_ministry.html') 



