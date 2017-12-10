from django.contrib import admin
from .models import Theme, Article, Question, Answer, UserResult, UserAnswer


admin.site.register(Theme)
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserResult)
admin.site.register(UserAnswer)
