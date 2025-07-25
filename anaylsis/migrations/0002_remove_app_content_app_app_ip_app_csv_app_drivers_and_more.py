# Generated by Django 5.2.4 on 2025-07-23 22:34

import pgvector.django.indexes
import pgvector.django.vector
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anaylsis', '0001_for_pgvector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='content',
        ),
        migrations.AddField(
            model_name='app',
            name='app_ip',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='csv',
            field=models.FileField(null=True, upload_to='data'),
        ),
        migrations.AddField(
            model_name='app',
            name='drivers',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='painpoints',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='embeded_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.TextField(null=True)),
                ('content', models.TextField()),
                ('embedding', pgvector.django.vector.VectorField(blank=True, dimensions=384, null=True)),
            ],
            options={
                'indexes': [pgvector.django.indexes.HnswIndex(ef_construction=64, fields=['embedding'], m=16, name='clip__ll4_vectors_index', opclasses=['vector_cosine_ops'])],
            },
        ),
    ]
