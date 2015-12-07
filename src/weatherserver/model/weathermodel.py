"""Weather Model

.. moduleauthor:: grzes71

"""

from collections import namedtuple
import weatherserver.config as cfg

WeatherModel = namedtuple('WeatherModel', 'temperature pressure humidity windspeed')


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
    return WeatherModel(temperature, pressure, humidity, windspeed)
