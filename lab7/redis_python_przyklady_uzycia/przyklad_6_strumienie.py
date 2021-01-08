from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

stream_name ='testowy_strumien'

redis_connection.xadd(stream_name,{'testowy_klucz': 'testowa_wartosc'}) # dodanie do strumienia s�ownika
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1) #odczytanie element�w na podstawie
																		# ilo�ci count, block ustala na ile ms 
																		#ma byc blokowane dzieki temu mozna urzywa�
																		#w petli, nazwa to s�ownik z kluczem oraz
																		#id z kt�ego startuje
print(message)


