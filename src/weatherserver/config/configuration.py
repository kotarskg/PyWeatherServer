"""Configuration module.
"""

import weatherserver.config as cfg


class Configuration:
    """Configuration class
    """
    def __init__(self, conf, args):
        """Constructor for the Configuration class.

        :param  conf: configuration.
        :type conf: ConfigParser.
        :param  args: command line arguments.
        :type conf: ArgParse.
        """
        self._name = self._get_val(conf, cfg.OPT_NAME, args.name)
        self._host = self._get_val(conf, cfg.OPT_HOST, args.server)
        self._port = int(self._get_val(conf, cfg.OPT_PORT, args.port))

    def _get_val(self, conf, opt_name, args_value):
        return conf.get(opt_name) if not args_value else args_value

    @property
    def name(self):
        """Name of the service getter
        """
        return self._name

    @property
    def host(self):
        """Host name for the service getter
        """
        return self._host

    @property
    def port(self):
        """Service port number getter
        """
        return self._port

    def __repr__(self):
        return "{}({},{})".format(self.__class__.__name__,
                                  self.host, self.port)

    def __str__(self):
        return 'Configuration {} for {}:{}'.format(self.name,
                                                   self.host, self.port)
