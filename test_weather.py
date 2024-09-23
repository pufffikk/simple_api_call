import pytest
import requests
from unittest.mock import patch
from weather import get_weather


mock_weather_data = {
    "city": "New York",
    "temperature": "20°C",
    "description": "Clear sky"
}


@patch("weather.requests.get")
def test_get_weather_success(mock_get):
    # Mock the API response to return the mock_weather_data
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_weather_data

    city_name = "New York"

    result = get_weather(city_name)

    # Assert that the result matches the mock data
    assert result == mock_weather_data


@patch("weather.requests.get")
def test_get_weather_failure(mock_get):
    # Simulate a 404 error response
    mock_get.return_value.status_code = 404
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()

    city_name = "UnknownCity"

    # Assert that the SystemExit exception is raised due to the error
    with pytest.raises(SystemExit):
        get_weather(city_name)