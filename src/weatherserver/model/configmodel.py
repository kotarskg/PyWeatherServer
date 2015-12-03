"""Configuration for the application.

.. moduleauthor:: grzes71

"""
import logging


def logger():
    return logging.getLogger(__name__)


class ConfigWeatherModel:
    """Model for weather data provided by configuration file.
    """
    def __init__(self, temperature, pressure, humidity, windspeed):
        """Constructor of the ConfigWeatherModel class.

        :param float temperature: Temperature value [C]
        :param float pressure: Pressure value [hPa].
        :param int humidity: Humidity value [percent].
        :param float windspeed: Wind speed valiue [km/h]
        """
        self._temperature = temperature
        self._windspeed = windspeed
        self._pressure = pressure
        self._humidity = humidity
        logger().debug('Created {} {}'.format(self.__class__.__name__, str(self)))

    @property
    def temperature(self):
        """Temperature getter.
        """
        return self._temperature

    @property
    def humidity(self):
        """Humidity getter.
        """
        return self._humidity

    @property
    def windspeed(self):
        """Wind speed getter.
        """
        return self._windspeed

    @property
    def pressure(self):
        """Pressure getter.
        """
        return self._pressure

    def __repr__(self):
        return '{}({},{},{},{})'.format(self.__class__.__name__,
                                        self.temperature,
                                        self.pressure,
                                        self.humidity,
                                        self.windspeed)

    def __str__(self):
        return "Temperature={:2.2f} Pressure={:.0f} Humidity={} Windspeed={:2.2f}".format(
                                        self.temperature,
                                        self.pressure,
                                        self.humidity,
                                        self.windspeed)
