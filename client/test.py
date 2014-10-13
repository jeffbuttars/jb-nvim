#!/usr/bin/env python
# encoding: utf-8
# 2014-10-12 19:07:57.165946

import logging

# Set up the logger
logger = logging.getLogger(__name__)
# Use a console handler, set it to debug by default
logger_ch = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter(('%(levelname)s: %(asctime)s %(processName)s:%(process)d'
                                   ' %(filename)s:%(lineno)s %(module)s::%(funcName)s()'
                                   ' -- %(message)s'))
logger_ch.setFormatter(log_formatter)
logger.addHandler(logger_ch)

import os
import socket
import time
import msgpack
import funcs

NVIM_LISTEN_ADDRESS = os.environ.get('NVIM_LISTEN_ADDRESS', '/tmp/nvim')

def function(arg1):
    """todo: Docstring for function
    
    :param arg1: arg description
    :type arg1: type description
    :return:
    :rtype:
    """

    pass


# https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md
def main():

    # fd = open(NVIM_LISTEN_ADDRESS)
    # sock = socket.fromfd(fd, socket.AF_UNIX, socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM | socket.SOCK_NONBLOCK)
    # sock.bind(NVIM_LISTEN_ADDRESS)
    sock.connect(NVIM_LISTEN_ADDRESS)
    logger.debug("sock %s: %s", sock, sock.fileno())

    msg_id = 1
    # msg = [0, msg_id] + funcs.vim_command('echo "some shit"')
    # sent = sock.send(msgpack.packb(msg))

    # msg = [0, msg_id] + funcs.vim_subscribe('text_changed')
    msg = [0, msg_id] + funcs.vim_subscribe('text_changed')
    # msg = 
    # print("msg", msg)
    # sent = sock.send(msgpack.packb(msg))

    cmd_q = []
    # channel id is returned by this, call this first to get the id. 
    # the id is the first member of the array returned
    cmd_q.append([0, msg_id] + funcs.vim_get_api_info())
    msg_id += 1
    cmd_q.append([0, msg_id] + funcs.vim_subscribe('text_changed'))
    msg_id += 1
    # cmd_q.append([0, msg_id] + funcs.vim_command(
    #     'au FileType python call rpcnotify(%d, "py!", bufnr("$"))'))
    # msg_id += 1

    nostop = True
    while nostop:
        if cmd_q:
            sock.send(msgpack.packb(cmd_q.pop(0)))
                
        try:
            recvd = sock.recv(10000)
            print("recvd", recvd)
            logger.debug("recvd: %s", msgpack.unpackb(recvd))
            # nostop = False
        except BlockingIOError:
            time.sleep(0.2)


if __name__ == '__main__':
    main()
