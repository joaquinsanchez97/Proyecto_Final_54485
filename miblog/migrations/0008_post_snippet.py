# Generated by Django 4.2.2 on 2023-07-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Vista previa del post', max_length=255, verbose_name='Subtítulo'),
        ),
    ]
