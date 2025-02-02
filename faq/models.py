from django.db import models

class FAQ(models.Model):
    question_en = models.CharField(max_length=255)
    question_fr = models.CharField(max_length=255, blank=True, null=True)
    question_es = models.CharField(max_length=255, blank=True, null=True)
    answer_en = models.TextField()
    answer_fr = models.TextField(blank=True, null=True)
    answer_es = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_en

# Create your models here.
