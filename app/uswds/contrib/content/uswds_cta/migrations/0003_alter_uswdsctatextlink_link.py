# Generated by Django 3.2.4 on 2022-11-30 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uswds_cta', '0002_auto_20221130_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uswdsctatextlink',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uswds_cta_link', to='uswds_cta.uswdsctatext'),
        ),
    ]