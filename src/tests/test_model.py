"""Weather Model unit tests

.. moduleauthor:: grzes71

"""

import unittest
from configparser import SafeConfigParser

from weatherserver.config import OPT_HUMIDITY, OPT_PRESSURE, OPT_TEMPERATURE, OPT_WINDSPEED
from weatherserver.model.weathermodel import create_weather_model, WeatherModel

TEST_CONFIG = """
[site]
temperature = 7.4
humidity = 45
windspeed = 15.5
pressure = 1020
"""


class TestModel(unittest.TestCase):
    """Test Weather Model class
    """
    def setUp(self):
        unittest.TestCase.setUp(self)
        config_parser = SafeConfigParser()
        config_parser.read_string(TEST_CONFIG)
        self.site_config = config_parser['site']

    def test_weather_model(self):
        """test weather model type
        """
        weather_model = WeatherModel(10, 20, 30, 40)
        self.assertEqual(weather_model.temperature, 10)
        self.assertEqual(weather_model.pressure, 20)
        self.assertEqual(weather_model.humidity, 30)
        self.assertEqual(weather_model.windspeed, 40)

    def test_create_weather_model(self):
        """test method creating weather model from config
        """
        model = create_weather_model(self.site_config)
        self.assertEqual(model.temperature, self.site_config.getfloat(OPT_TEMPERATURE))
        self.assertEqual(model.humidity, self.site_config.getfloat(OPT_HUMIDITY))
        self.assertEqual(model.pressure, self.site_config.getfloat(OPT_PRESSURE))
        self.assertEqual(model.windspeed, self.site_config.getfloat(OPT_WINDSPEED))
