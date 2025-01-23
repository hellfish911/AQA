"""This module tests registration."""

import pytest
import random
import string
from ..conftest import driver


@pytest.mark.usefixtures("driver")
def test_user_registration(login_page, registration_page):
    """Generate users data."""
    first_name = "Test"
    last_name = "User"
    email = f"testuser{random.randint(1000, 9999)}@example.com"
    password = "Password123"

    login_page.go_to_registration()

    registration_page.register_user(first_name, last_name, email, password)

    assert registration_page.is_garage_page_displayed(), "'Garage' page is not displayed!"
