from django.urls import path
from . import views


urlpatterns = [
        path('', views.Home, name='homepage'),
        path('friends', views.Friends, name='friends'),
        path('addfriend', views.AddFriend, name='addfriend'),
        path('connect', views.Connect, name='connectfriends'),
        path('detail', views.Detail, name='detail'),
        path('removed', views.Removed, name='removed'),
        path('random', views.RandomWord, name='random'),
        path('resetword', views.Resetword, name='resetword'),
        path('generate', views.WordGenerator, name='generate'),
        path('ninjagold', views.NinjaGold, name='ninja'),
        path('processgold', views.ProcessGold, name='process'),
        path('reset', views.reset, name='reset'),
        path('sessions', views.SessionWords, name='session'),
        path('addwords', views.Addword, name='addwords'),
        path('clear', views.Clear, name='clear'),       
        path('survey', views.SurveyForm, name='survey'),
        path('survey/submit', views.SurveryFormSubmit, name='surveysubmit'),
        path('results', views.Results, name='results'),
        path('upload', views.Upload, name='upload'),
        path('upload/file/', views.Upload_file, name='uploadfile'),
        path('upload/image/', views.Upload_image, name='uploadimage')
        
]
