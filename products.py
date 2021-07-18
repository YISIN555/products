import os  #operating system #標準函式庫


#讀取檔案
products = [] 
if os.path.isfile('products.csv'): # 相對路徑 #isfile 檢查檔案在不在
	print('有')
	with open ('products.csv', 'r', encoding= 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('沒有')

#讓使用者輸入
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

#印出所有購買紀錄
for p in products:
	print(p) #印出小清單
	print(p[0], '的價格是', p[1])


#寫入檔案
with open ('products.csv', 'w', encoding= 'utf-8' )as f: #打開
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #寫入



