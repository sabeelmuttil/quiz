from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from decimal import Decimal
import uuid


class LessonTest(models.Model):
	user = models.ForeignKey("auth.user",on_delete=models.CASCADE)
	test_mark = models.CharField(max_length=128,blank=True,null=True)

	class Meta:
		db_table = 'test'
		verbose_name = _('Test')
		verbose_name_plural = _('Tests')

	def __unicode__(self):
		return self.exam_type


class LessonQuestion(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	question = models.TextField()

	class Meta:
		db_table = 'question'
		verbose_name = _('Question')
		verbose_name_plural = _('Questions')

	def __str__(self):
		return str(self.question)


class LessonAnswer(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	question = models.ForeignKey("users.LessonQuestion",on_delete=models.CASCADE)
	answer = models.TextField()
	is_right_answer = models.BooleanField(default=False)
	is_deleted = models.BooleanField(default=False)

	class Meta:
		db_table = 'answer'
		verbose_name = _('Answer')
		verbose_name_plural = _('Answers')

	def __str__(self):
		return str(self.answer)
