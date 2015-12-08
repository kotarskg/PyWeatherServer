"""Main Weather Server application module.

.. moduleauthor:: grzes71

"""

import argparse
import logging

from configparser import ConfigParser

import weatherserver.config as cfg

from weatherserver.config.configuration import create_configuration
from weatherserver.model.weathermodel import create_weather_model
from weatherserver.service.weatherservice import create_weather_service


def logger():
    """Get logger instance.

    :return: logger instance
    :rtype: logging.Logger
    """
    return logging.getLogger(__name__)


def do_parse_args():
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description='Weather Service')

    parser.add_argument('-d', '--data', type=argparse.FileType('r'),
                        help="File with weather data", required=True)

    parser.add_argument('-l', '--loglevel', choices=[cfg.LEV_DEBUG, cfg.LEV_INFO,
                                                     cfg.LEV_WARNING, cfg.LEV_ERROR],
                        help='logging level (default {debug})'.format(debug=cfg.LEV_DEBUG),
                        default=cfg.LEV_DEBUG)

    parser.add_argument('-n', '--name', help='name of the service')
    parser.add_argument('-s', '--server', help='host to listen')
    parser.add_argument('-p', '--port', type=int, help='port to listen')

    return parser.parse_args()


def main():
    """Main application entry.
    """
    parsed_args = do_parse_args()
    logging.basicConfig(level=parsed_args.loglevel)

    config_parser = ConfigParser()
    config_parser.read_file(parsed_args.data)

    configuration = create_configuration(config_parser[cfg.SEC_CONF], parsed_args)
    weather_model = create_weather_model(config_parser[cfg.SEC_SITE])
    simple_server = create_weather_service(configuration, weather_model)

    try:
        logger().info('Use Control-C to exit')
        simple_server.serve_forever()
    except KeyboardInterrupt:
        logger().debug("Exiting")
