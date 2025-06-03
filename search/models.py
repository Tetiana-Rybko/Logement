from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SearchQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_queries')
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} — {self.query}"
