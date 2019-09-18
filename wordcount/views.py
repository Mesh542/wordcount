from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    if request.method == 'GET' and 'text' in request.GET:
        text = request.GET['text']
        words = text.split()
        count = len(words)
        word_dictionary = {}
        for word in words:
            if word.lower() in word_dictionary:
                word_dictionary[word.lower()] += 1
            else:
                word_dictionary[word.lower()] = 1
    else:
        count = None
        text = None

    return render(request, 'index.html', {
        'count': count,
        'text': text,
    })


def contact_us(request):
    return render(request, 'contact.html')
