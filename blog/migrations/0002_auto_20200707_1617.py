# Generated by Django 2.2.10 on 2020-07-07 10:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_comments', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2020, 7, 7, 10, 47, 52, 359527, tzinfo=utc))),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_on',
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 10, 47, 52, 359527, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
