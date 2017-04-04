# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sie_Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('UTI_LOGIN', models.CharField(max_length=50)),
                ('UTI_MDP', models.CharField(max_length=50)),
                ('UTI_NOM', models.CharField(max_length=50)),
                ('UTI_PRENOM', models.CharField(max_length=50)),
                ('UTI_CIVILITE', models.CharField(max_length=1)),
                ('UTI_EMAIL', models.CharField(max_length=50)),
                ('UTI_SUPPRIME', models.BooleanField()),
            ],
        ),
    ]
