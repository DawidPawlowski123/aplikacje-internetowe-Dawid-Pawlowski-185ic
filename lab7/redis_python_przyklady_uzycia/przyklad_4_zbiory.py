from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("key",2) #sadd dodawanie do zbioru
redis_connection.sadd("key",1)
redis_connection.sadd("key",3)

redis_connection.sadd("key2",3)
redis_connection.sadd("key2",3)
redis_connection.sadd("key2",3)

print(redis_connection.smembers("key")) #smembers pobieranie z zbioru  element�w w r�znej kolejnosci  

