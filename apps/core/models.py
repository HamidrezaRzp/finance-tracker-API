# apps/core/models.py
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """base model with created_at و updated_at"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """for sof delete (is_active = False)"""
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_("deleted_at"))

    def soft_delete(self):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True