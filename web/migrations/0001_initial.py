# Generated by Django 4.2.4 on 2023-09-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckUpImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
                ('content_1', models.TextField()),
                ('content_2', models.TextField()),
                ('content_3', models.TextField()),
                ('content_4', models.TextField()),
                ('content_5', models.TextField()),
                ('featur_1', models.CharField(max_length=100)),
                ('featur_2', models.CharField(max_length=100)),
                ('featur_3', models.CharField(max_length=100)),
                ('project_url', models.CharField(max_length=500)),
                ('is_websites', models.BooleanField(default=False)),
                ('is_web_apps', models.BooleanField(default=False)),
                ('is_ecommerce', models.BooleanField(default=False)),
                ('is_updates', models.BooleanField(default=False)),
            ],
        ),
    ]
