# Generated by Django 2.2.16 on 2020-12-03 00:49

from django.db import migrations


class Migration(migrations.Migration):

    # This is an oddly long list of dependencies, but I'm not going to argue with it
    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtail_footnotes', '0001_initial'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailinventory', '0001_initial'),
        ('wagtailpages', '0023_buyersguidepage_cutoff_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PeoplePage',
        ),
    ]
