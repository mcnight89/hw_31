import pytest
from rest_framework import status

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, user_access_token):
    user, access_token = user_access_token
    ad_list = AdFactory.create_batch(10)
    data = {
        "name": "test",
        "author_id": None,
        "items": [ads.id for ads in ad_list],
    }

    expected_response = {
        "id": 1,
        "name": "test",
        "author_id": None,
        "items": [ads.id for ads in ad_list]
    }

    response = client.post(
        "/selection/create/",
        data=data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_response
