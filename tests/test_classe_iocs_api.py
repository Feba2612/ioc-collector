from unittest.mock import patch, Mock
from src.integrations_apis import ApiIntegrations


def test_requisicao_coleta_ips():
    """
    Testa se a função:
    
    1. Faz requisição GET corretamente
    2. Envia headers corretos
    3. Envia parâmetros corretos
    4. Retorna texto da resposta
    """

    # =====================================================
    # ARRANGE
    # =====================================================
    # Prepara os dados necessários para o teste
    # =====================================================

    endpoint = "https://api.abuseipdb.com/api/v2/blacklist"
    token = "TOKEN_TESTE"

    api = ApiIntegrations(endpoint, token)

    # Resposta falsa da API (texto bruto, pois o método retorna response.text)
    fake_response_text = """
    {
        "data": [
            {
                "ipAddress": "8.8.8.8",
                "abuseConfidenceScore": 100
            }
        ]
    }
    """

    # Mock da resposta HTTP
    mock_response = Mock()

    # Simula response.text da biblioteca requests
    mock_response.text = fake_response_text

    # =====================================================
    # ACT
    # =====================================================
    # Executa a função que queremos testar
    # =====================================================

    with patch('src.integrations_apis.requests.request', return_value=mock_response) as mock_request:

        resultado = api.abuseipdb_requisicao_coletaips()

        # =================================================
        # ASSERT
        # =================================================
        # Verifica se tudo ocorreu corretamente
        # =================================================

        # Verifica retorno
        assert resultado == fake_response_text

        # Verifica se requests.request foi chamado
        mock_request.assert_called_once()

        # Verifica parâmetros enviados
        mock_request.assert_called_with(
            method='GET',
            url=endpoint,
            headers={
                'Accept': 'text/plain',
                'Key': token
            },
            params={
                'limit': '10000',
                'ipVersion': 4
            }
        )