from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Question, Answer, Like
from .forms import SignUpForm, LoginForm, QuestionForm, AnswerForm

# Home Page - List of all questions
def home(request):
    questions = Question.objects.all().order_by('-created_date')
    return render(request, 'home.html', {'questions': questions})

# User Registration
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username,password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# User Logout
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

# Post a Question
@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, "Your question has been posted!")
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'post_questions.html', {'form': form})

# Question Detail and Answer Form
@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.ques = question
            answer.save()
            messages.success(request, "Your answer has been posted!")
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'question_details.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

# Like an answer
@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    existing_like = Like.objects.filter(answer=answer, user=request.user)
    if not existing_like.exists():
        Like.objects.create(answer=answer, user=request.user)
        messages.success(request, "You liked an answer!")
    else:
        messages.info(request, "You already liked this answer.")
    return redirect('question_detail', question_id=answer.ques.id)
