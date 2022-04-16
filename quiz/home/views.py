from pprint import pprint

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
import random


# Create your views here.


def home(request):
    context = {'categories': Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request, 'home/home.html', context)


def quiz(request):
    context = {'category': request.GET.get('category')}
    return render(request, 'home/quiz.html', context)


def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))

        question_objs = list(question_objs)

        data = []
        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()
            })

        playload = {
            'status': True,
            'data': data
        }
        pprint(playload)

        return JsonResponse(playload)

    except Exception as e:
        print(e)

    return HttpResponse("Something went wrong")
