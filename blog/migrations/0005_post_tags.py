# Generated by Django 5.2.3 on 2025-07-01 04:57

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_delete_comments_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
