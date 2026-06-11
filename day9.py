# ДЕНЬ 9 работа со словарями данных

print("КАРТОЧКА исследуемого сервера")

# 1. Создаем словарь с подробной информацией о цели
server_info = {
	"ip": "10.1.1.5",
	"os": "Linux kali",
	"vuln_count": 3
}
# Достаем текстовые данные по ихним ключам
print("[Target ip]:" + server_info["ip"])
print("[Os version]:" + server_info["os"])

print("[VULNERABILITIES]:" + str(server_info["vuln_count"]))

print("СКАНЕР обнаружил открытый порт на сервере")
server_info["status"] = "Уязвим"
# Проверяем появился ли новый ключ
print("[CURRENT STATUS]" + str(server_info) + str(["status"]))
