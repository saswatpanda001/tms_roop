from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounts.models import spent

@receiver(pre_save, sender=spent)
def update_item_name_on_spent_change(sender, instance, **kwargs):
    # If the instance already exists in the database
    if instance.pk:
        # Retrieve the original instance from the database
        original_instance = spent.objects.get(pk=instance.pk)
        # Check if 'spent_on' has changed
        if original_instance.spent_on != instance.spent_on:
            instance.item_name = instance.spent_on.name
    else:
        # For new instances, set the item_name
        instance.item_name = instance.spent_on.name