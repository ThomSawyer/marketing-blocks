# Generated by Django 2.2.7 on 2019-12-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketing_blocks", "0005_marketingblock_content_sendgrid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marketingblock",
            name="content_mailchimp",
            field=models.TextField(
                blank=True, default="", verbose_name="Contenu pour Mailchimp"
            ),
        ),
        migrations.AlterField(
            model_name="marketingblock",
            name="content_sendgrid",
            field=models.TextField(
                blank=True, default="", verbose_name="Contenu pour SendGrid"
            ),
        ),
    ]
