# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from django.test import TestCase

from ispmail_auth.models import User


@pytest.mark.django_db
def test_create_superuser():
    User.objects.create_superuser('test@example.org', 'secret')
    assert User.objects.count() == 1
    superuser = User.objects.first()
    assert superuser.is_active
    assert superuser.is_staff
    assert superuser.is_superuser
