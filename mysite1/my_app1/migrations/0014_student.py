# Generated by Django 4.0.4 on 2022-06-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app1', '0013_carddetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('sub_mark1', models.CharField(max_length=30)),
                ('sub_mark2', models.CharField(max_length=30)),
                ('sub_mark3', models.CharField(max_length=30)),
                ('Total', models.CharField(max_length=30)),
                ('avg', models.CharField(max_length=30)),
            ],
        ),
    ]
