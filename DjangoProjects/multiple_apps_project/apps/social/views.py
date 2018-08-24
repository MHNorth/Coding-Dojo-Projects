from django.contrib import messages
from time import localtime, strftime
from django.shortcuts import render, redirect
import random, datetime
from apps.accounts.models import User
from .models import Word, Survey



##---------- Social Views ----------##
def Home(request, *args, **kwargs): 
        """
        Renders the home.html template which 
        list the current date and local time

        """
        datenow = strftime("%B %d, %Y", localtime())
        timenow = strftime("%H:%M %p", localtime())
        context = {
                'timenow': timenow,
                'datenow': datenow,
        }
        return render(request, 'social/home.html', context)   

def Friends(request, *args, **kwargs):
        if "user_id" not in request.session:
                return(redirect("homepage"))        
        return render(request, 'social/friends.html',) 

def AddFriend(request, *args, **kwargs):
        if "user_id" not in request.session:
                return(redirect("homepage"))
        return redirect('friends')

def Connect(request, *args, **kwargs):
        if "user_id" not in request.session:
                return(redirect("homepage"))
        return redirect('friends')

def Detail(request, *args, **kwargs):
        if "user_id" not in request.session:
                return(redirect("homepage"))
        return render(request, 'social/detail.html')

def Removed(request, *args, **kwargs):
        if "user_id" not in request.session:
                return(redirect("homepage"))
        return render(request, 'social/remove_friend.html')


##---------- Random Word Generator Views ----------##

wordlist = Word.objects.all()
info = {'num_visits': 1, 'randword': random.choice(wordlist)}

def RandomWord(request, *args, **kwargs):
        context = {
                'count': info['num_visits'],
                'randomword': info['randword'],
        }

        return render(request,'social/random.html', context) 

def WordGenerator(request, *args, **kwargs):
        """
        Renders a random word to the user

        """ 
        if request.session:
                info['num_visits'] += 1
                info['randword'] = random.choice(wordlist)

        return redirect('random')


def Resetword(request, *args, **kwargs):
        request.session.clear()
        info['num_visits'] = 1
        return redirect('random')

        

##---------- Face Detection Views ----------##
def FaceDetection(request, *args, **kwargs):

        return render(request, 'social/face_detection.html')


##---------- Ninja Gold Views ----------##

def NinjaGold(request, *args, **kwargs):

        return render(request, 'social/ninja_gold.html')

def ProcessGold(request, *args, **kwargs):

        if request.method == 'POST':
                
                gold_location = request.POST["location"]
                time = strftime("%Y/%m/%d %#I:%M %p", localtime())
                gold_earned = 0

                if 'gold' not in request.session:
                        request.session["gold"] = 0

                if 'activities' not in request.session:
                        request.session["activities"] = []

                if request.POST['location'] == "farm":
                        gold_earned += random.randint(10, 20)

                if request.POST['location'] == "cave":
                        gold_earned += random.randint(5, 10)

                if request.POST['location'] == "house":
                        gold_earned += random.randint(2, 5)

                if request.POST['location'] == "casino":
                        gold_earned += random.randint(-50, 50)

                request.session["gold"] += gold_earned
                time = datetime.datetime.strftime(datetime.datetime.now(), "%Y/%m/%d %I:%M %p")
                
                if gold_earned > 0:
                        request.session["activities"].append(
                        "You went to the {} and earned {} gold at ({})".format(gold_location, gold_earned, time))
                elif gold_earned == 0:
                        request.session["activities"].append(
                                "You went to the casino and left with the same amount of money. ({})".format(time))  
                else:
                        request.session["activities"].append(
                        "You went to the casino and lost {} gold at ({})".format(gold_earned, time))
                        print(request.session["activities"])

                
        return redirect('ninja')


def reset(request):
        request.session.clear()
        return redirect('ninja')



##---------- Session Views ----------##

def SessionWords(request, *args, **kwargs):
        return render(request, 'social/session_words.html')


def Addword(request, *args, **kwargs):

        if request.method == 'POST':
                wordtime = strftime("%B %d, %Y %H:%M %p", localtime())
                if 'word' not in request.session:
                        request.session['word'] = []

                if 'Bigfont' in request.POST:
                        info = {
                                'word': request.POST['addword'],
                                'color': request.POST['color'],
                                'font': 'sbig',
                                'time': wordtime,
                        }
                else:
                        info = {
                                'word': request.POST['addword'],
                                'color': request.POST['color'],
                                'font': 'ssmall',
                                'time': wordtime, 
                        }

                request.session['word'].append(info)
                request.session.modified = True

                print(request.session['word'])

        return redirect('session')

def Clear(request, *args, **kwargs):
        request.session.clear()
        return redirect('session')



##---------- Survey Form Views ----------##

count = {'num': 0}

def SurveyForm(request, *args, **kwargs):
        return render(request, 'social/survey_form.html')

def SurveryFormSubmit(request, *args, **kwargs):
        """
        A survey that gets user information and 
        posts survey info on alternate page

        """ 

        if request.method == "POST":
                request.session['name'] = request.POST['name']
                request.session['dojo'] = request.POST['dojo']
                request.session['language'] = request.POST['language']
                request.session['comment'] = request.POST['comment']

        request.session.modified = True
        return redirect('results')    


def Results(request, *args, **kwargs): 
        request.session
        count['num'] += 1 
        context = {
                'count': count['num']
        }
        return render(request, 'social/survey_form_results.html', context)


##---------- Upload Views ----------##
def Upload(request, *args, **kwargs):
        # if request.method == 'POST':
        #         form = UploadFileForm(request.POST, request.FILES)
        #         if form.is_valid():
        #                 handle_uploaded_file(request.FILES['file'])
        #                 return HttpResponseRedirect('/success/url/')
        # else:
        #         form = UploadFileForm()
        return render(request, 'social/upload_file.html', )  #{'form':form}













 
