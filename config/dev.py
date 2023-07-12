daemon = False
chdir = '/home/ubuntu/panoptes/panoptes'
bind = '0.0.0.0:6000'
timeout = 0
preload = False
workers = 3 * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
loglevel = 'debug'
accesslog = 'access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = 'error.log'
