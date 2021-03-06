# Generated by Django 3.1.2 on 2021-11-14 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('YogaForm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yogaform',
            name='is_allowed_to_change_batch',
        ),
        migrations.RemoveField(
            model_name='yogaform',
            name='is_fees_paid',
        ),
        migrations.AlterField(
            model_name='yogaform',
            name='Batch',
            field=models.CharField(choices=[('Info', 'Choose a batch'), ('Morning-1', '6AM-7AM'), ('Morning-2', '7AM-8AM'), ('Morning-3', '8AM-9AM'), ('Evening-1', '5AM-6PM')], default='Info', max_length=100),
        ),
        migrations.AlterField(
            model_name='yogaform',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('is_allowed_to_change_batch', models.BooleanField(default=False)),
                ('is_fees_paid', models.BooleanField(default=False)),
                ('FormUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YogaForm.yogaform')),
            ],
        ),
    ]
