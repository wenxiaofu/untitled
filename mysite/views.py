from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice
from django.urls import reverse
#from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('mysite/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'mysite/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
     """
    return render(request,'mysite/detail.html',{'question':question})

   # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'mysite/detail.html',{
            'question':question,
            'error_message':"you didnot select a chioce"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('mysite:results', args=(question.id,)))
    #return HttpResponse("You're voting on question %s." % question_id)
def results(request,question_id):
    question= get_object_or_404(Question,pk=question_id)
    return render(request,'mysite/results.html',{'question':question})