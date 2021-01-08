from redis import Redis

redis_connection = Redis(decode_responses=True)  # <- tu zmiana!

key ="some-key"
value ="some-val"

redis_connection.set(key, value)
print(redis_connection.get(key))