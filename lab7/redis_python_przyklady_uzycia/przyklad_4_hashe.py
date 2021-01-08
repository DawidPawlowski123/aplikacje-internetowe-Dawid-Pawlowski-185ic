# Hashe struktura danych przechowuj�ca klucze i odpowiadaj�ce im warto�ci.
from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='test_hash' # pod kluczem test_hash tworzymy s�ownik kt�ry ma jeden klucz key o wartosci value

redis_connection.hset(hash_key,'key','value')

print(redis_connection.hgetall(hash_key)) #hgetall pobiera wszytkie elementy

#HKEYS � zwraca wszystkie klucze s�ownika
#HVALS � analogicznie jak wy�ej, zwraca wszystkie warto�ci
#HEXISTS � sprawdza czy dany klucz istnieje w s�owniku