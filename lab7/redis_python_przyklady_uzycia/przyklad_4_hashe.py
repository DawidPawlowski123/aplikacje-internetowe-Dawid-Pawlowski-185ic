# Hashe struktura danych przechowuj¹ca klucze i odpowiadaj¹ce im wartoœci.
from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='test_hash' # pod kluczem test_hash tworzymy s³ownik który ma jeden klucz key o wartosci value

redis_connection.hset(hash_key,'key','value')

print(redis_connection.hgetall(hash_key)) #hgetall pobiera wszytkie elementy

#HKEYS – zwraca wszystkie klucze s³ownika
#HVALS – analogicznie jak wy¿ej, zwraca wszystkie wartoœci
#HEXISTS – sprawdza czy dany klucz istnieje w s³owniku