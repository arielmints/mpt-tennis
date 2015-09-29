# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mpt', '0002_auto_20150925_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='contact_text',
            field=ckeditor.fields.RichTextField(default=None),
        ),
    ]
