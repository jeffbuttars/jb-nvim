import os
import sys
import socket
import time
import tornado.ioloop
import tornado.iostream

from utils.log import logger
from utils.opts import OptionsParser
import nvim_funcs
from msg import Msg

NVIM_LISTEN_ADDRESS = os.environ.get('NVIM_LISTEN_ADDRESS', '/tmp/nvim')


class Session(object):

    def __init__(self, read_tout=3, opt_parser=None):
        self._stream = None
        self._sock = None
        self._mid = 0
        self._opt_parser = opt_parser
        self._read_tout = read_tout
        self._ioloop = tornado.ioloop.IOLoop.instance()

        if not self._stream:
            self._sock = socket.socket(
                socket.AF_UNIX, socket.SOCK_STREAM | socket.SOCK_NONBLOCK)
            self._stream = tornado.iostream.IOStream(self._sock)

            logger.debug("Connecting to UNIX socket at NVIM_LISTEN_ADDRESS: %s",
                         NVIM_LISTEN_ADDRESS)

            self._stream.connect(NVIM_LISTEN_ADDRESS, self.run)
            if self._stream.closed():
                logger.error("Unable to connect to socket, bailing.")
                sys.exit(1)

        for k, v in nvim_funcs.function_classes.items():
            setattr(self, k, v(self))

        # Get the API info

        self.api_info = self.vim.get_api_info()
        logger.debug("api_info: %s", self.api_info)

    @property
    def mid(self):
        self._mid += 1
        logger.debug("ID: %s", self._mid)
        return self._mid

    def start(self):
        logger.debug("Starting IOLoop")
        self._ioloop.start()

    def run(self):
        logger.debug("Running")

    def write(self, data, cb=None):
        logger.debug("writing to async stream '%s', callback: %s", data, cb)
        return self._stream.write(data, callback=cb)

    def send(self, msg):
        logger.debug("sending now: '%s'", msg)
        packed = msg.pack()
        logger.debug("sending now, packed: '%s'", packed)
        return self._stream.write_to_fd(packed)

    def read(self):
        logger.debug("sync read")

        # The socket is async, so keep reading for read_tout seconds
        res = self._stream.read_from_fd()
        now = time.monotonic()
        later = now + self._read_tout
        while not res and now < later:
            time.sleep(0.01)
            now = time.monotonic()
            res = self._stream.read_from_fd()

        if not res:
            raise Exception("Read timed out after {} seconds".format())

        logger.debug("sync read received: %s", res)
        msg = Msg.unpack(res)
        if not msg:
            return None
        logger.debug("sync read received unpacked: %s", msg)
        return msg

    def recv(self, num_bytes, cb=None):
        return self._stream.read_bytes(num_bytes, callback=cb)

    def send_msg(self, msg, cb=None):
        msg.mid = self.mid
        logger.debug("send_msg() ID: %s, msg: %s, callback: %s", msg.mid, msg, cb)
        data = msg.pack()
        return self.send(data, cb)
