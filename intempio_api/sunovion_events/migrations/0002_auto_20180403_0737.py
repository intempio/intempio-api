# Generated by Django 2.0.3 on 2018-04-03 07:37

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sunovion_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sunovionevent',
            name='accepted_at',
            field=model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, when={'accepted'}),
        ),
        migrations.AlterField(
            model_name='sunovionevent',
            name='reviewed_at',
            field=model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, when={'reviewed'}),
        ),
    ]
