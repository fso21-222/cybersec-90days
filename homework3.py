dop_ports =  int(input ("Сколько еще дополнительных портов ты хочешь проверить:"))
base_ports = 1024
dop_ports = dop_ports + base_ports
print ( "ВСЕГО ПОРТОВ:" + str( dop_ports ) )



fix = int(input ("Скорость работы взломщика:"))
fix_1 = 100000
fix_3 = fix_1/fix
print ("[INFO]")
print ("На полный перебор уйдет:"+ str( fix_3))




summa = int(input("Напишите любое целое число:"))
summa1 = summa % 2
print ("Остаток:"+ str(summa1))
