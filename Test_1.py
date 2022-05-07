products = []
while True:
    name = input('请输入商品名称：')
    if name == 'q':
        break
    price = input('请输入价格：')
    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]#简洁写法
    # products.append(p)
    products.append([name, price])  # 最最简洁的写法！
print(products)

for p in products:
    print(p[0], '的价格是', p[1])
