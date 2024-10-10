from django.contrib import admin

from .models import Question
from .models import Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date"]
    list_filter = ["question_text", "pub_date"]
    ordering = ["pub_date"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
