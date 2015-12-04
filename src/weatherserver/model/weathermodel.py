"""Weather Model

.. moduleauthor:: grzes71

"""
import logging

from collections import namedtuple


def logger():
    return logging.getLogger(__name__)


WeatherModel = namedtuple('WeatherModel', 'temperature, pressure, humidity, windspeed')
