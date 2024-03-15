from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging

from .forms import ChooseGameForm

logger = logging.getLogger(__name__)


def coin(request, amount_throws):
    results = [choice(('Head', 'Tails')) for i in range(amount_throws)]
    context = {
        'title': 'Монетка',
        'result': results
    }
    return render(request, 'myapp2/result.html', context)


def dice(request, amount_throws):
    results = [randint(1,6) for i in range(amount_throws)]

    context = {'title': 'Игральный кубик', 'result': results}
    return render(request, 'myapp2/result.html', context)


def hundred(request, amount_throws):
    results = [randint(1,100) for i in range(amount_throws)]
    context = {'title': 'Сотня', 'result': results}
    return render(request, 'myapp2/result.html', context)


def result(request):
    func = {"C": coin, "D": dice, "H": hundred}
    if request.method == 'POST':
        form = ChooseGameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            return func[game](request, count)
    else:
        form = ChooseGameForm()
    return render(request, 'myapp2/home.html', {'form': form})
