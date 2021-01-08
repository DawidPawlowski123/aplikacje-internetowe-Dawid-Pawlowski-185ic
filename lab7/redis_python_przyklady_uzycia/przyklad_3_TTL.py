from redis import Redis
from time import sleep
from datetime import datetime

redis_connection = Redis(decode_responses=True)

redis_connection.setex("key",10,"value") # d�ugo�� �ycia klucza to 10s wartosc value
                                        #setex jest skr�tem od SET i EXPIRE ustawia TTL
#redis_connection.set("key","value") alternatywny zapis zamiast setex efekt ten sam
#redis_connection.expire("key",30) 
print(datetime.now().time(), redis_connection.get("key"))
sleep(5)
print(datetime.now().time(), redis_connection.get("key"))
sleep(10)
print(datetime.now().time(), redis_connection.get("key")) #wartosc nie osiagalna up�ynol czas �ycia 