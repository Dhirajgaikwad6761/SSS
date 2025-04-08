import multiprocessing

# Number of worker processes
workers = 1  # Use only 1 worker for free tier
worker_class = 'eventlet'  # Use eventlet for WebSocket support
threads = 2  # Number of threads per worker

# Timeouts
timeout = 120  # Increase timeout to 120 seconds
graceful_timeout = 30
keepalive = 5

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Worker configurations
max_requests = 1000  # Restart workers after handling 1000 requests
max_requests_jitter = 50  # Add jitter to avoid all workers restarting at once
worker_connections = 1000  # Maximum number of simultaneous connections

# Process naming
proc_name = 'student_support_system'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL
keyfile = None
certfile = None 