"""Configuration module.

.. moduleauthor:: grzes71

"""

import logging
from collections import namedtuple

import weatherserver.config as cfg
from weatherserver.config import OPT_NAME, OPT_HOST, OPT_PORT

Configuration = namedtuple('Configuration', (OPT_NAME, OPT_HOST, OPT_PORT))


def logger():
    """Get logger instance.

    :return: logger instance
    :rtype: logging.Logger
    """
    return logging.getLogger(__name__)


def create_configuration(conf, args):
    """Create and return Configuration instance.

    :param  conf: Config section for config
    :type conf: configparser.SectionProxy
    :param  args: Command line arguments
    :type args: ArgParse
    :return: Configuration instance
    :rtype: weatherserver.config.Configuration
    """
    def get_val(opt_name, args_value):
        """Get value from args if it is not available in config file section.
        :param opt_name: Option name
        :type opt_name: str
        :param args_value: Value in args
        :return: Configuration value
        """
        return conf.get(opt_name) if not args_value else args_value

    name = get_val(cfg.OPT_NAME, args.name)
    host = get_val(cfg.OPT_HOST, args.server)
    port = int(get_val(cfg.OPT_PORT, args.port))
    configuration = Configuration(name, host, port)
    logger().debug("Created Configuration: %s", configuration)
    return configuration
