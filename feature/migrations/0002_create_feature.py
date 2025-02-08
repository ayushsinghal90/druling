from django.db import migrations


def create_plan(apps, schema_editor):
    Feature = apps.get_model('feature', 'Feature')
    Plan = apps.get_model("plan", "Plan")

    features = [
        {
            "id": "de2f2b83-7cf4-430c-81e4-a1b4d1cab5c3",
            "plan_id": '418e3e49-8ff7-48b2-8729-a60252325166',
            "description": "Menu basic plan",
            "type": "QR_MENU",
            "limit": 1
        },
        {
            "id": "5aff8be3-2f88-41f2-a3a9-c4078b0565fc",
            "plan_id": 'f5a1fab3-21aa-4d59-841f-50f0c561b21c',
            "description": "Menu advance plan",
            "type": "QR_MENU",
            "limit": 4
        },
    ]

    for feature in features:
        try:
            plan = Plan.objects.get(id=feature["plan_id"])

            defaults = {key: value for key, value in feature.items() if key != "id"}
            defaults["plan"] = plan
            Feature.objects.update_or_create(
                id=feature["id"],
                defaults=defaults,
            )
        except Plan.DoesNotExist:
            print(f"Plan with ID {feature['plan_id']} does not exist. Skipping.")


class Migration(migrations.Migration):
    dependencies = [
        ("feature", "0001_initial"),
        ("plan", "0001_create_plan"),
    ]

    operations = [
        migrations.RunPython(create_plan),
    ]
