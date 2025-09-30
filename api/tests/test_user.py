import pytest

from api.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create(
        email="matheus@gmail.com",
        username="gaucho",
        user_pass="monster",
        first_name="tulipa",
        last_name="Alho",
        country="Brasil",
        state="São Paulo",
        city="mairiqnue",
        postal_code="12345-789",
        address="R. dos Bobos, nº0"
    )

    assert user.username == "gaucho"
    assert user.first_name == "tulipa"
    assert user.country == "Brasil"
    assert user.city == "mairiqnue"
    assert user.id is not None

