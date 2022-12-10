from taobin_machine import TaobinMachine
from account_taobin import Account

main_machine = TaobinMachine()


print("""============================================
======-WELCOME TO THE TAOBIN MACHINE!-======
v                                          v
v                    )))                   v
v                   (((                    v
v                 +-----+                  v
v                 | :)  |]                 v
v                 `-----'                  v
v                                          v
============================================
 Please order your drink and enjoy you drink 
v           as much as you can!.           v
v        -------------------------         v
v          And here is your menu!          v
v        -------------------------         v
============================================""")
print("""====== >> ====== Menu Drink ====== << ======

             1. latte (฿ 35)
             2. espresso (฿ 25)
             3. cappuccino (฿ 40)
             4. black coffee (฿ 30)
             5. black tea (฿ 35)
             6. milk tea (฿ 35)
             7. dark cocoa (฿ 35)
             8. cocoa milk (฿ 35)
               """)

choice = input("""============================================\nDid you want to turn off the machine?: """)
if choice == "off":
    exit()
name = input("What is your name, sir : ")
main_account = Account(name)

main_machine.order_drink()
main_account.username(main_account)
for i in main_machine.total:
 main_account.menu(main_account.name, i)


def report():
    print(f"""Sale:{main_machine.sales} Drinks
Final Revenue: {main_machine.price} Baht and please enjoy your drink!""")


print("============================================\nList of Successful Drinks: ")
for i in range(len(main_machine.total)):
  print(f"{i + 1}. {main_machine.total[i].name}: {main_machine.total[i].cost} Baht")
