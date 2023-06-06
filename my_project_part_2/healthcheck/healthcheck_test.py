import pytest


@pytest.mark.parametrize('url', ["/lifecheck/", "/readycheck/", "/healthcheck/"])
def test_lifecheck(client, url):
    # TODO напишите Ваш тест здесь
    response = client.get(url)

    assert response.status_code == 200
