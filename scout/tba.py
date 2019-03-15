from django.conf import settings
from net.thefletcher.tbaapi.v3client import TBAApi
import logging

base_log = logging.getLogger('scout.tba')


class TBAAPIDown(RuntimeError):
    """ TBA API is down """


class TBA(TBAApi):
    """ Custom TBA class """

    def ping(self):
        """ Make sure api is alive """
        resp = self.get_status()
        return not resp.get('is_datafeed_down', True)
