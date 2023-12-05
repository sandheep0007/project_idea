# Generated by Django 4.2.7 on 2023-11-09 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pro_app', '0004_remove_topic_technologyname_topic_technologyname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='Technologyname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pro_app.technology'),
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isactive', models.BooleanField(default=True, verbose_name='Active')),
                ('project_type', models.CharField(max_length=200)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-isactive'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='topic',
            name='project_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pro_app.projecttype'),
        ),
    ]
