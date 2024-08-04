from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Quiz,Answer,UserQuizAttempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

def quiz_list(request):
    quizzes= Quiz.objects.all()
    context={'quizzes':quizzes}
    return render(request,'quiz_list.html',context)

@login_required(login_url='login')
def quiz_detail(request,quiz_id):

    quiz=get_object_or_404(Quiz,id=quiz_id)
    has_completed = UserQuizAttempt.objects.filter(user=request.user, quiz=quiz).exists()

    if has_completed:
        attempt=UserQuizAttempt.objects.get(user=request.user,quiz_id=quiz_id)
        return render(request, 'quiz_results.html', {'attempt': attempt})
        # return redirect(reverse('quiz_list') + '?completed=true') 

    questions=quiz.questions.all()
    context={'quiz': quiz, 'questions': questions}
    return render(request, 'quiz_detail.html', context)

@login_required(login_url='login')
def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        score = 0
        for question in quiz.questions.all():
            answer_id = request.POST.get(f'question_{question.id}')
            if answer_id:
                answer = get_object_or_404(Answer, id=answer_id)
                if answer.is_correct:
                    score += 1

        UserQuizAttempt.objects.create(user=request.user, quiz=quiz, score=score)
        return redirect('quiz_results', quiz_id=quiz_id)

@login_required(login_url='login')
def quiz_results(request, quiz_id):
    attempt = UserQuizAttempt.objects.get(user=request.user, quiz_id=quiz_id)
    return render(request, 'quiz_results.html', {'attempt': attempt})