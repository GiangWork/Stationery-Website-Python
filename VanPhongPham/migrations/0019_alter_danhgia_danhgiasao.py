# Generated by Django 5.0.4 on 2024-05-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("VanPhongPham", "0018_anhphu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="danhgia",
            name="DanhGiaSao",
            field=models.IntegerField(default=0),
        ),
    ]
