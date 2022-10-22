from django.shortcuts import render
from django.http import HttpResponse
from .models import RegisterModel
# Create your views here.
def home(request):
    return HttpResponse("Welcome to universal")
def index(request):
    return render(request,'register/index.html')
def register(request):
    if request.method=="POST":
        print("in post request")
        name=request.POST['name']
        email=request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        dob = request.POST['dob']
        profession = request.POST['profession']
        course = request.POST['course']
        print("name:",name)
        print("email:",email)
        print(dob)
        obj=RegisterModel.objects.create(name=name,email=email,phone=phone,gender=gender,profession=profession,course=course)
        obj.save()
    return render(request,'register/register.html')

def update(request):
    obj = None
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        dob = request.POST['dob']
        profession = request.POST['profession']
        course = request.POST['course']
        
        obj = RegisterModel.objects.get(id=int(request.POST['id']))
        obj.name = name
        obj.email = email
        obj.phone=phone
        obj.gender=gender
        obj.dob=dob
        obj.profession=profession
        obj.course=course
        obj.save()
        if request.POST['from'] == 'search':
            return render(request, 'register/update.html', {'name': obj.name, 'email': obj.email, 'id': obj.id, 'phone': obj.phone, 'dob': obj.dob, 'gender': obj.gender, 'profession': obj.profession, 'course': obj.course })
    return render(request, 'register/register.html')


def search(request):
    
    if request.method == "POST":
        if "id" in request.POST:
            name = request.POST['name']
            obj = RegisterModel.objects.get(id=request.POST['id'])
            obj.delete()
            queryset = RegisterModel.objects.all()
            return render(request, 'register/search.html', {'data': queryset})
            # return render(request, 'register/search.html', {})
        name = request.POST['name']
        queryset = RegisterModel.objects.filter(name=name)
        return render(request, 'register/search.html', {'data': queryset})
    queryset=RegisterModel.objects.all()
    return render(request, 'register/search.html', {'data': queryset})
    
    