x = 1
shop_list = ['nestomalt', 'milk', 'beet', 'green leaves', 'bitter gourd']
for i in shop_list:
    print(x,i)
    x = x + 1

shop_list = ['nestomalt', 'milk', 'beet', 'green leaves', 'bitter gourd']
length = len(shop_list)
for i in range(0, length):
    print(f'{i + 1}. {shop_list[i]}')