from django.conf import settings
from net.thefletcher.tbaapi.v3client import TBAApi
import logging
from functools import wraps

base_log = logging.getLogger('scout.tba')


class TBAAPIDown(RuntimeError):
    """ TBA API is down """


def chc(timeout=60):
    def dec(f):
        @wraps(f)
        def wrapped(self, *args, **kwargs):
            fname = f.__name__
            ckey = self.cache_name('chc', fname=fname, cname=self.__class__.__name__)
            cached = self.c.get(ckey, version=self.cache_version, default=None)
            if cached is None:
                ret = f(self, *args, **kwargs)
                self.c.set(ckey, ret, timeout=timeout, version=self.cache_version)
                return ret
            else:
                return cached

        return wrapped

    return dec


class TBA(TBAApi):
    """ Custom TBA class """

    def __init__(self):
        import net.thefletcher.tbaapi.v3client
        from django.core.cache import cache
        # Django's main cache
        self.c = cache
        self.c_prefix = self.__class__.__name__

        self.configuration = net.thefletcher.tbaapi.v3client.Configuration()
        self.configuration.api_key['X-TBA-Auth-Key'] = settings.TBA_AUTH_KEY

        super().__init__(net.thefletcher.tbaapi.v3client.ApiClient(self.configuration))

    @chc(timeout=15)
    def status(self):
        resp = self.get_status()
        return not resp.to_dict()

    def ping(self):
        """ Make sure api is alive """
        resp = self.get_status()
        return not resp.is_datafeed_down

    @property
    def cache_version(self):
        return self.c.get_or_set(self.cache_name('cache_version'), default=1)

    @cache_version.setter
    def cache_version(self, value):
        return self.c.set(self.cache_name('cache_version'), int(value))

    def cache_name(self, base, *args, **kwargs):
        return '_'.join([
            self.c_prefix,
            base,
            '-'.join(args),
            '-'.join(["%r=%r" % (k, kwargs[k]) for k in sorted(kwargs)]),
        ])
