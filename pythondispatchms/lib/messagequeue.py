from tg import app_globals,abort,request
import stomp
from stomp import ConnectionListener
from stomp import StatsListener
import logging

class MyListener(ConnectionListener):
    def on_message(self, headers, message):
        pass

class MyStatsListener(StatsListener):
    def on_disconnected(self):
        pass


class Message(object):
    @classmethod
    def post(cls, user,body):
        """Return Status of post"""
        logging.config.dictConfig({
            'version': 1,
            'disable_existing_loggers': True,
        })
        c = stomp.Connection([(app_globals.stompHost, 61613)])
        c.start()
        c.set_listener('my_listener', MyListener())
        c.set_listener('stats_listener', MyStatsListener())
        c.connect(app_globals.stompUserName , app_globals.stompPassword, wait=True)
        c.send(body=body, destination='/topic/' + user )
        c.disconnect()
        return ""