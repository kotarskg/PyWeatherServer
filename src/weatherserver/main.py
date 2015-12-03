"""Main application module.
"""

import argparse
import logging

from configparser import SafeConfigParser

import weatherserver.config as cfg

from weatherserver.config.configuration import Configuration
from weatherserver.model.configmodel import ConfigWeatherModel
from weatherserver.service.weatherservice import WeatherService

def logger():
    """Get logger.
    """
    return logging.getLogger(__name__)


def do_parse_args(config):
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


def create_weather_config(site_config):
    """Create weather model using configuration data.
    """
    temperature = site_config.getfloat(cfg.OPT_TEMPERATURE)
    pressure = site_config.getfloat(cfg.OPT_PRESSURE)
    humidity = site_config.getint(cfg.OPT_HUMIDITY)
    windspeed = site_config.getfloat(cfg.OPT_WINDSPEED)
    return ConfigWeatherModel(temperature, pressure, humidity, windspeed)

    
def main():
    """Main application entry.
    """
    conf = SafeConfigParser()
    args = do_parse_args(conf)
    logging.basicConfig(level=args.loglevel)
    conf.read_file(args.data)
    
    app_config = Configuration(conf[cfg.SEC_CONF], args)

    weather_model = create_weather_config(conf[cfg.SEC_SITE])
    
    WeatherService.start_weather_service(app_config, weather_model)
    