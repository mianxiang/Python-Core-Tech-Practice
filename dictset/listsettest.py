import time
#list version
def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)

def build_products():
    id = [x for x in range(0, 100000)]
    price = [x for x in range(200000, 300000)]
    return list(zip(id, price))

products = build_products()

start_using_list = time.perf_counter()
print('number of unique price is:{} using list'.format(find_unique_price_using_list(products)))
end_using_list = time.perf_counter()
print("time elapse using list:{}".format(end_using_list - start_using_list))

start_using_set = time.perf_counter()
print('number of unique price is:{} using set'.format(find_unique_price_using_set(products)))
end_using_set = time.perf_counter()
print("time elapse using set:{}".format(end_using_set - start_using_set))