# Generated by Django 4.0.4 on 2022-05-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formcontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
    ]