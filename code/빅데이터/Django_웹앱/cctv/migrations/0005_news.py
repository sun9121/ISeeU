# Generated by Django 3.2.3 on 2021-05-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0004_auto_20210526_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News_title', models.CharField(max_length=200)),
                ('News_content', models.CharField(max_length=200)),
                ('News_href', models.CharField(max_length=200)),
                ('News_writer', models.CharField(max_length=200)),
                ('News_write_time', models.DateTimeField()),
                ('News_area', models.CharField(max_length=10)),
            ],
        ),
    ]
