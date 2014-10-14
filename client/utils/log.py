import logging

# Set up the logger
logger = logging.getLogger('jb-nvim')
# Use a console handler, set it to debug by default
logger_ch = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter(('%(levelname)s: %(asctime)s %(processName)s:%(process)d'
                                   ' %(filename)s:%(lineno)s %(module)s::%(funcName)s()'
                                   ' -- %(message)s'))
logger_ch.setFormatter(log_formatter)
logger.addHandler(logger_ch)
