#!/usr/bin/env python
# encoding: utf-8
# 2014-10-12 17:05:17.676061

import builtins
import subprocess
import tempfile
import keyword
import msgpack
from pprint import pformat as pf


def convert(x):
    if isinstance(x, bytes):
        return x.decode('utf-8')
    return x


def kword(kw):
    if kw in keyword.kwlist or kw in dir(builtins):
        return 'v_' + kw
    return kw


def print_func(func):
    fmt = (
        "    # Function: {name}\n"
        "    # Parameters {parameters}\n"
        "    # Returns {return_type}\n"
        "    # Recieves channel id {receives_channel_id}\n"
        "    # Can fail {can_fail}\n"
        "    def {func_name}(self, {args}):\n"
        "        return self.send_sync(ReqMsg('{name}', *[{args}]))\n"
        )

    func['receives_channel_id'] = func.get('receives_channel_id', False)
    func['can_fail'] = func.get('can_fail', False)
    func['args'] = ', '.join([kword(x[1]) for x in func.get('parameters', [])])
    func['parameters'] = ', '.join(
        [x[0] + ': ' + x[1] for x in func.get('parameters', [])])
    print(fmt.format(**func))


def print_cls(cls, funcs):
    fmt = (
        "\nclass {}(Cmd):\n\n"
        "    def __init__(self, session):\n"
        "        self._session = session\n"
    )
    print(fmt.format(cls))

    for func in funcs:
        print_func(func)


def parse_funcs(funcs):

    cls_map = {}

    for func in funcs:
        fn = func['name']
        cls, name = fn.split('_', 1)
        cls = cls.title()
        func['func_name'] = name
        if cls not in cls_map:
            cls_map[cls] = []

        cls_map[cls].append(func)

    for k, v in cls_map.items():
        print_cls(k, v)

    print("function_classes = {")
    for k in cls_map:
        print("    '{}': {},".format(k.lower(), k))
    print("}\n")


def main():
    try:
        fd = tempfile.TemporaryFile()
        with subprocess.Popen(['nvim', '--api-info'], stdout=subprocess.PIPE) as proc:
            fd.write(proc.stdout.read())
    except subprocess.CalledProcessError:
        print("Error running nvim --api-info")
        raise

    fd.seek(0)
    func_info = msgpack.unpackb(
        fd.read(), encoding='utf-8',
        object_hook=lambda obj: {convert(k): convert(v) for k, v in obj.items()},
        list_hook=lambda item: [convert(x) for x in item],
    )

    # print("api_info =", pf(func_info))
    print("from msg import ReqMsg")
    print("from cmds import Cmd\n")
    parse_funcs(func_info['functions'])

if __name__ == '__main__':
    main()
