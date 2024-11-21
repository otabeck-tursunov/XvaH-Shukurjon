from django.shortcuts import render
from .models import *

def index(request):
    soz = request.GET.get('soz')

    correct_word = None
    incorrect_words = None

    if soz is not None:
        corrects = CorrectWord.objects.filter(word=soz)
        if corrects.exists():
            correct_word = corrects.first()
            incorrect_words = IncorrectWord.objects.filter(correct_word=correct_word)
        else:
            incorrect_words = IncorrectWord.objects.filter(word=soz)
            if incorrect_words.exists():
                incorrect_word = incorrect_words.first()
                correct_word = incorrect_word.correct_word
                incorrect_words = IncorrectWord.objects.filter(correct_word=correct_word)
    context = {
        'correct_word': correct_word,
        'incorrect_words': incorrect_words,
    }
    return render(request, 'index.html', context)
