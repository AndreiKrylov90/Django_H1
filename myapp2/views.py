from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import CoinFlip

logger = logging.getLogger(__name__)


def coin(request, amount_flips):
    result = choice(('Head', 'Tails'))
    logger.info(result)
    CoinFlip(side=result).save()
    last_results = CoinFlip.get_last_flips(amount_flips)
    context = {
        'current_flip': result,
        'last_results': last_results
    }
    return render(request, 'myapp2/coin.html', context)
    # return HttpResponse(result)


def dice(request, amount_throws):
    results = [randint(1,6) for i in range(amount_throws)]

    context = {'title': 'Игральный кубик', 'result': results}
    return render(request, 'myapp2/result.html', context)


def hundred(request):
    count = randint(1, 100)
    logger.debug(count)
    return HttpResponse(f"{count}")

