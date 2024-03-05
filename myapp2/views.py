from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging

logger = logging.getLogger(__name__)


def coin(request):
    side = choice(["Орел", "Решка"])
    logger.debug(side)
    return HttpResponse(side)


def dice(request):
    count = randint(1, 6)
    logger.debug(count)
    return HttpResponse(f"{count}")


def hundred(request):
    count = randint(1, 100)
    logger.debug(count)
    return HttpResponse(f"{count}")

