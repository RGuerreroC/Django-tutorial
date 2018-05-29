from django.shortcuts import render, HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '|| '.join([q.question_text for q in latest_question_list])

    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("Estas viendo la pregunta %s." % question_id)


def results(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s." % question_id)