"""Weather Model

.. moduleauthor:: grzes71

"""

import logging
from collections import namedtuple

import weatherserver.config as cfg

WeatherModel = namedtuple('WeatherModel', (cfg.OPT_TEMPERATURE, 
                                           cfg.OPT_PRESSURE,
                                           cfg.OPT_HUMIDITY, 
                                           cfg.OPT_WINDSPEED))


def logger():
    """Get logger instance.

    :return: logger instance
    :rtype: logging.Logger
    """
    return logging.getLogger(__name__)


def create_weather_model(site_config):
    """Create weather model using configuration data.

    :param site_config: Config section for Site
    :type site_config: configparser.SectionProxy
    :return: Weather model instance
    :rtype: weatherserver.model.WeatherModel
    """
    temperature = site_config.getfloat(cfg.OPT_TEMPERATURE)
    pressure = site_config.getfloat(cfg.OPT_PRESSURE)
    humidity = site_config.getint(cfg.OPT_HUMIDITY)
    windspeed = site_config.getfloat(cfg.OPT_WINDSPEED)
    weather_model = WeatherModel(temperature, pressure, humidity, windspeed)
    logger().debug("Created Weather Model: %s", weather_model)
    return weather_model
