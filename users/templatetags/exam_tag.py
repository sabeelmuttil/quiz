from django.template import Library
from django.contrib.auth.models import User
register = Library()
from django.template.defaultfilters import stringfilter
from users.models import LessonTest, LessonAnswer, LessonQuestion

@register.filter
def get_answers(question):
	answers =  LessonAnswer.objects.filter(question=question)
	return answers


@register.filter
def get_questions(lesson):
	questions =  LessonQuestion.objects.filter(lesson=lesson)
	return questions
