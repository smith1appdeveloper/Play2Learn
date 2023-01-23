import json
import re
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from users.forms import CustomUserChangeForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import AddScoreM
from json import dumps

class MathFactsView(TemplateView):
    template_name =  'mathfacts/mathfacts.html'

class MFAView(TemplateView):
    template_name = 'mathfacts/mfa.html'

class MFDView(TemplateView):
    template_name = 'mathfacts/mfd.html'

class MFMView(TemplateView):
    template_name = 'mathfacts/mfm.html'

class MFSView(TemplateView):
    template_name = 'mathfacts/mfs.html'

def FinalView(request):
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
            new_score = AddScoreM(username=username,score=score,scoreM=scoreM)
            new_score.save()
            return render(request, 'mathfacts/final.html', {})
        except:
            score = request.POST.get('addScore',False)
            scoreM = request.POST.get('addScoreM',False)
            new_score = AddScoreM(username=username,score=score,scoreM=scoreM)
            new_score.save()
            print("had an issue with Math Fact's game data transfer. Used second option, transfer complete.")
            return render(request, 'mathfacts/final.html', {})

    else:
        return render(request, 'mathfacts/final.html', {})
        print('anonymous user, database update not performed.')

def GametrackView(request):
    try:
        data = AddScoreM.objects.all().filter(username=request.user).order_by('-score').values()[:5]
        return render(request, 'mathfacts/gametrackmf.html', {'data' : data})
    except:
        return HttpResponse('Had a issue')

def LeaderboardView(request):
    try:
        data = AddScoreM.objects.all().order_by('-score').values()[:10]
        return render(request, 'mathfacts/leaderboardmf.html', {'data' : data})
    except:
        return HttpResponse('Had a issue')



