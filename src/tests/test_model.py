"""Weather Model unit tests

.. moduleauthor:: grzes71

"""

import unittest
from configparser import SafeConfigParser

from weatherserver.config import (OPT_HUMIDITY,
                                  OPT_PRESSURE,
                                  OPT_TEMPERATURE,
                                  OPT_WINDSPEED,
                                  SEC_SITE)
from weatherserver.model.weathermodel import create_weather_model, WeatherModel

TEST_TEMPERATURE_VALUE = 7.4
TEST_HUMIDITY_VALUE = 45
TEST_WINDSPEED_VALUE = 15.5
TEST_PRESSURE_VALUE = 1020

TEST_CONFIG = """
[{}]
temperature = {}
humidity = {}
windspeed = {}
pressure = {}
""".format(SEC_SITE,
           TEST_TEMPERATURE_VALUE,
           TEST_HUMIDITY_VALUE,
           TEST_WINDSPEED_VALUE,
           TEST_PRESSURE_VALUE)


class TestModel(unittest.TestCase):
    """Test Weather Model class
    """
    def setUp(self):
        unittest.TestCase.setUp(self)
        config_parser = SafeConfigParser()
        config_parser.read_string(TEST_CONFIG)
        self.site_config = config_parser[SEC_SITE]

    def test_weather_model(self):
        """test weather model type
        """
        weather_model = WeatherModel(TEST_TEMPERATURE_VALUE,
                                     TEST_HUMIDITY_VALUE,
                                     TEST_WINDSPEED_VALUE,
                                     TEST_PRESSURE_VALUE)
        self.assertEqual(weather_model.temperature, TEST_TEMPERATURE_VALUE)
        self.assertEqual(weather_model.pressure, TEST_HUMIDITY_VALUE)
        self.assertEqual(weather_model.humidity, TEST_WINDSPEED_VALUE)
        self.assertEqual(weather_model.windspeed, TEST_PRESSURE_VALUE)

    def test_create_weather_model(self):
        """test method creating weather model from config
        """
        model = create_weather_model(self.site_config)
        self.assertEqual(model.temperature, self.site_config.getfloat(OPT_TEMPERATURE))
        self.assertEqual(model.humidity, self.site_config.getfloat(OPT_HUMIDITY))
        self.assertEqual(model.pressure, self.site_config.getfloat(OPT_PRESSURE))
        self.assertEqual(model.windspeed, self.site_config.getfloat(OPT_WINDSPEED))


if __name__ == '__main__':
    unittest.main()
