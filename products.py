products = [] 
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	# p = []
	# p.append(name)
	# p.append(price)
	products.append([name, price])  #等於7~8行
print(products) #印出大清單

products[0][0]


for p in products:
	print(p) #印出小清單
	print(p[0], '的價格是', p[1])