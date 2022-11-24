from model_bakery import baker
import pytest

def test_if_password_data_is_being_created(db):
    first_password = baker.make("base.SecurePassword", name="TESTE", password="FIRST_TESTE")
    items = [items for items in first_password]
    breakpoint()
    assert first_password