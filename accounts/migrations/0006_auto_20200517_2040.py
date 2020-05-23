# Generated by Django 3.0.6 on 2020-05-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200516_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', '保留中'), ('Out for delivery', '配達中'), ('Deliverd', '配送済み')], max_length=200, null=True),
        ),
    ]