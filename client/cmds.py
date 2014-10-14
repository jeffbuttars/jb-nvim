from utils.log import logger

class Cmd(object):
    def __init__(self, session):
        self._session = session

    def send_sync(self, msg):
        logger.debug("send_sync: %s", msg)
        sent = self._session.send(msg)
        msg = self._session.read()
        logger.debug("sync recvd msg: %s", msg)
        return msg
