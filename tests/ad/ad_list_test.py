import pytest

from ads.serializers import AdSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client, access_token):
    ad_list = AdFactory.create_batch(4)
    response = client.get(f"/ads/", HTTP_AUTHORIZATION=f"Bearer {access_token}")
    assert response.status_code == 200
    assert response.data == {
        "count": 4,
        "next": None,
        "previous": None,
        "results": AdSerializer(ad_list, many=True).data
    }
