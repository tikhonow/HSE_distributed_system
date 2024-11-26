from django.db import models

class Number(models.Model):
    value = models.PositiveIntegerField(unique=True)
    processed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('value', 'processed_at')

    def __str__(self):
        return str(self.value)
