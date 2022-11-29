# Generated by Django 3.2 on 2022-11-26 17:48

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteFooterRibbonLinks',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='uswds_footer_ribbon_sitefooterribbonlinks', serialize=False, to='cms.cmsplugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SiteFooterRibbonLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=255)),
                ('is_external', models.BooleanField(default=False, null=True)),
                ('external_url', models.URLField(blank=True, max_length=255, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('footer_ribbon_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footer_ribbon_link', to='uswds_footer_ribbon.sitefooterribbonlinks')),
                ('internal', cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.page')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
    ]