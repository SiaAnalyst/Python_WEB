from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=250, null=False, unique=True)
    born_date = models.DateField(null=False)
    born_location = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField(null=False)
    tags = models.ManyToManyField(Tag, related_name='quotes')

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="quotes")

    def __str__(self):
        return f"{self.author.fullname}: '{self.text[:30]}...'"
