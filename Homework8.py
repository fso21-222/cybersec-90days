bad_password = ["123","222","111","321"]
for bad in bad_password:
	print("Опасный пароль:" + str(bad))



critical_ports = ["22","80","443","3389","8080"]
for ports in critical_ports:
	if ports == "22" or  ports == "3389":
		print ("Опасный порт:" + ports + "открыт!")
	else:
		print ("Порт в безопасном режиме:" + ports)		
