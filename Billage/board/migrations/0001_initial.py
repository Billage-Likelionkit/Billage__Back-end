# Generated by Django 3.2.14 on 2022-07-09 06:52

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
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='글 제목')),
                ('description', models.TextField(verbose_name='글 내용')),
                ('image', models.CharField(max_length=300)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='글 작성 시간')),
                ('writer', models.ForeignKey(db_column='writer', on_delete=django.db.models.deletion.CASCADE, related_name='board', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='BoardInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20, verbose_name='분류')),
                ('price', models.CharField(max_length=20, verbose_name='가격')),
                ('process_status', models.CharField(max_length=20, verbose_name='상태')),
                ('board_id', models.ForeignKey(db_column='board_id', on_delete=django.db.models.deletion.CASCADE, related_name='boardinfo', to='board.board')),
            ],
        ),
    ]
