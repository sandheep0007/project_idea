# Generated by Django 4.2.7 on 2023-11-08 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pro_app', '0002_technology'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isactive', models.BooleanField(default=True, verbose_name='Active')),
                ('topicname', models.CharField(max_length=150)),
                ('project_type', models.IntegerField(choices=[('1', 'mini'), ('2', 'main'), ('3', 'live_project')])),
                ('description', models.TextField()),
                ('Technologyname', models.ManyToManyField(to='pro_app.technology')),
                ('coursename', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pro_app.course')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-isactive'],
                'abstract': False,
            },
        ),
    ]
