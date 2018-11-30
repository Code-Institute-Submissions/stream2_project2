# Generated by Django 2.0.8 on 2018-11-29 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opportunities', '0002_post_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='messages_sent', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='messages', to='opportunities.Post')),
                ('recipient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='messages_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]