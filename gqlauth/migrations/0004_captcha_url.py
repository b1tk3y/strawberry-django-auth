# Generated by Django 4.0.6 on 2022-08-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gqlauth", "0003_remove_captcha_id_alter_captcha_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="captcha",
            name="url",
            field=models.ImageField(
                default=None,
                editable=False,
                help_text="url for the captcha image",
                upload_to="captcha/%Y/%m/%d/",
            ),
        ),
    ]