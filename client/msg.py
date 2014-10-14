import msgpack

MSGID = 1
MSG_REQUEST = 0
MSG_RESPONSE = 1
MSG_NOTIFY = 2


def data_unpack(data):

    def convert(x):
        if isinstance(x, bytes):
            return x.decode('utf-8')
        return x

    return msgpack.unpackb(
        data,
        encoding='utf-8',
        object_hook=lambda obj: {convert(k): convert(v) for k, v in obj.items()},
        list_hook=lambda item: [convert(x) for x in item],
    )


def data_pack(data):
    return msgpack.packb(data)


class Msg(object):

    @classmethod
    def unpack(cls, data):
        if not data:
            return None    

        msg_data = data_unpack(data)

        if len(msg_data) == 4:
            if msg_data[0] == MSG_REQUEST:
                return ReqMsg(msg_data[2], msg_data[3])

            if msg_data[0] == MSG_RESPONSE:
                return RespMsg(msg_data[1], msg_data[2], msg_data[3])

            if msg_data[0] == MSG_NOTIFY:
                return Notification(msg_data[1], msg_data[2])

        return msg_data

    def __init__(self, method, *params):
        self._mtype = 0
        self.method = method
        self.params = params

    def pack(self, mid=1):
        return data_pack([
            self._mtype,
            mid,
            self.method,
            self.params
        ])

    def __str__(self):
        return "type: {}, method: {}, params: {}".format(
            self._mtype, self.method, self.params
        )


class ReqMsg(Msg):
    def __init__(self, method, *params):
        super(ReqMsg, self).__init__(method, *params)
        self.mtype = MSG_REQUEST


class RespMsg(Msg):
    def __init__(self, mid, error, result):
        self._mtype = MSG_RESPONSE
        self.mid = mid
        self.error = error
        self.result = result

    def pack(self):
        raise NotImplementedError

    def __str__(self):
        return "type: {}, error: {}, result: {}".format(
            self._mtype, self.error, self.result
        )


class Notification(Msg):

    def __init__(self, method, *params):
        self._mtype = MSG_NOTIFY 
        self.method = method
        self.params = params

    def pack(self):
        raise NotImplementedError
