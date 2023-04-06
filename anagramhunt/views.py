import json
import re
from json import dumps
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from .models import AddScore


class AnagramHuntView(TemplateView):
    template_name =  'anagramhunt/anagramhunt.html'

class AHGameplayView(TemplateView):
    template_name = 'anagramhunt/ah_gameplay.html'

def AHView(request):
    username = str(request.user)
    if username != "AnonymousUser" :
        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        try:
            data = json.loads(request.body)
            score = data['addScore']
            scoreM = data['addScoreM']
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            return render(request, 'anagramhunt/ah_final.html', {})
        except:
            score = request.POST.get('addScore',False)
            print(score)
            scoreM = request.POST.get('addScoreM',False)
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            print("had an issue with Anagram Hunt's game data transfer. Used second option, transfer complete.")
            return render(request, 'anagramhunt/ah_final.html', {})

    else:
        return render(request, 'anagramhunt/ah_final.html', {})
        print('anonymous user, database update not performed.')

def AHView2(request):
    username = str(request.user)
    if username != "AnonymousUser" :
        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        try:
            data = json.loads(request.body)
            score = data['addScore']
            scoreM = data['addScoreM']
            lastAnagram = data['lastAnagram']
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            return render(request, 'anagramhunt/ah_final2.html', {})
        except:
            score = request.POST.get('addScore',False)
            print(score)
            scoreM = request.POST.get('addScoreM',False)
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            print("had an issue with Anagram Hunt's game data transfer. Used second option, transfer complete.")
            return render(request, 'anagramhunt/ah_final2.html', {})

    else:
        return render(request, 'anagramhunt/ah_final2.html', {})
        print('anonymous user, database update not performed.')

def AHView3(request):
    username = str(request.user)
    if username != "AnonymousUser" :
        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        try:
            data = json.loads(request.body)
            score = data['addScore']
            scoreM = data['addScoreM']
            lastAnagram = data['lastAnagram']
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            return render(request, 'anagramhunt/ah_final3.html', {})
        except:
            score = request.POST.get('addScore',False)
            print(score)
            scoreM = request.POST.get('addScoreM',False)
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            print("had an issue with Anagram Hunt's game data transfer. Used second option, transfer complete.")
            return render(request, 'anagramhunt/ah_final3.html', {})

    else:
        return render(request, 'anagramhunt/ah_final3.html', {})
        print('anonymous user, database update not performed.')

def AHView4(request):
    username = str(request.user)
    if username != "AnonymousUser" :
        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        try:
            data = json.loads(request.body)
            score = data['addScore']
            scoreM = data['addScoreM']
            lastAnagram = data['lastAnagram']
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            return render(request, 'anagramhunt/ah_final4.html', {})
        except:
            score = request.POST.get('addScore',False)
            print(score)
            scoreM = request.POST.get('addScoreM',False)
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            print("had an issue with Anagram Hunt's game data transfer. Used second option, transfer complete.")
            return render(request, 'anagramhunt/ah_final4.html', {})

    else:
        return render(request, 'anagramhunt/ah_final4.html', {})
        print('anonymous user, database update not performed.')

def AHViewVictory(request):
    username = str(request.user)
    if username != "AnonymousUser" :
        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        try:
            data = json.loads(request.body)
            score = data['addScore']
            scoreM = data['addScoreM']
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            return render(request, 'anagramhunt/ah_victory.html', {})
        except:
            score = request.POST.get('addScore',False)
            print(score)
            scoreM = request.POST.get('addScoreM',False)
            new_score = AddScore(username=username,score=score,scoreM=scoreM)
            new_score.save()
            print("had an issue with Anagram Hunt's game data transfer. Used second option, transfer complete.")
            return render(request, 'anagramhunt/ah_victory.html', {})

    else:
        return render(request, 'anagramhunt/ah_victory.html', {})
        print('anonymous user, database update not performed.')

def GametrackView(request):
    try:
        data = AddScore.objects.all().filter(username=request.user).order_by('-score').values()[:5]
        return render(request, 'anagramhunt/gametrackah.html', {'data' : data})
    except:
        return HttpResponse('Had a issue')

def LeaderboardView(request):
    try:
        data = AddScore.objects.all().order_by('-score').values()[:10]
        return render(request, 'anagramhunt/leaderboardah.html', {'data' : data})
    except:
        return HttpResponse('Had a issue')