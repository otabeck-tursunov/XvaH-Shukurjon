from django.db import models


class CorrectWord(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class IncorrectWord(models.Model):
    word = models.CharField(max_length=50)
    correct_word = models.ForeignKey(CorrectWord, on_delete=models.CASCADE)

    def __str__(self):
        return self.word

# halol -> xalol
# xohish -> xoxish, hohish, hoxish