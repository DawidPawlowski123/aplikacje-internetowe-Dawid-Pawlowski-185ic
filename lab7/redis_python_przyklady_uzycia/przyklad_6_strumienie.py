from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

stream_name ='testowy_strumien'

redis_connection.xadd(stream_name,{'testowy_klucz': 'testowa_wartosc'}) # dodanie do strumienia s³ownika
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1) #odczytanie elementów na podstawie
																		# iloœci count, block ustala na ile ms 
																		#ma byc blokowane dzieki temu mozna urzywaæ
																		#w petli, nazwa to s³ownik z kluczem oraz
																		#id z któego startuje
print(message)


