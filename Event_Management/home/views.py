from django.shortcuts import render,redirect
from django.contrib import messages
from home.models import User,Event,Booking,owner,Payment
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(uemail=email, upassword=password)
            request.session['uid'] = user.uid
            return redirect('/landing')
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('/login') 

    return render(request, 'login.html')

def register(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phno']
        password=request.POST['password']
        obj=User.objects.create(uname=name,uemail=email,uphone=phno,upassword=password)
        return redirect('/login',{'message':'registration successfull'})
    return render(request,'register.html')

def landing(request):  
    obj = Event.objects.all()
    return render(request,'landing.html',{'events':obj})


def createvent(request):
    if request.method == 'POST':     
            title = request.POST['title']
            desc = request.POST['desc']
            cities = request.POST['cities']
            location = request.POST['location']
            date = request.POST['date']
            time=request.POST['time']
            vprice = request.POST['vprice']
            gprice = request.POST['gprice']
            obj = Event.objects.create(
                
                etitle=title.upper(),
                edesc=desc,
                ecity=cities,
                elocation=location,
                edate=date,
                etime=time,
                vticket=vprice,
                gticket=gprice
            )
            return redirect('/adminlanding')
    
    return render(request, 'createvent.html')

def yourevents(request):
    object=Event.objects.all()
    return render(request, 'yourevents.html',{'events':object})

def deletevent(request,eid):
    obj=Event.objects.get(pk=int(eid))
    obj.delete()
    obj=Event.objects.all()
    return redirect('/yourevents')

def viewdetails(request,eid):
    obj=Event.objects.filter(pk=int(eid))
    return render(request, 'viewdetails.html',{'event':obj})

from django.utils.dateparse import parse_date, parse_time
import datetime

def editevent(request,eid):
    if request.method=='POST':
        title = request.POST['title']
        desc = request.POST['desc']
        cities = request.POST['cities']
        location = request.POST['location']
        date = request.POST['date']
        time=request.POST['time']
        vprice = request.POST['vprice']
        gprice = request.POST['gprice']
        date = parse_date(date)  
        time = parse_time(time) 
        object=Event.objects.get(pk=int(eid))
        object.etitle=title.upper()
        object.edesc=desc
        object.ecity=cities
        object.elocation=location
        object.edate=date
        object.etime=time
        object.vticket=vprice
        object.gticket=gprice
        object.save()
        return redirect("/yourevents")
    obj=Event.objects.get(pk=int(eid))
    return render(request, 'editevent.html', {'event':obj})

def book(request,eid):
    if request.method=='POST':
        uid=request.session['uid']
        event = Event.objects.get(pk=int(eid))
        ticket_type=request.POST['ticket_type']
        Quantity=request.POST['Quantity']
        booking =Booking.objects.create(
            eid=event,
            uid=User.objects.get(uid=uid),
            ttype=ticket_type,
            quantity=Quantity
        )
        return redirect('/landing')
    return render(request, 'booking.html')

def yourtickets(request):
    uid=request.session['uid']
    bookings=Booking.objects.filter(uid=int(uid))
    events = [booking.eid for booking in bookings]
    return render(request,'yourticket.html',{'bookings': bookings,'events':events})

def dashboard(request, eid):
    event = Event.objects.get(eid=eid)
    bookings = Booking.objects.filter(eid=event)
    context = {
        'event': event,
        'bookings': bookings,
    }

    return render(request, 'dashboard.html', context)

def adminlogin(request):
    if request.method=='POST': 
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = owner.objects.get(email=email, password=password)
            return redirect('/adminlanding')
        except owner.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('/adminlogin')

    return render(request, 'adminlogin.html')

def adminlanding(request):
    return render(request,'adminlanding.html')
