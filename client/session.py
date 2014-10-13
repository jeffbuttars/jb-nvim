import os
import socket
import tornado.ioloop
import tornado.iostream

import nvim_funcs

NVIM_LISTEN_ADDRESS = os.environ.get('NVIM_LISTEN_ADDRESS', '/tmp/nvim')


class Session(object):

    def __init__(self, stream=None):
        self._stream = stream
        self._sock = None
        self._mid = 0

        if not self._stream:
            self._sock = socket.socket(
                socket.AF_UNIX, socket.SOCK_STREAM | socket.SOCK_NONBLOCK)
            self._stream = tornado.iostream.IOStream(self._sock)
            self._stream.connect(NVIM_LISTEN_ADDRESS, self.run)

        for k, v in nvim_funcs.function_classes:
            setattr(self, k, v(self))

    @property
    def mid(self):
        self._mid += 1
        return self._mid

    def start(self):
        ioloop = tornado.ioloop.IOLoop.instance()
        ioloop.start()

    def run(self):
        print("Running!", self._stream)

    def send(self, data, cb=None):
        return self._stream.write(data, callback=cb)

    def recv(self, num_bytes, cb=None):
        return self._stream.read_bytes(num_bytes, callback=cb)

    def send_msg(self, msg, cb=None):
        msg.mid = self.mid
        data = msg.pack()
        return self.send(data, cb)
