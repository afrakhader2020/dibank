# Generated by Django 4.2.3 on 2023-09-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0002_register_remove_userprofile_materials_provided_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('cpwd', models.CharField(max_length=20)),
            ],
        ),
    ]