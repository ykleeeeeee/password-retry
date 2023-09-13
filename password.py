password = 'a123456'
i = 3
while True:
    pwd = input('請輸入密碼:')          #存入的字串名稱不能與上line1的password重複
    if pwd == password:
        print('登入成功')
        break                 #逃出迴圈
    else:
    	i = i - 1 
    	print('密碼錯誤!  還有', i,'次機會')
    	if i == 0 :
    		break

