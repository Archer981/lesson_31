import pytest


@pytest.mark.parametrize('name, statuscode', [('Choco', 201), ('Test', 422)])
@pytest.mark.django_db
def test_save_choco(client, name, status_code):
    # TODO напишите Ваш код здесь
    data = {
        'name': name,
        'description': 'test',
        'price': 1000,
    }
    response = client.post('/chocolate/create/', data=data)
    assert response.status_code == status_code
