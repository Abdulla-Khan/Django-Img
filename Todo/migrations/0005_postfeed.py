# Generated by Django 4.0.4 on 2022-06-08 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0004_rename_rent_todo_collaborations_remove_todo_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedImage', models.ImageField(upload_to='feed')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Todo.todo')),
            ],
        ),
    ]
