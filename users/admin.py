from django.contrib import admin
from users.models import LessonQuestion, LessonAnswer

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('pk','question')
admin.site.register(LessonQuestion, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
	list_display = ('pk','question','answer','is_right_answer','is_deleted')
admin.site.register(LessonAnswer, AnswerAdmin)