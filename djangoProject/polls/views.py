# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from .models import Question

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # #render(request, template name, (optional)dict) returns HttpResponse
    # return render(request, 'polls/index.html', context)
    return render(request, 'polls/index.html')

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)