from django.conf import settings
import logging
import net.thefletcher.tbaapi.v3client
from .tba import TBA, TBAAPIDown

base_log = logging.getLogger('scout.helpers')


def get_tba(p_log=base_log):
    """ Get an instance of the blue alliance api"""
    log = p_log.getChild('get_tba')
    log.debug("Creating tba")
    net.thefletcher.tbaapi.v3client.configuration.api_key['X-TBA-Auth-Key'] = settings.TBA_AUTH_KEY
    # TODO: Look into wrapping in a try/except
    api_instance = TBA()
    log.debug("Created api instance", extra=dict(api=api_instance))
    if api_instance.ping():
        return api_instance
    else:
        raise TBAAPIDown("API reported as down")
