# Generated by Django 5.0.4 on 2024-05-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("VanPhongPham", "0003_giohang"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sanpham",
            name="DonGia",
            field=models.IntegerField(),
        ),
    ]
