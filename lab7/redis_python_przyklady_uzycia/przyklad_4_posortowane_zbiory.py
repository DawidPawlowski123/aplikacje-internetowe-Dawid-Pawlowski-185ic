from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("sorted_set_key",{"key1": 1})#zadd dodawanie do zbioru oraz waga element�w oznacza kolejno�� przy wypisywaniu
redis_connection.zadd("sorted_set_key",{"key2": 2})#jesli wagi takie same to sortowane alfabetycznie
redis_connection.zadd("sorted_set_key",{"key3": 3})
redis_connection.zadd("sorted_set_key",{"key4": 4})

print(redis_connection.zrange("sorted_set_key",0, -1,withscores=True))#zrange pobieranie z zbioru  element�w w r�znej kolejnosci  
												#ZPOPMAX ZPOPMIN  element najwiekszy lub najmniejszy 
												#withscores=True dodajemy ze wy�wietla wartosc klucza