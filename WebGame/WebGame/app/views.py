"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def survival(request):
    """Renders the survival page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/survival.html',
        {
            'title':'Survival',
            'message':'This page is a blank template.',
            'year':datetime.now().year,
        }
    )

def tournament(request):
    """Renders the tournament page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tournament.html',
        {
            'title':'Tournament',
            'message':'This page is a blank template.',
            'year':datetime.now().year,
        }
    )

def groupfight(request):
    """Renders the groupfight page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/groupfight.html',
        {
            'title':'Group fight',
            'message':'This page is a blank template.',
            'year':datetime.now().year,
        }
    )

def fight(request):
    """Renders the fight page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fight.html',
        {
            'title':'1v1 Fight',
            'message':'This page is a blank template.',
            'year':datetime.now().year,
        }
    )

def quest(request):
    """Renders the quest page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/quest.html',
        {
            'title':'Quest',
            'message':'Start a quest here.',
            'year':datetime.now().year,
        }
    )
