from django.db import models

class TestGenerator(models.Model):
    code = models.TextField()
    generated_test = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
