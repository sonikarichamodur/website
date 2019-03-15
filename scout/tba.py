from django.conf import settings
from net.thefletcher.tbaapi.v3client import TBAApi
import logging

base_log = logging.getLogger('scout.tba')


class TBA(TBAApi):
    """ Custom TBA class """
    pass
