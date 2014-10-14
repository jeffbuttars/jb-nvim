from optparse import OptionParser
import logging
from .log import logger

class OptionsParser(object):

    def __init__(self, usage=None):
        self.usage = usage
        opt_parser = OptionParser(usage=usage)

        # A basic option that sets an option variable to a string value
        # opt_parser.add_option(
        #     "-c", "--config", dest="config_file",
        #         default="",
        #         help="The path to the config file for this program")

        # An example of a boolean option
        opt_parser.add_option("-d", "--debug", dest="debug",
                action="store_true", default=False,
                help="Run in debug mode"
        )

        # 'options' is an object that allows easy referencing of the
        # parser options added above.
        # Ex: To the the value of the '--config' option refercence: options.config_file
        # 'args' is a list of arguments given that aren't part of the option switches
        # defined above.
        # Ex: If the command '$ command --config=/path/to/config start' is called
        # Then args would look like: ['start']
        self.opt_parser = opt_parser
        (self.options, self.args) = opt_parser.parse_args()

        if self.options.debug:
            logger.setLevel(logging.DEBUG)
