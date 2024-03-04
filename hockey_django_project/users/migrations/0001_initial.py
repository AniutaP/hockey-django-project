# Generated by Django 5.0.2 on 2024-03-04 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.skill')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.team')),
            ],
        ),
    ]
