import datetime
import pytest

from django.core.exceptions import ValidationError

from model_mommy import mommy

from .models import Event, PaidEvent, Item, PaidItem, ItemChoice

def test_trivial():
    assert True is True

@pytest.fixture
def event(db):
    return mommy.make(Event)

@pytest.fixture
def paid_event(db):
    return mommy.make(PaidEvent)

@pytest.fixture
def item(db):
    return mommy.make(Item)

@pytest.fixture
def paid_item(db):
    return mommy.make(PaidItem)

@pytest.fixture
def item_choice(db):
    return mommy.make(ItemChoice)

@pytest.mark.django_db
def test_event_bad_start_date():
    event = mommy.make(
        Event,
        start=datetime.date.today(),
        end=datetime.date.today() - datetime.timedelta(days=1)
    )
    with pytest.raises(ValidationError):
        event.full_clean()

@pytest.mark.django_db
def test_event_start_end_equal():
    event = mommy.make(
        Event,
        start=datetime.date.today(),
        end=datetime.date.today()
    )
    try:
        event.full_clean()
    except:
        assert False
    else:
        assert True

@pytest.mark.django_db
def test_paid_item_regular_event(event):
    paid_item = mommy.make(PaidItem, event=event)
    with pytest.raises(ValidationError):
        paid_item.full_clean()

@pytest.mark.django_db
def test_paid_item_paid_event(paid_event):
    paid_item = mommy.make(PaidItem, event=paid_event)
    try:
        paid_item.full_clean()
    except:
        assert False
    else:
        assert True

def test_event_str(event):
    s = "{} ({} to {})".format(event.name, event.start, event.end)
    assert s == str(event)

@pytest.mark.django_db
def test_item_str(event):
    item = mommy.make(Item, event=event)
    event_s = "{} ({} to {})".format(event.name, event.start, event.end)
    item_s = "{} (Event: {})".format(item.name, event_s)
    assert item_s == str(item)

def test_item_choice_str(item_choice):
    assert item_choice.name == str(item_choice)

if __name__ == '__main__':
    pytest.main()
