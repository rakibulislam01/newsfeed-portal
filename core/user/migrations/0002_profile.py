# Generated by Django 3.1.7 on 2021-04-07 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_tag', models.CharField(default=None, max_length=255, null=True)),
                ('source_tag', models.CharField(default=None, max_length=255, null=True)),
                ('keyword_tag', models.CharField(default=None, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]