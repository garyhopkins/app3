# Generated by Django 4.0.5 on 2022-08-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='positive_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
