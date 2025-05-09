from django.db import models

class Team(models.Model):
    temaname = models.CharField(max_length=255)

    def __str__(self):
        return self.temaname

class Leader(models.Model):
    leadername = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.leadername
    
class User(models.Model):
    username = models.CharField(max_length=255)
    leader = models.ForeignKey(Leader, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class Score(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE) 
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.score

class Quiz(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubQuiz(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    point = models.IntegerField(default=10)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    def __str__(self):
        return self.quiz.name+" "+str(self.point)

class Point(models.Model):
    leader = models.ForeignKey(Leader, on_delete=models.SET_NULL, null=True, blank=True)
    subquiz = models.ForeignKey(SubQuiz, on_delete=models.SET_NULL, null=True, blank=True, related_name="points")
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.leader.leadername + " - " + self.subquiz.question + " - " + str(self.point)





