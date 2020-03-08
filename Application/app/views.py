"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.models import Order, Client

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

def about_us(request):
    return render(
        request,
        'app/about_us.html'
    )

def show_orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.exclude(author=request.user)
    else:
        orders = Order.objects.all()
    return render(
        request,
        'app/show_orders.html',
        {
            'orders': orders,
        }
    )

def manage_order(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.exclude(author=request.user)
    my_orders = Order.objects.filter(author=request.user)
    matchs = []
    if my_orders:
        for my_order in my_orders:
            for order in orders:
                my_range = TimeRange(my_order.start_date, my_order.end_date)
                other_range = TimeRange(order.start_date, order.end_date)
                if my_range.is_overlapped(other_range):
                    order.overlap_range = my_range.get_overlapped_range(other_range)
                    matchs.append(order)
    return render(
        request,
        'app/manage_order.html',
        {
            'my_orders': my_orders,
            'matchs': matchs
        }
    )

def create_order(request):
    order = Order.objects.create(
        location = request.POST['location'],
        author = request.user,
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        description = request.POST['description'],
        gender_preferences = request.POST['gender_preferences'],
        room_url = request.POST['room_url']
    )
    return redirect('manage_order')

def add_profile_info(request):
    try:
        client = Client.objects.get(user=request.user)
        client.gender = request.POST['gender']
        client.save()
    except Client.DoesNotExist:
        Client.objects.create(
            user = request.user,
            gender = request.POST['gender']
        )

    return redirect('manage_order')

def cancel_order(request, order_id):
    order = Order.objects.filter(id=order_id).delete()
    return redirect('manage_order')

class TimeRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = self.end - self.start

    def is_overlapped(self, time_range):
        if max(self.start, time_range.start) < min(self.end, time_range.end):
            return True
        else:
            return False

    def get_overlapped_range(self, time_range):
        if not self.is_overlapped(time_range):
            return

        if time_range.start >= self.start:
            if self.end >= time_range.end:
                return TimeRange(time_range.start, time_range.end)
            else:
                return TimeRange(time_range.start, self.end)
        elif time_range.start < self.start:
            if time_range.end >= self.end:
                return TimeRange(self.start, self.end)
            else:
                return TimeRange(self.start, time_range.end)

    def __repr__(self):
        return '{0} ------> {1}'.format(*[time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(d))
                                          for d in [self.start, self.end]])

