from django.shortcuts import render
from django.http import HttpResponse
# we have to import random function
import random

# Create your views here.

def home(request):
    return render(request, 'generator\home.html')

def about(request):
    return render(request, 'generator/about.html')

def generatedpassword(request):

    # from list, we can select out characters randomly
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # control well if the user selects how many passwords to be displayed, 
    # inside html, we set select name="length"
    looptimes = int(request.GET.get('length',12))

    # control well if the user selects Uppercase,
    #inside html, we set name="showuppercase"
    if request.GET.get('showuppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # control well if the user selects Numbers,
    #inside html, we set name="shownumbers"
    if request.GET.get('shownumbers'):
        characters.extend(list('0123456789'))

    # control well if the user selects Special Characters,
    #inside html, we set name="showspecial"
    if request.GET.get('showspecial'):
        characters.extend(list('!@#$%^&*()"\|{[}]~`?/><.,'))

    # by default the password is empty
    theluckypassword = ''

    # we have to make it randomly loop 10 times
    # looptimes = 10

    # go loop 10 times
    for x in range(looptimes):

        # each time looping, go look for characters randomly and then pass to theluckpassword
        theluckypassword += random.choice(characters)

    return render(request, 'generator\password.html', {'genpassword': theluckypassword})
    