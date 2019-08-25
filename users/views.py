from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from users.models import LessonQuestion, LessonTest, LessonAnswer 
from users.decorators import role_required
from users.functions import get_current_role
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("users:dashboard"))
		else:
			return HttpResponseRedirect(reverse('users:user_login'))
	else:
		context = {

		}
		return render(request,'users/login.html', context)


def check_login(request):
	if request.user.is_superuser:
		return HttpResponseRedirect(reverse('users:admin_dash'))
	else:
		return HttpResponseRedirect(reverse('users:dashboard'))


@login_required
def quiz_logout(request):
	current_role = get_current_role(request)
	logout(request)
	if current_role == "superadmin":
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		return HttpResponseRedirect(reverse('users:user_login'))


@login_required(login_url='/users/login/')
@role_required(['member'])
def dashboard(request):
	questions = LessonQuestion.objects.all()
	if request.method == 'POST':
		all_questions_attended = True
		mark = 0

		for question in questions:
			answer_pk = request.POST.get('answer_' + str(question.pk))

			if not answer_pk:
				all_questions_attended = False

			if LessonAnswer.objects.filter(pk=answer_pk,question=question.pk).exists():

				answer = get_object_or_404(LessonAnswer.objects.filter(pk=answer_pk,question=question.pk))
				
				if answer.is_right_answer:
					mark = mark + 1

		if all_questions_attended:
			test = LessonTest(
				user = request.user,
				test_mark = mark
			).save()

			context = {
				"title" : "Result",
				'mark' : mark
			}

			return render(request,'users/result.html', context)
		else:
			context = {
				"title" : "Dashboard",
				'questions': questions
			}
			return render(request,'users/dashboard.html', context)

	else:
		context = {
			"title" : "Dashboard",
			'questions': questions
		}
		return render(request,'users/dashboard.html', context)


@login_required
@role_required(['superadmin'])
def admin_dash(request):
	user_tests = LessonTest.objects.all()
	is_superuser = True
	context = {
		"title" : "Result",
		'is_superuser' : is_superuser,
		'user_tests' : user_tests,
	}

	return render(request,'users/result.html', context)


def user_register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		password =''
		error = False
		user = None
		message = ''

		if password1 == password2:
			password = password1
			error = False
		else:
			error = True

		if not error:
			user = User.objects.create_user(
				username=username,
				email=email,
				password=password
			)

			user = authenticate(username=username, password=password)
			
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse("users:dashboard"))
		else: 
			context = {
				message: 'both password are not same',
			}
			return render(request,'users/registration.html', context)
	else:
		context = {
		}
		return render(request,'users/registration.html', context)