# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from datetime import datetime
from uuid import uuid4

from django.db import models


# Create your models here.

class User(models.Model):
    GENDERS = (("MALE", "MALE"),
               ("FEMALE", "FEMALE"),
               ("OTHER", "OTHER"))

    username = models.CharField(max_length=254, primary_key=True)
    password = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254, null=True)
    email = models.CharField(max_length=254)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=128, choices=GENDERS, default=None)
    profile_pic = models.CharField(max_length=512, null=True)
    created_on = models.DateTimeField(default=datetime.now())


class LoginEntry(models.Model):
    user = models.ForeignKey(User)
    login_time = models.DateTimeField(default=datetime.now())
    client_id = models.CharField(max_length=256)
    auth_token = models.CharField(max_length=512, default=str(uuid.uuid4()))
    is_active = models.BooleanField(default=True)