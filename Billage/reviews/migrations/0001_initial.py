# Generated by Django 4.0.6 on 2022-07-09 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='글 작성 시간')),
                ('star', models.IntegerField()),
                ('content', models.TextField()),
                ('receive_id', models.ForeignKey(db_column='recieve_id', on_delete=django.db.models.deletion.CASCADE, related_name='recieve_id', to=settings.AUTH_USER_MODEL, verbose_name='수신자')),
                ('send_id', models.ForeignKey(db_column='send_id', on_delete=django.db.models.deletion.CASCADE, related_name='send_id', to=settings.AUTH_USER_MODEL, verbose_name='송신자')),
            ],
        ),
    ]
