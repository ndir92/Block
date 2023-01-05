# Generated by Django 4.0.3 on 2022-12-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/images/')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
