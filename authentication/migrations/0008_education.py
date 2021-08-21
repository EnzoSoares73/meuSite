# Generated by Django 3.2.6 on 2021-08-14 02:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0007_alter_experience_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('experience_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='authentication.experience')),
            ],
            bases=('authentication.experience',),
        ),
    ]
