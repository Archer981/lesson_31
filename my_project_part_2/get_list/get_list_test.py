import pytest


@pytest.mark.django_db
def test_root_ok(client):
    # TODO напишите Ваш код здесь
    response = client.get('/get_list')
    assert response.status_code == 200
