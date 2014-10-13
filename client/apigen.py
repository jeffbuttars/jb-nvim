#!/usr/bin/env python
# encoding: utf-8
# 2014-10-12 17:05:17.676061

import subprocess
import tempfile
import msgpack


def convert(x):
    if isinstance(x, bytes):
        return x.decode('utf-8')
    return x


def object_hook(obj):
    return {convert(k): convert(v) for k, v in obj.items()}


def list_hook(item):
    return [convert(x) for x in item]


def print_func(func):
    # print("FUNC:", func)
    # print("FUNC:", {k.decode(): v for k, v in func.items()})

    # func = {k.decode(): v for k, v in func.items()}
    func['can_fail'] = func.get('can_fail', False)
    fmt = (
        "# Function: {name}\n"
        "# Parameters {parameters}\n"
        "# Returns {return_type}\n"
        "# Can fail {can_fail}\n"
        "def {name}({args}):\n"
        "\tpass\n\n\n")

    func['args'] = ', '.join([x[1] for x in func.get('parameters', [])])
    func['parameters'] = ', '.join([x[0] + ': ' + x[1] for x in func.get('parameters', [])])
    print(fmt.format(**func))


# def print_dict(d, title):
#     print(title)

#     if isinstance(d, dict):
#         for k, v in d.items():
#             print("\t'%s': %s" % (k, v))


def main():
    try:
        fd = tempfile.TemporaryFile()
        with subprocess.Popen(['nvim', '--api-info'], stdout=subprocess.PIPE) as proc:
            fd.write(proc.stdout.read())
            # print("GO: ", output.__class__)
            # print("GO: ", output)
        # output = subprocess.check_output(['nvim', '--api-info'])
    except subprocess.CalledProcessError:
        print("Error running nvim --api-info")
        raise

    fd.seek(0)
    func_info = msgpack.unpackb(
        fd.read(), encoding='utf-8',
        object_hook=object_hook,
        list_hook=list_hook,
    )

    # for k, v in func_info.items():
    #     print("{}".format(k))

    # print("As Python:", func_info)

    # print_dict(func_info['types'], "*** Types ***")
    # print_dict(func_info['features'], "*** Features ***")
    # print_dict(func_info['error_types'], "*** Error Types ***")
    # print_dict(func_info['functions'], "*** Functions ***")

    for func in func_info['functions']:
        print_func(func)

if __name__ == '__main__':
    main()
