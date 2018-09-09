from django.shortcuts import render, redirect
from .models import User, Trip, Jointrip
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "belt_app/index.html")

def register(request):
    print(request.POST)
    results = User.objects.register(request.POST)

    if results[0]:
        request.session["user_id"] = results[1].id
        request.session["first_name"] = results[1].first_name
        request.session["last_name"] = results[1].last_name
        return redirect("/travels/{}".format(request.session["user_id"]))
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect("/")

def login(request):
    print(request.POST)
    results = User.objects.login(request.POST)

    if results[0]:
        request.session["user_id"] = results[1].id
        request.session["first_name"] = results[1].first_name
        request.session["last_name"] = results[1].last_name
        return redirect("/travels/{}".format(request.session["user_id"]))
    else:
        # print(results[1])
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")

def trips(request):
    if "user_id" not in request.session:
        messages.add_message(request, messages.ERROR, "You need to login first")
        return redirect("/")

    data = {
        "trips": Trip.objects.all()
    }
    return render(request, "belt_app/dashboard.html", data)

def add_trip(request):
    if "user_id" not in request.session:
        messages.add_message(request, messages.ERROR, "You need to login first")
        return redirect("/")

    data = {
        "trips": Trip.objects.all()
    }
    return render(request, "belt_app/addtrip.html", data)

def travels(request, user_id):
    print(user_id)

    all_trips = Trip.objects.all()
    joined_trips = Jointrip.objects.filter(user=user_id)
    
    for join in joined_trips:
        all_trips = all_trips.exclude(id=join.trip.id)

    data = {
        "all_trips": all_trips,
        "joined_trips": joined_trips,
    }
    return render(request, "belt_app/dashboard.html", data)
    
def add(request):
    print(request.POST)
    results = Trip.objects.add(request.POST, request.session["user_id"])
    if not results[0]:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect("/add_trip")
    else:
        # print(results[1].id, type(results[1].id))
        Jointrip.objects.join(results[1].id, request.session["user_id"])
    return redirect("/travels/{}".format(request.session["user_id"]))
    

def jointrip(request, trip_id):
    # Trip.objects.join(trip_id, request.session["user_id"])
    Jointrip.objects.join(trip_id, request.session["user_id"])
    return redirect("/travels/{}".format(request.session["user_id"]))

# def remove(request, trip_id):
#     Trip.objects.get(id=trip_id).delete()
#     return redirect("/dashboard/{}".format(request.session["user_id"]))

def showtrip(request, trip_id):
    print(trip_id)
    trip = Trip.objects.get(id=trip_id)
    join = Jointrip.objects.filter(trip_id=trip_id)
    return render(request, "belt_app/view.html", {"trip": trip, "joins": join})
    # return redirect("/travels/{}".format(request.session["user_id"]))

def leave_trip(request, trip_id):
    joined_trips = Jointrip.objects.filter(trip_id=trip_id).filter(user_id=request.session["user_id"])
    joined_trips.delete()
    return redirect("/travels/{}".format(request.session["user_id"]))

def delete_trip(request, trip_id):
    print(trip_id)
    trip = Trip.objects.filter(id=trip_id)
    print(trip, type(trip))
    trip.delete()
    return redirect("/travels/{}".format(request.session["user_id"]))
