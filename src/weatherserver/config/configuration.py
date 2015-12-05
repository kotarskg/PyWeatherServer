"""Configuration module.

.. moduleauthor:: grzes71

"""

from collections import namedtuple

import weatherserver.config as cfg

Configuration = namedtuple('Configuration', 'name host port')


def create_configuration(conf, args):
    """Create and return Configuration instance.
    :param  conf: configuration.
    :type conf: ConfigParser.
    :param  args: command line arguments.
    :type conf: ArgParse.
    :return: Configuration instance
    :rtype: Configuration
    """
    def get_val(opt_name, args_value):
        return conf.get(opt_name) if not args_value else args_value

    name = get_val(cfg.OPT_NAME, args.name)
    host = get_val(cfg.OPT_HOST, args.server)
    port = int(get_val(cfg.OPT_PORT, args.port))
    return Configuration(name, host, port)
