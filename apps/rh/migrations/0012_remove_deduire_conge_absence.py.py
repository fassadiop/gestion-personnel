from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rh", "00XX_derniere_migration"),
    ]

    operations = [

        migrations.RunSQL(
            sql="""
                ALTER TABLE rh_absence
                DROP COLUMN IF EXISTS deduire_conge;
            """,
            reverse_sql="""
                ALTER TABLE rh_absence
                ADD COLUMN deduire_conge BOOLEAN DEFAULT FALSE;
            """,
        ),

    ]