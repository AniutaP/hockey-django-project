# Generated by Django 5.0.2 on 2024-03-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_skill_alter_user_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='сontact_information',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
