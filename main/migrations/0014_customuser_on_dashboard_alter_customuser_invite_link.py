# Generated by Django 4.2.7 on 2024-02-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_plan_bonus_alter_customuser_invite_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='on_dashboard',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='invite_link',
            field=models.CharField(default='43bc3b7d0db442e0bfe2fd4946ba5335', max_length=50),
        ),
    ]