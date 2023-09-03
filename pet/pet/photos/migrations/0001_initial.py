# Generated by Django 4.2.2 on 2023-09-02 20:43

import core.model_mixins
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pet.photos.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='pet_photos/', validators=[pet.photos.validators.validate_file_less_than_5mb])),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('publication_date', models.DateTimeField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, to='pets.pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(core.model_mixins.StrFromFieldsMixin, models.Model),
        ),
    ]