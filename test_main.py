from main import app

def test_json_output():
    with app.test_client() as client:
        response = client.get('/?output=json')
        assert response.status_code == 200
        assert response.is_json
        assert response.get_json() == {"name": "Oliwer"}