# Generated by Django 2.2.17 on 2020-11-24 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_questions', '0003_move_data'),
    ]

    operations = [
         migrations.RunSQL("""
            DELETE FROM a4_candy_questions_question;
        """),
        migrations.RunSQL("""
            DELETE FROM a4_candy_questions_livestream;
        """)
    ]
