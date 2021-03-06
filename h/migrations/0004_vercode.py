# Generated by Django 3.0.3 on 2020-02-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h', '0003_ban_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id，自增，计数作用')),
                ('email', models.CharField(max_length=30, unique=True, verbose_name='发送验证码的邮箱，唯一')),
                ('vercode', models.CharField(max_length=6, verbose_name='随机的验证码')),
            ],
        ),
    ]
