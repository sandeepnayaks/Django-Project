# Generated by Django 2.0.4 on 2018-05-30 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20180530_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='past_records', to='student.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='attendance',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Attendance'),
        ),
        migrations.AlterField(
            model_name='student',
            name='progress',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='student.Progress'),
        ),
    ]