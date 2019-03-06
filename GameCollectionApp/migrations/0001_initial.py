# Generated by Django 2.0.6 on 2019-03-06 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=200)),
                ('Password1', models.CharField(default='', max_length=200)),
                ('Password2', models.CharField(default='', max_length=200)),
                ('dateAccountCreated', models.DateField(default=django.utils.timezone.now)),
                ('rank', models.CharField(default='Grunt', max_length=200)),
                ('foreignkeyToUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('developer', models.CharField(default='', max_length=200)),
                ('dateMade', models.DateField(default='')),
                ('ageLimit', models.IntegerField(default=0)),
                ('foreignKeyToCollector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GameCollectionApp.CollectorModel')),
            ],
        ),
    ]
