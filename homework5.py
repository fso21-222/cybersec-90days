def check_pwn(attempts):
	attempts = int(input("Введите число:"))
	if attempts >= 5:
		print ("Предупреждение о блокировки аккаунта")
	else:
		print ("Попытка номер:" + str( attempts) + ":Осталось до блокировки:" +  str( 5 - attempts)) 
check_pwn(5)			




def welcome_user(name):
	print("[Авторизация прошла успешна. Приветствуем в системе,]" + name)
welcome_user("Max")
welcome_user("Oleg")	




def verify_number(num):
 	num1 = num % 2
 	if num1 == 1:
 		print ("Число нечетное")
 	else:
 		print ("Число четное")	
num2 = int(input("Введите целое число:"))
verify_number(num2)
num5 = int(input("Введите целое число:"))		
verify_number( num5 )
