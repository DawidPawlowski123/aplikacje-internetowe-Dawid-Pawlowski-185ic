from redis import Redis

redis_connection = Redis(decode_responses=True)

pubsub = redis_connection.pubsub()
pubsub.psubscribe("tasks_*")

for message in pubsub.listen(): #czeka na odpowiedz
    print(message)