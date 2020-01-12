products = []
while True:
    name = input('請輸入您的商品名稱：')
    if name == 'q':
        break
    price = input('請輸入您的商品價格：')
    p = []
    p.append(name)
    p.append(price) #簡化(7-9行)版 p = [name, price]
    products.append(p)#簡化(7-10行)版 products.append([name,price])
print(products)


