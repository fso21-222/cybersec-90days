system = input("ВВЕДИТЕ пароль:")
if system == "Hak239":
	print("С возращением!")
else:
	print("Ошибка: попытка несанкционированного входа.")



ip_adress = int(input("Первое число Ip-adress:"))
if ip_adress == 192:
	print("[NETWORK] Это адрес локальной сети.")
else:
	print("[NETWORK] Это внешний адрес из интернета")	




summa = int(input("Напишите любое целое число:"))
summa1 = summa % 2
if summa1 == 0:
	print ("ВЫ ввели ЧЕТНОЕ число")
else:
	print ("ВЫ ввели НЕЧЕТНОЕ число")
		



