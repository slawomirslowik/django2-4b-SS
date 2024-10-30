from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question
import logging

logger = logging.getLogger(__name__)

def index(request):
    context = { "latest_question_list": Question.objects.order_by("-pub_date")[:5]}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        logger.info("Found question: " + str(question_id))
    except Question.DoesNotExist:
        logger.error("Question does not exist. ID: " + str(question_id))
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)