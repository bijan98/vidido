from django.contrib import admin
from polls.models import Choice,AnswerLog,Question
# Register your models here.


admin.site.register(Choice)
admin.site.register(AnswerLog)
admin.site.register(Question)