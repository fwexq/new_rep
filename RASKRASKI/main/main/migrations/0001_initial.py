# Generated by Django 4.0.1 on 2022-03-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('opisanie', models.CharField(max_length=50, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]