# Generated by Django 5.1 on 2024-09-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='', max_length=20)),
                ('Lastname', models.CharField(default='', max_length=20)),
                ('Email', models.CharField(default='', max_length=20)),
                ('Password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
