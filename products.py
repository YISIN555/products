import os  #operating system #標準函式庫


#讀取檔案
def read_file(filename):
	products = [] 
	with open (filename, 'r', encoding= 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

	

#讓使用者輸入
def user_input(products):
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
	return products


#印出所有購買紀錄
def print_products(products):	
	for p in products:
		print(p) #印出小清單
		print(p[0], '的價格是', p[1])


#寫入檔案
def write_file(filename, products):
	with open (filename, 'w', encoding= 'utf-8' )as f: #打開
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #寫入



def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 相對路徑 #isfile 檢查檔案在不在
		print('有')
		products = read_file(filename)	
	else:
		print('沒有')
		



	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()