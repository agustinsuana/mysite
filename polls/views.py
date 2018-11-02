from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404

def index(request):
    #last_questions_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template("polls/index.html")
    #context = {
    #    'last_question_list' : last_questions_list,
    #}
    #output = ', '.join([q.question_text for q in last_questions_list])
    #return HttpResponse(template.render(context, request))
    last_questions_list = Question.objects.order_by("-pub_date")[:5]
    context = {"last_questions_list" : last_questions_list}
    return render(request, 'polls/index.html', context)


def edit(request):
    return HttpResponse("Hola mundo, esta es el edit de Polls.")

def delete(request):
    return HttpResponse("Hola mundo, esta es el delete de Polls.")

#def detail(request, question_id):
#    return HttpResponse("Estas viendo el detalle de  %s." % question_id)

#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk = question_id)
#    except Question.DoesNotExist:
#        raise Http404("La pagina no existe")

#    return render(request, 'polls/detail.html', {"question" : question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question' : question})


def results(request, question_id):
    response = "Estas buscando los resultados de %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Tu has votado por %s" % question_id)
