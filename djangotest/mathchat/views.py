# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from .models import ChatRoom, Message

def index (request):
    """ returns the index page of mathchat

    Currently replies a helloworld string

    Args:
        request (HttpRequest): the request to which this function is responding

    Returns:
        HttpResponse: an object containing the index pge of this site

    """
    return HttpResponse("Hello, World - This is the mathchat index.")

def room (request, room_name):
    template = loader.get_template('mathchat/room.html')
    messages = ChatRoom.objects.get(name=room_name).message_set.all()
    context = {
        'room_title': room_name,
        'message_list': messages
    }

    return HttpResponse(template.render(context, request))
