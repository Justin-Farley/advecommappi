from flask_limiter import Limiter

limiter = Limiter(
    key_func=lambda: 'global',
    default_limits=["100 per day"]
)
