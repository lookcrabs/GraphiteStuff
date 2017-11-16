SECRET_KEY = '<SECRET>'
TIME_ZONE = 'America/Chicago'
DOCUMENTATION_URL = "http://graphite.readthedocs.io/"
LOG_ROTATION = True
LOG_ROTATION_COUNT = 1
LOG_RENDERING_PERFORMANCE = True
LOG_CACHE_PERFORMANCE = True
DEBUG = True
MEMCACHE_HOSTS = [ '123.456.789.012:8543', '234.567.890.123:8543', '345.678.901.234:8543', '456.789.012.345:11211' ]
DEFAULT_CACHE_DURATION = 600 # Cache images and data for 1 minute
DEFAULT_CACHE_POLICY = [(0, 600), # default is 60 seconds
                        (7200, 1200), # >= 2 hour queries are cached 2 minutes
                        (21600, 1800)] # >= 6 hour queries are cached 3 minutes
MEMCACHE_KEY_PREFIX = 'graphite'
MAX_TAG_LENGTH = 255
AUTO_REFRESH_INTERVAL = 60
GRAPHITE_ROOT = '/var/lib/graphite'
CONF_DIR = '/etc/graphite'
STORAGE_DIR = '/var/lib/graphite/storage/'
STATIC_ROOT = '/var/lib/graphite/webapp/static'
LOG_DIR = '/var/log/graphite/'
INDEX_FILE = '/var/lib/graphite/storage/index'     # Search index file
DASHBOARD_CONF = '/etc/graphite/dashboard.conf'
WHISPER_DIR = '/var/lib/graphite/storage/whisper'
RRD_DIR = '/var/lib/graphite/storage/rrd'
STANDARD_DIRS = [WHISPER_DIR, RRD_DIR] # Default: set from the above variables
DATABASES = {
    'default': {
        'NAME': 'graphite',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'graphiteadmin',
        'PASSWORD': '<PASSWORD>',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET storage_engine=MyISAM"
            },
    }
}
CLUSTER_SERVERS = [ '123.456.789.012:8543', '234.567.890.123:8543', '345.678.890.123:8543', '456.789.012.345:8543' ]
REMOTE_STORE_MERGE_RESULTS = True
CARBON_METRIC_PREFIX='carbon'
REPLICATION_FACTOR = 1
