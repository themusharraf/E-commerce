# Generated by Django 4.2 on 2023-07-24 10:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("productsapp", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("-id",)},
        ),
    ]