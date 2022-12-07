# Generated by Django 3.2 on 2022-12-02 08:22

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='USWDSHeader',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='uswds_header_uswdsheader', serialize=False, to='cms.cmsplugin')),
                ('name', models.CharField(blank=True, help_text='The name of the site or agency.', max_length=60, null=True)),
                ('show_search', models.BooleanField(default=True, help_text='Show the search bar in navigation.')),
                ('search_placeholder', models.CharField(default='Search...', help_text='This text is included in the search input box as a placeholder. Max-length 60 characters.', max_length=60)),
                ('extended_header', models.BooleanField(default=False, help_text='An extended header allows for the inclusion of more sections in a horizontal navigation.')),
                ('header_type', models.CharField(choices=[('default', 'Default dropdown'), ('mega_menu', 'Mega Menu')], default='default', max_length=60)),
                ('icon', filer.fields.image.FilerImageField(blank=True, help_text='Make sure the logo is sized appropriately for the space.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': 'USWDS Header',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='USWDSActionLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=255)),
                ('is_external', models.BooleanField(default=False, null=True)),
                ('external_url', models.URLField(blank=True, max_length=255, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('internal', cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.page')),
                ('uswds_action_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uswds_action_link', to='uswds_header.uswdsheader')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]