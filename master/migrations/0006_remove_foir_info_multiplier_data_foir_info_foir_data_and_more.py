# Generated by Django 4.1.2 on 2022-12-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "master",
            "0005_rename_multipier_info_product_and_policy_master_multiplier_info_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="foir_info", name="multiplier_data",),
        migrations.AddField(
            model_name="foir_info",
            name="foir_data",
            field=models.ManyToManyField(to="master.foir_data"),
        ),
        migrations.AlterField(
            model_name="foir_data",
            name="tenure_foirs",
            field=models.ManyToManyField(to="master.pertenure_foir_data"),
        ),
    ]
