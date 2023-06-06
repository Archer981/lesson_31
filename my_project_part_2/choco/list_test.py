import pytest

from choco.factories import ChocolateFactory


@pytest.mark.django_db
def test_list_view(client):
    # TODO напишите Ваш код здесь
    ChocolateFactory.create_batch(6)
    response = client.get('/choco/')
    assert len(response.data) == 5

