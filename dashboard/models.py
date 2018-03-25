from django.db import models

# Create your models here.


class DashboardData(models.Model):
    end_year = models.CharField(max_length=10)
    intensity = models.CharField(max_length=10)
    sector = models.CharField(max_length=20)
    topic = models.CharField(max_length=10)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=30)
    start_year = models.CharField(max_length=10)
    impact = models.CharField(max_length=10)
    added = models.CharField(max_length=40)
    published = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    relevance = models.CharField(max_length=10)
    pestle = models.CharField(max_length=30)
    source = models.CharField(max_length=20)
    title = models.TextField()
    likelihood = models.CharField(max_length=10)

    def __str__(self):
        return self.title
