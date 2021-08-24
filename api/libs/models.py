from django.db import models


class TimeStampedModel(models.Model):
    """
    TimeStampedModel is an abstract model to add following fields in every
    model where it is inherited.
      - created_at
      - updated_at
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def get_all_field_names(cls):
        """
        This method returns the field names of the list
        """
        return [field.name for field in cls._meta.get_fields()]
