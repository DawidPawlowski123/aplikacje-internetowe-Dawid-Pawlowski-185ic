from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="example-list"

redis_connection.rpush(list_key,1,2,3,4,5) #rpush, lpush dodawanie do listy z prawej i lewej striony
print(redis_connection.lrange(list_key,0, -1)) #lrange pobranie wartosci z listy i okreœlenie przedia³u
                                                #od 0 do -1 to ca³a lista 
while True:
    print(redis_connection.brpop(list_key)) #brpop blokowanie programu po pobraniu ostatniego elementu z 
                                            #listy przez pêtle while bez petli poberze ostatni element i zablokuje