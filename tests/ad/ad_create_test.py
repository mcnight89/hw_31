import pytest
from rest_framework import status


@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        "author_id": user.id,
        "name": "Test 10 characters minimum",
        "price": 2500,
        "description": "Test description",
        "is_published": False,
        "category_id": category.id,
    }
    expected_response = {
        "id": user.id,
        "name": "Test 10 characters minimum",
        "price": 2500,
        "author_id": user.id,
        "category_id": category.id,
        "is_published": False,
        "description": "Test description"
    }

    response = client.post("/ads/create/",
                           data=data,
                           content_type='application/json',
                           HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_response
