# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': last_question_list
    }
    # render是loader函数的简化
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # context直接简化到render函数里面了
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 没有选择任何答案，返回问卷页
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "您还没选择任何选项"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 为了防止用户在提交数据结束后，单击浏览器后退按钮重新提交数据，必须使用HttpResponseRedirect方法进行页面跳转
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
