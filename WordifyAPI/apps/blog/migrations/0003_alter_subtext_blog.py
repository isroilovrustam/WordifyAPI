# Generated by Django 4.1.7 on 2023-03-31 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_subpicture_blog_text_alter_subtext_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtext',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blog_subtext', to='blog.blog'),
        ),
    ]
