# Generated by Django 2.0.6 on 2018-06-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_relation_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='relation_type',
            field=models.CharField(choices=[('b', 'Block'), ('f', 'Follow')], max_length=1),
        ),
    ]