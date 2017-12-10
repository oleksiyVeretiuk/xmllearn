from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from .models import Theme, UserAnswer, UserResult


class ThemeListView(View):

    def get(self, request):
        themes = Theme.objects.all()
        return render(request, 'education/list.html', {'themes': themes})


class ArticleListView(View):

    def get(self, request, pk):
        theme = get_object_or_404(Theme, pk=pk)
        return render(request, 'education/article-list.html', {'articles': theme.articles.all(), 'theme': theme})


class ThemeTestView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        theme = get_object_or_404(Theme, pk=pk)
        return render(request, 'education/test-form.html', {'theme': theme})

    @method_decorator(login_required)
    def post(self, request, pk):
        theme = get_object_or_404(Theme, pk=pk)
        questions_name = [('question-' + str(question.id), question) for question in theme.questions.all()]
        user_result = UserResult.objects.create(user=request.user, theme=theme)
        for name, question in questions_name:
            UserAnswer.objects.create(
                result=user_result,
                question=question,
                answer=question.answers.get(pk=request.POST[name])
                )
        return redirect(reverse('result_list'))


class UserResultView(View):

    @method_decorator(login_required)
    def get(self, request):
        user_results = request.user.results.all()
        return render(request, 'education/results.html', {'results': user_results})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('result_list'))
            else:
                return render(request, 'education/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'education/login.html', {'error_message': 'Invalid login'})
    return render(request, 'education/login.html')
