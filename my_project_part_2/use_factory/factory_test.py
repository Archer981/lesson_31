import pytest


@pytest.mark.django_db
def test_create_vacancy(skill):
    # TODO напишите проверку здесь
    assert skill.name == 'Skill 1'
