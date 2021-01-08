from redis import Redis
from json import dumps
redis_connection = Redis(decode_responses=True, db=0)


script ="""
return "test"
"""

print(redis_connection.eval(script,0))#eval przekazanie skryptu napisanego w LUA, 0 okre�la ilo�� argument�w
                                        #indeksowanie tabel od 1 

script2 ="""
return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}
"""

print(redis_connection.eval(script2,2,1,2,'first','second'))


script3 ="""
local arr = {}
for i = 0, 10 do
    arr[i] = i
end
return arr
"""

print(redis_connection.eval(script3,0))# lista od 1 do 10

script4 ="""
local json_data = KEYS[1]
local decoded_data = cjson.decode(json_data)
return decoded_data['a'] + decoded_data['b']
"""

print(redis_connection.eval(script4,1, dumps({'a': 1,'b': 6})))  # wynik to 7

redis_connection.set("key1",10)
script5 ="""
local arg1 = redis.call('get','key1')
redis.call('set', 'key2', arg1 + KEYS[1])
return nil
"""

print(redis_connection.eval(script5,1,5))  # None, ze wzgl�du na "return nil"
print(redis_connection.get("key2"))  # 15, bo 10 + 5 = 15 ;)



permission ='ADD_BOOKING'

redis_connection.sadd("users_group:2", *list(range(0,50)))

redis_connection.sadd('permissions', permission)

# dot�d jest przygotowanie danych

add_permission_script ="""
local is_valid_permission = redis.call('sismember', 'permissions', KEYS[2])
if is_valid_permission == 1 then
    local users = redis.call('smembers','users_group:'..KEYS[1])
    for _, user in ipairs(users) do
        redis.call('sadd', 'user_permissions:'..user, KEYS[2])
    end
    return true
else
    return false
end
"""


print(redis_connection.eval(add_permission_script,2,2, permission))

sha= redis_connection.script_load(add_permission_script)
print(redis_connection.evalsha(sha,2,2, permission))