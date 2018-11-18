# Generated by Django 2.1.2 on 2018-11-18 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_book_md5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Resource')),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('base.resource',),
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='_keywords',
            new_name='keywords',
        ),
    ]
