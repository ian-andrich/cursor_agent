from typing import Any, Dict
import os
import logging
import ssl
import certifi
import httpx
import click
from dotenv import load_dotenv
from .base import BaseTool

logger = logging.getLogger(__name__)


class WeatherAPIError(Exception):
    """Custom exception for weather API errors."""
    pass


class WeatherTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="weather",
            description="Get current weather for a US city"
        )
        load_dotenv()
        self.api_key = os.getenv("WEATHER_API_KEY")
        logger.debug("API Key found: %s", "Yes" if self.api_key else "No")
        self.base_url = "https://api.weatherapi.com/v1"
    
    def _validate_api_key(self) -> None:
        """Validate that API key is present and has correct format."""
        if not self.api_key:
            raise WeatherAPIError(
                "WEATHER_API_KEY not found in environment. "
                "Please add it to your .env file."
            )
        if not isinstance(self.api_key, str) or len(self.api_key) < 16:
            raise WeatherAPIError("Invalid API key format")
    
    @property
    def parameters(self) -> Dict[str, Dict[str, Any]]:
        return {
            "city": {
                "type": "string",
                "description": (
                    "US city name (can include state e.g. 'Portland, OR')"
                ),
                "required": True
            }
        }

    async def execute(self, **kwargs: Any) -> Dict[str, Any]:
        self._validate_api_key()
            
        city = kwargs["city"]
        # Add US to ensure US locations
        location_query = f"{city}, United States of America"
        logger.debug("Fetching weather for: %s", location_query)
        
        try:
            # Create SSL context with certifi's certificates
            ssl_context = ssl.create_default_context(
                cafile=certifi.where()
            )
            
            async with httpx.AsyncClient(
                verify=ssl_context,
                timeout=httpx.Timeout(10.0)
            ) as client:
                url = f"{self.base_url}/current.json"
                params = {
                    "key": self.api_key,
                    "q": location_query,
                    "aqi": "no"
                }
                logger.debug("Request URL: %s", url)
                # Mask API key in logs
                safe_params = {**params, "key": "*" * len(params["key"])}
                logger.debug("Request params: %s", safe_params)
                
                try:
                    response = await client.get(url, params=params)
                    logger.debug("Response status: %d", response.status_code)
                    # Mask API key in URL logs
                    safe_url = str(response.url).replace(
                        self.api_key,
                        "*" * len(self.api_key)
                    )
                    logger.debug("Response URL: %s", safe_url)
                    
                    if response.status_code == 401:
                        raise WeatherAPIError("Invalid API key")
                    elif response.status_code == 400:
                        data = response.json()
                        error = data.get("error", {}).get(
                            "message", "Unknown error"
                        )
                        raise WeatherAPIError(f"API error: {error}")
                    elif response.status_code != 200:
                        raise WeatherAPIError(
                            f"API returned status code {response.status_code}"
                        )
                    
                    data = response.json()
                    logger.debug("Response data: %s", data)
                    
                    return {
                        "location": data["location"]["name"],
                        "region": data["location"]["region"],
                        "temp_f": data["current"]["temp_f"],
                        "condition": data["current"]["condition"]["text"],
                        "humidity": data["current"]["humidity"],
                        "wind_mph": data["current"]["wind_mph"]
                    }
                except httpx.RequestError as e:
                    raise WeatherAPIError(
                        f"Failed to connect to API: {str(e)}"
                    )
                except httpx.TimeoutException:
                    raise WeatherAPIError("Request timed out")
                except KeyError as e:
                    raise WeatherAPIError(
                        f"Missing data in API response: {str(e)}"
                    )
        except Exception as e:
            if not isinstance(e, WeatherAPIError):
                logger.exception("Unexpected error occurred")
                raise WeatherAPIError(f"Unexpected error: {str(e)}")
            raise


@click.command()
@click.argument("city")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging")
def weather_cli(city: str, verbose: bool):
    """Get current weather for a US city."""
    if verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    import asyncio
    tool = WeatherTool()
    try:
        result = asyncio.run(tool.execute(city=city))
        click.echo(
            f"\nWeather for {result['location']}, {result['region']}:\n"
            f"Temperature: {result['temp_f']}°F\n"
            f"Condition: {result['condition']}\n"
            f"Humidity: {result['humidity']}%\n"
            f"Wind: {result['wind_mph']} mph"
        )
    except WeatherAPIError as e:
        click.echo(f"Weather API error: {str(e)}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {str(e)}", err=True)
        logger.exception("Unexpected error in CLI")
        raise click.Abort()


if __name__ == "__main__":
    weather_cli() 