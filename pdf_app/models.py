from django.db import models

class ExtractedData(models.Model):
    question_no = models.IntegerField()
    sub_question = models.IntegerField()
    marks = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()
    
    class meta:
        db_name = 'extracted_data'
