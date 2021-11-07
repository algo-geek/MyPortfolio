# Generated by Django 3.2.5 on 2021-08-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_name_category_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=25)),
                ('icon_link', models.URLField()),
                ('s_des', models.CharField(max_length=100)),
            ],
        ),
    ]
