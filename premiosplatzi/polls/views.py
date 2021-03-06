from multiprocessing import context
from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.all() # se pueden traer también con filter, etc.
#     return render(request, "polls/index.html", {
#         "latest_question_list" : latest_question_list
#     })

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {
#         "question" : question
#     })


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html",{
#         "question": question
#     })

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list" # Ahora esta varaible context_object_name va a guardar lo que retorne la función queryset

    def get_queryset(self):
        """ Return the last published questions."""
        return Question.objects.order_by("-pub_date")[:5] # - indica en orden DESC

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id): # function based views
    question = get_object_or_404(Question, pk=question_id) # Question.objects.get(pk=1) # Handle error for selected question
    
    try: # handle error for selected choice
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) # Rescata la opción que está en "value" del HTML llamado "choice" que es el id del objeto de tipo 'Choice'.
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect( reverse("polls:results", args=(question.id, ) ) )

