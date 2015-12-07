"""XML-RPC server implementation serving Weather Report data.

.. moduleauthor:: grzes71

"""

import logging

from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer


def logger():
    """Get logger instance.

    :return: logger instance
    :rtype: logging.Logger
    """
    return logging.getLogger(__name__)


class WeatherService:
    """Weather Service class providing access to model data.
    """
    def __init__(self, label, model):
        """WeatherService constructor.

        :param label: Name of the service
        :type label: string
        :param model: Model of the data for the service
        :type model: weatherserver.model.WeatherModel
        """
        self._label = label
        self._model = model

    @property
    def model(self):
        """Getter for service model.

        :return: Weather model instance
        :rtype: weatherserver.model.WeatherModel
        """
        return self._model

    @property
    def label(self):
        """Getter for service label.

        :return: Name of the service
        :rtype: string
        """
        return self._label

    def temperature(self, identity):
        """Service method to provide temperature.

        :param identity: Requester identity
        :type identity: string
        :return: Temperature
        :rtype: float
        """
        logger().debug("Identity %s asks %s for temperature = %s", identity, self.label, self.model.temperature)
        return self.model.temperature

    def humidity(self, identity):
        """Service method to provide humidity in percent.

        :param identity: Requester identity
        :type identity: string
        :return: Humidity
        :rtype: integer
        """
        logger().debug("Identity %s asks %s for humidity = %s", identity, self.label, self.model.humidity)
        return self.model.humidity

    def windspeed(self, identity):
        """Service method to provide wind speed.

        :param identity: Requester identity
        :type identity: string
        :return: Wind speed
        :rtype: float
        """
        logger().debug("Identity %s asks %s for wind speed = %s", identity, self.label, self.model.windspeed)
        return self.model.windspeed

    def pressure(self, identity):
        """Service method to provide pressure value.

        :param identity: Requester identity
        :type identity: string
        :return: Pressure
        :rtype: float
        """
        logger().debug("Identity %s asks %s for pressure = %s", identity, self.label, self.model.pressure)
        return self.model.pressure

    def datetime(self, identity):
        """Service method to provide current server date and time.

        :param identity: Requester identity
        :type identity: string
        :return: Data and time
        :rtype: datetime
        """
        now = datetime.now()
        logger().debug("Identity %s asks %s for time = %s", identity, self.label, now)
        return now

    def name(self, identity):
        """Service method to provide site name.

        :param identity: Requester identity
        :type identity: string
        :return: Name of the location
        :rtype: string
        """
        logger().debug("Identity %s asks %s for name", identity, self.label)
        return self.label

    def __str__(self):
        return '{} {}'.format(self.label, str(self.model))

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__,
                                   self.label, str(self.model))


def create_weather_service(config, weather_model):
    """Create and register service, then start server

    :param config: Configuration instance
    :type config: weatherserver.config.Configuration
    :param weather_model: WeatherModel instance
    :type weather_model: weatherserver.model.WeatherModel
    :return: Server instance
    :rtype: SimpleXMLRPCServer
    """
    weather_service = WeatherService(config.name, weather_model)
    simple_server = SimpleXMLRPCServer((config.host, config.port))
    simple_server.register_multicall_functions()
    simple_server.register_introspection_functions()
    simple_server.register_instance(weather_service)
    logger().debug("Created Weather Service: %s", weather_service)
    return simple_server
