import json
from unittest.mock import patch, Mock
from src.ioc_api import Apioc


@patch("requests.request")
def test_requisicao_para_x_ips(mock_request):
    # Arrange
    endpoint = "https://api.abuseipdb.com/api/v2/check"
    token = "fake_token"

    api = Apioc(endpoint, token)

    mock_response = Mock()
    mock_response.text = json.dumps({
        "data": {
            "ipAddress": "118.25.7.39",
            "abuseConfidenceScore": 100
        }
    })

    mock_request.return_value = mock_response

    # Act
    response = api.requisicao_para_x_ips(
        accept="application/json",
        method="get"
    )

    # Assert
    assert response["data"]["ipAddress"] == "118.25.7.39"
    assert response["data"]["abuseConfidenceScore"] == 100

    mock_request.assert_called_once_with(
        method="GET",
        url=endpoint,
        headers={
            "Accept": "application/json",
            "Key": token
        },
        params={
            "ipAddress": "118.25.7.39",
            "maxAgeInDays": "90"
        }
    )