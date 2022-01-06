import json

params = {
    'symbol': '12345',
    'type': 'limit',
    'price': 123.56,
    'amount': 45
}

with open('param.json', 'w') as fout:
    json.dump(params, fout)

with open('param.json', 'r') as fin:
    original_params = json.load(fin)

print('after deserialzation')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))