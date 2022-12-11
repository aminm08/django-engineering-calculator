from django.shortcuts import render, redirect
from .calculator import Calculator
from django.http import HttpRequest
from django.contrib import messages
from django.utils.translation import gettext as _


def index(request):
    result = ''
    if request.GET:
        statement = request.GET['statement']
        if not statement:
            return redirect('cal_index')

        cal = Calculator(statement)
        try:
            result = cal.calculate()
        except Exception:
            messages.error(request, _('error during calculate'))

    return render(request, 'calculator/index.html', {'result': result})
