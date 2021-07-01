import os
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')
# end def

clearconsole()
print("CAFE AU LAIT – ORDER MANAGEMENT SYSTEM")
print("--------------------------------------")
print()
# print("Choose Mode [T]est / [I]NTERACTIVE [Default]: ")
mode = input("Choose Mode [T]est / [I]NTERACTIVE [Default]: ")
print()
action = input("[D]aily Summary / New [O]rder [Default]: ")


# Process a new order
clearconsole()
print("CAFE AU LAIT – ORDER MANAGEMENT SYSTEM")
print("--------------------------------------")
print("MODE:   INTERACTIVE")
print("ACTION: NEW ORDER")
print()
print()
print("NEW ORDER #: 1")
print("-----------")
print()
print("ORDER TYPE:")
print("-----------")
print()
print("[D]ine-In")
print("[T]ake-Away")
print()
print("[E]xit Ordering")
print()
orderType = input("Choice: ")



