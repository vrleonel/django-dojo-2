from django.shortcuts import render
from app.models import Task
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_tasks(request):
    qs = Task.objects.all()
    qs = qs.filter(author=request.user)
    tasks = list(qs.values())

    return JsonResponse(tasks, safe=False)


def login(request):
    return render(request, 'login.html', context={})
