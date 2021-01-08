from redis import Redis

redis_connection = Redis(decode_responses=True)  # decode_responses=True dzieki temu otrzymujemy string,
											#lub inne typy danych w przeciwnym wypadku otrzymamy ciag bajtów

imie ="Dawid" 
nazwisko ="Pawlowski"

redis_connection.set(imie,"Pawel ")
redis_connection.append(imie,imie)
print(redis_connection.get(imie))
redis_connection.set(nazwisko,nazwisko)
print(redis_connection.get(nazwisko))

a =10
b =20
wartosc =""
wyrazenie =""

#wyrazenie
redis_connection.set(wyrazenie, a)
redis_connection.append(wyrazenie," + ")
redis_connection.append(wyrazenie,b)
redis_connection.append(wyrazenie," = ")

print(redis_connection.get(wyrazenie))
#dodawanie
redis_connection.set(wartosc, a)
redis_connection.incr(wartosc,b)

print(redis_connection.get(wartosc))
#odejmowanie
redis_connection.set(wartosc,30)
print(redis_connection.decr(wartosc,b))




