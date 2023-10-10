# Generated by Django 4.2.5 on 2023-10-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название издательства.', max_length=50)),
                ('website', models.URLField(help_text='Сайт издательства.')),
                ('email', models.EmailField(help_text='Адрес электронной почты издателя.', max_length=254)),
            ],
        ),
    ]
