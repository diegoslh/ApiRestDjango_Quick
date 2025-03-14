# Generated by Django 5.1.6 on 2025-03-09 03:35

from django.db import migrations


class Migration(migrations.Migration):

    DML = """
        INSERT INTO restaurant_category (created_at, updated_at, active, category) VALUES 
            (now(), now(), True, 'Colombiana'),
            (now(), now(), True, 'Regional'),
            (now(), now(), True, 'Peruana'),
            (now(), now(), True, 'Mexicana'),
            (now(), now(), True, 'Italiana'),
            (now(), now(), True, 'Cafetería'),
            (now(), now(), True, 'Heladería');
    """

    dependencies = [
        ("restaurants", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(DML, reverse_sql=migrations.RunSQL.noop),
    ]
