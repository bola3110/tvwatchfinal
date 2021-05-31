from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests

from .models import User, Tvshow, Mylist, Newsletter


def index(request):
    '''
        This function returns the user to the homepage.
    '''
    return render(request, "tvwatch/index.html")

def login_view(request):
    '''
        This function lets the user login.

        Steps:
        1. Attempt to sign user in.
        2. Check if authentication successful.
    '''
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("add_interest"))
        else:
            return render(request, "tvwatch/sign.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "tvwatch/sign.html")

def register(request):
    '''
        This function lets the user register.

        Steps:
        1. Ensure password matches confirmation.
        2. Attempt to create new user.
    '''
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "tvwatch/sign.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "tvwatch/sign.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return render(request,"tvwatch/interest.html")
    else:
        return render(request, "tvwatch/sign.html")

def logout_view(request):
    '''
        This function lets the user logout.
    '''
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def about_view(request):
    '''
        This function returns the user to the about page.
    '''
    return render(request,"tvwatch/about.html")

def newsletter(request):
    '''
        This function lets users subscribe to our newsletter.

        Steps:
        1. getting email from the user.
        2. saving the email in the database for later use (marketing).

    ''' 
    if request.method == "POST":
        newsletter = request.POST["newsletter"]
        existing_newsletters = Newsletter.objects.all()

        found = False
        for x in existing_newsletters:
            if newsletter == x.newsletter:
                found = True

        if found != True:
            try:
                newsletter = Newsletter(
                    newsletter=newsletter)
                newsletter.save()

                return redirect(request.META['HTTP_REFERER'])
            except IntegrityError:
                return render(request, "tvwatch/interest.html", {
                    "message": "Er is iets fouts gegaan"
                })
    return redirect(request.META['HTTP_REFERER'])

@login_required
def detail_view(request):
    '''
        This function gets the detailed info of the selected Tv-show from the API.

        Steps:
        1. Getting ID and name of the detailed tv-show as input.
        2. fetching youtubeurl, detailed info and similar tv-shows from the API.
        3. returning the user to the detail page.
    ''' 
    if request.method == "POST":
        tvid = request.POST["tvid"]
        name = request.POST["name"]
        original_language = request.POST.get("original_language", "")
        vote_average = request.POST.get("vote_average", "")
        release_year = request.POST.get("first_air_date", "")
        genre_ids = request.POST.get("genre_ids", "")

        # Youtubeurl Tv-show
        y=requests.get(f"https://api.themoviedb.org/3/tv/{tvid}/videos?api_key=ee98bfe4da01cc400b4f3028b791aee7")
        url = y.json()
        if url["results"] == []:
            youtubeurl = "slx9VvyBq5g"
        else:
            youtubeurl = url["results"][0]["key"]

        # Detailed info tv-show
        r=requests.get(f"https://api.themoviedb.org/3/search/tv?api_key=ee98bfe4da01cc400b4f3028b791aee7&language=en-US&page=1&query={name}&include_adult=false")
        data = r.json()
        tvshows=[]
        for row in data["results"]:
            if row["id"] ==  int(tvid):
                tmp={
                    "name": row["name"],
                    "overview": row["overview"],
                    "poster_path": row["poster_path"],
                    "vote_average":  row["vote_average"],
                    "tvid": row["id"]
                }
                tvshows.append(tmp)

        # Similar Tv-shows
        reccomended=requests.get(f"https://api.themoviedb.org/3/tv/{tvid}/recommendations?api_key=ee98bfe4da01cc400b4f3028b791aee7&language=en-US&page=1")
        data = reccomended.json()
        rec_tvshows=[]
        for row in data["results"]:
            tmp={
                "name": row["name"],
                "overview": row["overview"],
                "poster_path": row["poster_path"],
                "vote_average":  row["vote_average"],
                "tvid": row["id"],
                "genre_ids": row["genre_ids"][0],
                "original_language": row["original_language"],
                "first_air_date": row["first_air_date"]
            }
            rec_tvshows.append(tmp)

    return render(request,"tvwatch/detail.html", {
        "tvshows": tvshows,
        "youtubeurl": youtubeurl,
        "rec_tvshows": rec_tvshows
    })

@login_required
def add_interest(request):
    '''
        This function lets the user add their interest and gets data from the API.

        Steps:
        1. Gets the input from the page.
        2. Saving the input of the different parameters to the Tvshow class in models.py.
        3. Redirecting to 'reccomended' function. 
    ''' 
    if request.method == "POST":
        genre = request.POST["genre"]
        language = request.POST["language"]
        vote_average = request.POST["vote_average"]
        release_year = request.POST["release_year"]
        try:
            tvshow = Tvshow(
                user=request.user,
                genre=genre, 
                language=language, 
                vote_average=vote_average, 
                release_year=release_year)
            tvshow.save()

        except IntegrityError:
            return render(request, "tvwatch/interest.html", {
                "message": "Er is iets fouts gegaan"
            })
    return redirect('reccomended')

@login_required
def reccomended(request):
    '''
        This function lets the user add their interest and gets data from the API.

        Steps:
        1. Using the parameters to request data from the API.
        2. Looping through the results and saving the relevent info in a dictionary inside a list.
        3. returning this list with data and the user to the tvshow page.
    ''' 
    tvshow = Tvshow.objects.get(user=request.user)

    r=requests.get(f"https://api.themoviedb.org/3/discover/tv?sort_by=popularity.desc&api_key=ee98bfe4da01cc400b4f3028b791aee7&with_genres={tvshow.genre}&with_original_language={tvshow.language}&vote_average.gte={tvshow.vote_average}&first_air_date.gte={tvshow.release_year}")
    data = r.json()
    tvshows=[]
    for row in data["results"]:
        tmp={
            "name": row["name"],
            "overview": row["overview"],
            "poster_path": row["poster_path"],
            "vote_average":  row["vote_average"],
            "tvid": row["id"]
        }
        tvshows.append(tmp)
    return render(request,"tvwatch/tvshow.html", {
        "tvshows": tvshows
    })

@login_required  
def add_mylist(request):
    '''
        This function lets the add Tv-shows to their personal list.

        Steps:
        1. Getting ID and name of the detailed Tv-show as input from the page (if user wants to add a new tv-show to their list).
        2. Checking if the Tv-show is already listed in the database.
        3. Adding new Tv-shows to the list (if it doesn't exist yet).
        4. Redirecting to 'mylist' function. 
    '''  
    if request.method == "POST":
        mylistuser = Mylist.objects.filter(user=request.user).all()
        name = request.POST["name"]
        tvid = request.POST["tvid"]
        found = False
        for x in mylistuser:
            if name == x.mylist:
                found = True

        if found != True:
            try:
                mylist = Mylist(
                    user=request.user,
                    mylist=name,
                    tvid=tvid )
                mylist.save()

            except IntegrityError:
                return render(request, "tvwatch/interest.html", {
                    "message": "Er is iets fouts gegaan"
                })
    return redirect('mylist')        

@login_required  
def mylist(request):
    '''
        This function lets the add Tv-shows to their personal list.

        Steps:
        1. Fetching info of all the listed tv-shows from the API.
        2. Returning the user and the data to the My list page. 
    '''  
    mylistuser = Mylist.objects.filter(user=request.user).all()
    tvshow = Tvshow.objects.get(user=request.user)
    mytvshows=[]
    for x in mylistuser:
        m=requests.get(f"https://api.themoviedb.org/3/search/tv?api_key=ee98bfe4da01cc400b4f3028b791aee7&language=en-US&page=1&query={x}&include_adult=false")
        mylistdata = m.json()
        
        for row in mylistdata["results"]:
            if row["name"] == x.mylist and int(row["id"]) == int(x.tvid):
                tmp={
                    "name": row["name"],
                    "overview": row["overview"],
                    "poster_path": row["poster_path"],
                    "vote_average":  row["vote_average"],
                    "tvid": row["id"]
                }
                mytvshows.append(tmp)
        
    return render(request,"tvwatch/mylist.html", {
        "mytvshows": mytvshows
    })

@login_required
def remove_mylist(request):
    '''
        This function lets the user remove Tv-shows from their list.

        Steps:
        1. Getting ID and name of the detailed tv-show as input from the page.
        2. Checking if the Tv-show exists in the database of the user.
        3. Removing the Tv-show from the database.
        4. Redirecting to add_mylist (to show data to the user)
    '''
    if request.method == "POST":
        mylistuser = Mylist.objects.filter(user=request.user).all()
        name = request.POST["name"]
        tvid = request.POST["tvid"]
        
        for x in mylistuser:
            if name == x.mylist:
                x.delete()
            
    return redirect('add_mylist')