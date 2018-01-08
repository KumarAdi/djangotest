# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ChatRoom (models.Model):
    name = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class Message (models.Model):
    body = models.CharField(max_length = 200);
    room = models.ForeignKey(ChatRoom, on_delete = models.CASCADE)

    def __str__(self):
        return self.body
