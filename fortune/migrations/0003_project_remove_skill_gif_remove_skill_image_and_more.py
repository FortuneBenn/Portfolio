# Generated by Django 4.2.4 on 2023-09-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0002_education_skill_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/images/')),
                ('gif', models.FileField(blank=True, null=True, upload_to='projects/gifs/')),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='gif',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='image',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_percentage',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
