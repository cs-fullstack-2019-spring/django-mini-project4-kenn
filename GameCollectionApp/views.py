from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CollectorModel, CollectorForm, GameModel, GameForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    # If the current person is logged in, do the code below
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable collector
        collector = CollectorModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user using the variable you just created
        allEntries = GameModel.objects.filter(foreignKeyToCollector = collector)
    # If the user is not logged in...
    else:
        # Make all Entries blank because you need this because both the index.html page is expecting a allEntries variable
        allEntries = ""
    context = {"allEntries": allEntries}
    return render(request, "GameCollectionApp/index.html", context)


def newCollector(request):
    # POST Request
    # If the form is being pushed to this function
    if request.method == "POST":
        print(request.method)
        # This will put all the user's information from the HTML page into this new form variable
        form = CollectorForm(request.POST)
        # Run all the validation on this form
        if form.is_valid():
            # Save the form's information in the model
            form.save()
            # Create a new Django User entry
            User.objects.create_user(request.POST["username"], "", request.POST["password1"])
            return redirect("index")
        else:
            context={
                "errors": form.errors,
                "form": form
            }
            return render(request, "GameCollectionApp/newCollector.html", context)


    # GET Request
    else:
        # This will create a blank form using CollectorForm
        form = CollectorForm()
        context = {"form": form}
        return render(request, "GameCollectionApp/newCollector.html", context)


def addGame(request):
    # This will create a blank form using CollectorForm
    form = GameForm()
    context = {
        "form": form
    }
    return render(request, "GameCollectionApp/addGame.html", context)


def gotGameInfo(request):
    # This will put all the user's information from the HTML page into this new form variable
    form = GameForm(request.POST)
    # This puts the logged in user entry into the variable collector
    collector = CollectorModel.objects.get(username=request.user)

    # Shorter but more confusing way to add an entry not in the form
    # newForm = form.save(commit=False)
    # newForm.foreignKeyToCollector = collector
    # newForm.save()

    # Easier but longer way to create a game from the logged in user
    if form.is_valid():
        # Created a new GameMode entry usin the user's form information that was passed using the request.POST
        GameModel.objects.create(name=request.POST["name"], developer=request.POST["developer"], dateMade =request.POST["dateMade"], ageLimit=request.POST["ageLimit"], foreignKeyToCollector=collector)
        return redirect("index")
    else:
        context = {"form":form, "errors":form.errors}
        return render(request, "GameCollectionApp/addGame.html", context)


def editGame(request, gameID):
    # Grab an exact entry of the GameModel using the primary key
    editExistingGame = get_object_or_404(GameModel, pk=gameID)

    # Post method
    if request.method == "POST":
        # This will fill in the form with the user's information and use the exact GameModel with primary key
        form = GameForm(request.POST, instance=editExistingGame)
        if form.is_valid():
            form.save()
        else:
            print("Form is not valid")
        return redirect("index")

    # Get method
    # Grabbed the exact game form using the existing game model using the primary key from earlier
    form = GameForm(instance=editExistingGame)
    context = {
        "form": form,
        "gameID": gameID
    }
    return render(request, "GameCollectionApp/editGame.html", context)


# def gotEditGameInfo(request):
#
#     form = GameForm(request.POST, instance=)
#     form.save()
#     return redirect("index")

def deleteGame(request, gameID):
    deleteThisGame = get_object_or_404(GameModel, pk=gameID)
    deleteThisGame.delete()
    return redirect("index")
