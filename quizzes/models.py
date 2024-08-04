from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quiz(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')
    text=models.TextField()

    def __str__(self):
        return self.text
    
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="answers")
    text=models.CharField(max_length=100)
    is_correct=models.BooleanField()

    def __str__(self):
        return self.text
    
class UserQuizAttempt(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)
    completed_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.score}"

