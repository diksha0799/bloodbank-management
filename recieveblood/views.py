from django.shortcuts import render, HttpResponse
from recieveblood.models import Hospital

def home(request):
    return render(request, 'home.html')

def hospital(request):
    hospitals = Hospital.objects.all()
    context = { 'hospitals':hospitals
    }

    return render(request, 'hospital.html', context)

def registerhospital(request):
    error = ""
    user="none"
    if request.method == 'POST':
        hospitalname = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        birthdate = request.POST['dateofbirth']
        bloodsample = request.POST['bloodsample']
        try:
            if password == repeatpassword:
                Hospital.objects.create(hospitalname=hospitalname,email=email,password=password,phonenumber=phonenumber,address=address,bloodsample=bloodsample)
                user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
                rec_group = Group.objects.get(name='Hospital')
                rec_group.user_set.add(user)
                user.save()
                error = "no"
            else:
              error = "yes"
        except Exception as e:
               error = "yes"
    d = {'error' : error}
    return render(request,'registerhospital.html',d)

    
def registerreciever(request):
    error = ""
    user="none"
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']
        gender = request.POST['gender']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        birthdate = request.POST['dateofbirth']
        bloodgroup = request.POST['bloodgroup']
        try:
            if password == repeatpassword:
                Reciever.objects.create(name=name,email=email,password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodsample=bloodsample)
                user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
                rec_group = Group.objects.get(name='Reciever')
                rec_group.user_set.add(user)
                user.save()
                error = "no"
            else:
              error = "yes"
        except Exception as e:
               error = "yes"
    d = {'error' : error}
    return render(request,'registerreciever.html',d)

def login(request):
    error = ""
    page = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(request,username=u,password=p)
        try:
            if user is not None:
                login(request,user)
                error = "no"
                g = request.user.groups.all()[0].name
                if g == 'Reciever':
                   page = "reciever"
                   d = {'error': error,'page':page}
                   return render(request,'reciever.html',d)
                elif g == 'Hospital':
                    page = "hospital"
                    d = {'error': error,'page':page}
                    return render(request,'hoispital.html',d)
            else:
                error = "yes"
        except Exception as e:
            error = "yes"
    return render(request,'login.html')