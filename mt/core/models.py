from django.core.exceptions import ValidationError
from django.db import models

from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel
from model_utils import Choices

from .behaviors import Payable, Permalinkable

class Event(Permalinkable, TimeStampedModel):
    # status: open or closed for registration
    STATUS = Choices('open', 'closed')
    status = StatusField(help_text="Status of registration.")
    name = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return "{} ({} to {})".format(self.name, self.start, self.end)

    def clean(self):
        if self.start > self.end:
            raise ValidationError("Event: start cannot be after end.")

class PaidEvent(Payable, Event):
    fees_due = models.DateField()

class Item(TimeStampedModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    choices_enabled = models.BooleanField(
        default=False,
        help_text=("Whether or not to show choices. "
                   "This doesn't disable actually having choices, however.")
    )

    def __str__(self):
        return "{} (Event: {})".format(self.name, self.event)

class PaidItem(Payable, Item):
    def clean(self):
        if not isinstance(self.event, PaidEvent):
            msg = ("PaidItem: event must be a PaidEvent. "
                   "(If you want a free event with paid items, "
                   "create a PaidEvent with fee = 0.)")
            raise ValidationError(msg)

class ItemChoice(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
