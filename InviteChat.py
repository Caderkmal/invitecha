import pyfiglet
from configs import menu_configs, invite_functions
from tabulate import tabulate
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_CORAL + style.BOLD)
print("""Script by Carson
Github : """)
print(pyfiglet.figlet_format("InviteChat", font="rectangles"))
print(tabulate(menu_configs.main_menu, tablefmt="psql"))
select = input("Select >> ")

if select == "1":
	دعوة الاعضاء الأونلاين

elif select == "2":
	دعوة الاعضاء الجدد

elif select == "3":
	دعوة الاعضاء من المتابعين