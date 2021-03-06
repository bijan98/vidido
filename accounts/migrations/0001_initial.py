# Generated by Django 2.0.7 on 2018-07-10 08:14

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_photo', models.ImageField(blank=True, default='../static/facebook-avatar.jpg', null=True, upload_to='vidido/profile-phto', verbose_name='photo')),
                ('birthday', models.DateField(null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other'), ('alien', 'alien')], max_length=10)),
                ('friends', models.ManyToManyField(db_index=True, related_name='_profile_friends_+', to='accounts.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
