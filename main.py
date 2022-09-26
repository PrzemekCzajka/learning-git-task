#Zadanie 3 1 1 - Dołączam do zadania z Gita

shop_list = {'warzywniak': ['jabłka', 'cebula', 'ziemniaki'],  
                'mięsny': ['kiełbasa', 'wołowina']}

x = 0
x = (len(shop_list['warzywniak'])) + (len(shop_list['mięsny']))

print("Lista zakupów")
for (a, b) in shop_list.items():
    len(a)
    a = a.capitalize()
    b = " ".join(b)
    b = b.title()
    print("Idę do", a, "i kupuję tam", b)
print("W sumie kupuję", x, "produktów.")

#A na końcu jeszcze jedno zdanie dla dodatkowego commita