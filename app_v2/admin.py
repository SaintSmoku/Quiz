from django.contrib import admin
from .models import Team, User, Score, Quiz, SubQuiz, Leader, Point

admin.site.register(Team)
admin.site.register(User)
admin.site.register(Score)
admin.site.register(Quiz)
admin.site.register(SubQuiz)
admin.site.register(Leader)
admin.site.register(Point)