# Generated by Django 4.1.7 on 2023-04-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_delete_userprofile'),
        ('users', '0004_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='products',
            field=models.ManyToManyField(to='mainapp.product'),
        ),
    ]
