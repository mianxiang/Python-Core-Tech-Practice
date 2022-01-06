import json

params = {
    'symbol':'123456',
    'type':'limit',
    'price':123.59,
    'amount':23
}

params_str = json.dumps(params)

print('after json serializaiton')
print('type of params_str = {}, params_str = {}'.format(type(params_str), params_str))

original_params = json.loads(params_str)
print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))