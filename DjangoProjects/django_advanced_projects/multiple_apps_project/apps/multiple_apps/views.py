##---------- Imported Modules ----------##
import os
import random, datetime

from django.views.decorators.http import require_POST
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView


from .models import Word, Survey, UploadFile, UploadImage
from .forms import ImageUploadForm, FileUploadForm
from django.forms import modelformset_factory
from time import localtime, strftime

##----------------------------------------##



##---------- Social Views ----------##
def Home(request): 
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
        return render(request, 'multiple_apps/home.html', context)   

def Friends(request, *args, **kwargs):
        if "user_id" not in request.session:
                return(redirect("homepage"))        
        return render(request, 'multiple_apps/friends.html',) 

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
        return render(request, 'multiple_apps/detail.html')

def Removed(request, *args, **kwargs):
        if "user_id" not in request.session:
                return(redirect("homepage"))
        return render(request, 'multiple_apps/remove_friend.html')


##---------- Random Word Generator Views ----------##

wordlist = Word.objects.all()
info = {'num_visits': 1, 'randword': random.choice(wordlist)}

def RandomWord(request, *args, **kwargs):
        context = {
                'count': info['num_visits'],
                'randomword': info['randword'],
        }

        return render(request,'multiple_apps/random.html', context) 

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


##---------- Ninja Gold Views ----------##

def NinjaGold(request, *args, **kwargs):

        return render(request, 'multiple_apps/ninja_gold.html')

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
        return render(request, 'multiple_apps/session_words.html')


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
        return render(request, 'multiple_apps/survey_form.html')

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
        return render(request, 'multiple_apps/survey_form_results.html', context)


##---------- Upload Views ----------##


def Upload(request): 
        all_files = UploadFile.objects.all()
        all_images = UploadImage.objects.all()
        image_form = forms.ImageUploadForm()
        file_form = forms.FileUploadForm()
        upload_files = UploadFile()
        
        context = {
        "images_key": all_images,
        "form_key": image_form,
        "file_fr": file_form,
        "upload_key": upload_files,
        "files_key": all_files,
        }

        return render(request, 'multiple_apps/upload_file.html', context) 


def Upload_Images(FormView):
                    
        form_class = forms.ImageUploadForm
        template_name='upload_file.html'
        success_url = '/upload/'


        def post(self, request, *args, **kwargs):
                form_class = self.get_form_class()
                form = self.get_form(form_class)
                files = request.FILES.getlist('image')
                
                if form.is_valid():
                        return self.form_valid(form)
                else:
                        return self.form_invalid(form)


def Upload_Files(request):
        
        if request.method=="POST":
                upload_files = UploadFile()
                upload_files.post(request)
        else:
                return redirect('upload')











 
