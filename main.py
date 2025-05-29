"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-19001.c336.samerica-east1-1.gce.redns.redis-cloud.com',
    port=19001,
    decode_responses=True,
    username="default",
    password="CkZcXjVN8EpjIWmJEt0IrhoT2xNWSGCP",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar