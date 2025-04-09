from django.contrib.auth.models import User
from django.db import models



class CommonFields(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500)
    updated_date = models.DateTimeField(null=True)

class Question(CommonFields):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Answer(CommonFields):
    ques = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    user = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,related_name='likes')



