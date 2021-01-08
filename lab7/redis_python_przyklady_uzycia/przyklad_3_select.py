from redis import Redis

redis_connection = Redis(decode_responses=True) # pierwsza przestrzen baza 0

redis_connection.set("key","value")

redis_connection_1 = Redis(decode_responses=True, db=1) #db=1 jedna z baz jest ich 16 od 0 do 15, druga przestrzen

redis_connection_2 = Redis(decode_responses=True, db=2) 

redis_connection_2.set("key","value3") #modyfikacja dodanie bazy nr3

print(redis_connection_2.get("key"))

print(redis_connection_1.get("key")) #wynik none poniewaz wartosc key jest na bazie nr0

print(redis_connection.get("key"))
