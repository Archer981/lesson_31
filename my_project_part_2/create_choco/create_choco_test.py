import pytest


@pytest.mark.django_db
def test_create_choco(client):
    # TODO напишите Ваш тест здесь
    expected_response = {
        'name': 'Choco',
    }

    data = {
        'name': 'Choko',
        'price': '100',
        'description': 'Chocolate',
    }

    response = client.post('/create_choco/', data=data)
    assert response.status_code == 201
    assert response.data == expected_response
