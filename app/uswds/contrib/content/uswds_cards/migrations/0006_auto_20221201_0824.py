# Generated by Django 3.2 on 2022-12-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uswds_cards', '0005_alter_uswdscardgrid_columns'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uswdscardgrid',
            options={'verbose_name': 'Card grid'},
        ),
        migrations.AlterField(
            model_name='uswdscardgrid',
            name='columns',
            field=models.CharField(choices=[('tablet:grid-col-6', 'Two Columns'), ('tablet:grid-col-4', 'Three Columns'), ('tablet:grid-col-3', 'Four Columns')], default='tablet:grid-col-3', max_length=60),
        ),
    ]