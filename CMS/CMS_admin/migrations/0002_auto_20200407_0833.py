# Generated by Django 3.0.3 on 2020-04-07 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CMS_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('h1', models.BooleanField(default=False)),
                ('h2', models.BooleanField(default=False)),
                ('h3', models.BooleanField(default=False)),
                ('h4', models.BooleanField(default=False)),
                ('h5', models.BooleanField(default=False)),
                ('h6', models.BooleanField(default=False)),
                ('attendence_status', models.CharField(choices=[('A', 'Absent'), ('F', 'Full Day'), ('H', 'Half Day')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS_admin.Class')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS_admin.Class')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfileStatus',
        ),
        migrations.AddField(
            model_name='attendence',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS_admin.Student'),
        ),
        migrations.AddField(
            model_name='attendence',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS_admin.Teacher'),
        ),
    ]