from django.db import migrations


def create_plan(apps, schema_editor):
    Plan = apps.get_model('plan', 'Plan')

    plans = [
        {
            "id": '418e3e49-8ff7-48b2-8729-a60252325166',
            "name": "Menu basic plan",
            "type": "BASIC",
            "amount": 1099,
            "product": "MENU",
            "duration": 30
        },
        {
            "id": 'f5a1fab3-21aa-4d59-841f-50f0c561b21c',
            "name": "Menu advance plan",
            "type": "ADVANCE",
            "amount": 2999,
            "product": "MENU",
            "duration": 30
        },
    ]

    for plan in plans:
        Plan.objects.update_or_create(
            id=plan["id"],
            defaults={key: value for key, value in plan.items() if key != "id"}
        )


class Migration(migrations.Migration):
    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_plan),
    ]
