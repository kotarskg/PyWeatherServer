"""Weather Model

.. moduleauthor:: grzes71

"""

from collections import namedtuple

WeatherModel = namedtuple('WeatherModel', 'temperature, pressure, humidity, windspeed')
