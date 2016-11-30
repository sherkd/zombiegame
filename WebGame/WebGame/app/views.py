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

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def shop(request):
    """Renders the shop page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/shop.html',
        {
            'title':'Shop',
            'message':'This page is a blank template.',
            'year':datetime.now().year,
        }
    )

def bank(request):
    """Renders the bank page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/bank.html',
        {
            'title':'Bank',
            'message':'This page is a blank template.',
            'year':datetime.now().year,
        }
    )

def recovery(request):
    """Renders the recovery page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/recovery.html',
        {
            'title':'Health Recovery',
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
            'message':'This page is a blank template.',
            'year':datetime.now().year,
        }
    )
