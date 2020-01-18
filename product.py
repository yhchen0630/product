products = []
#讀取資料
with open('products.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue #跳過"繼續執行line"
        name, price = line.strip().split(',')
        products.append([name, price])

print(products)



while True:
    name = input('請輸入您的商品名稱：')
    if name == 'q':
        break
    price = input('請輸入您的商品價格：')
    price = int(price)
    p = []
    p.append(name)
    p.append(price) #簡化(7-9行)版 p = [name, price]
    products.append(p)#簡化(7-10行)版 products.append([name,price])
print(products)

for product in products:
    #print(product)
    print(product[0],'的價格為', product[1])

with open('products.csv','w',encoding = 'utf-8' ) as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')