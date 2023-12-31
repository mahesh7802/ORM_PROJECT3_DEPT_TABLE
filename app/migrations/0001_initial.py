# Generated by Django 4.2.2 on 2023-06-21 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('did', models.IntegerField()),
                ('dlocation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=20)),
                ('enumber', models.IntegerField()),
                ('elocation', models.CharField(max_length=20)),
                ('dname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
