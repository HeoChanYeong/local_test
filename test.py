print('가계부 프로그램에 오신 것을 환영합니다')
print('='*45)
print()
money_list = []
cmd_list = []
price_list = []
while True : 
    cmd =input('명령을 입력하세요 (1=내역입력, 2=결과출력, 3=종료)) : ')
    cmd_list.append(cmd)
    #print(cmd_list)    
    if cmd_list[-1] == '1':        
        item  = input('지출 항목을 입력하세요 : ')
        money = int(input('지출 금액을 입력하세요 : '))
        money_list.append(item)
        price_list.append(money)
        
    elif cmd_list[-1] == '2':
        total=0
        print('지출 항목 리스트입니다')
        for i in range(len(money_list)):
            print(f'{money_list[i]} {price_list[i]}원')
            total += price_list[i]
        else:   
            print(f'지출 총 금액은 {total}원 입니다')
    elif cmd_list[-1] == '3':
        break
    else :
        print('잘못된 입력입니다')
        continue
    
    print()

print('프로그램을 종료합니다')
