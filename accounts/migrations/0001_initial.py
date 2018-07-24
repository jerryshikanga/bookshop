# Generated by Django 2.0.7 on 2018-07-24 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.IntegerField(verbose_name='Telephone Number')),
                ('address', models.TextField(verbose_name='Physical Address')),
                ('picture', models.ImageField(default='profile_default.png', upload_to='accounts/profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Account')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'permissions': (('custom_can_add_user', 'Custom Can add User'), ('custom_can_edit_user', 'Custom Can edit User'), ('custom_can_delete_user', 'Custom Can delete User')),
            },
        ),
    ]
