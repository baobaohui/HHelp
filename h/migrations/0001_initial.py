# Generated by Django 3.0.3 on 2020-02-16 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id，自增')),
                ('email', models.CharField(max_length=30, unique=True, verbose_name='用户账号，唯一')),
                ('password', models.CharField(max_length=20, verbose_name='账号密码')),
                ('isDoctor', models.IntegerField(null=True, verbose_name='是否是医生，0：是，1：否')),
                ('lastlogin', models.DateField(default=django.utils.timezone.now, verbose_name='最后登录时间')),
                ('token', models.CharField(max_length=40, unique=True, verbose_name='token,唯一')),
                ('vercode', models.CharField(max_length=6, verbose_name='验证码')),
            ],
        ),
    ]