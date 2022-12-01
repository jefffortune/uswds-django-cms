# Generated by Django 3.2.4 on 2022-11-30 09:24

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='USWDSHero',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='uswds_hero_uswdshero', serialize=False, to='cms.cmsplugin')),
                ('title_prefix', models.CharField(blank=True, help_text='Max length is 15 characters.', max_length=15, null=True)),
                ('title', models.CharField(help_text='Max length is 60 characters.', max_length=60)),
                ('support', models.TextField(blank=True, help_text='Support the callout with some short explanatory text.', max_length=255, null=True)),
                ('align_support', models.CharField(choices=[('support-left', 'Left'), ('support-right', 'Right')], default='support-left', max_length=60)),
                ('background_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uswds_hero_background_image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': 'USWDS Hero',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='USWDSHeroLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=255)),
                ('is_external', models.BooleanField(default=False, null=True)),
                ('external_url', models.URLField(blank=True, max_length=255, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('internal', cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.page')),
                ('uswds_hero_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uswds_hero_link', to='uswds_hero.uswdshero')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]