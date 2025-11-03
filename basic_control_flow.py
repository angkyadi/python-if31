def is_active(is_active : bool):
    if is_active:
        print("system Aktif")
    else:
        print("System Tidak Aktif")

def number_to_alphabet(value : int):
    if value > 90:
        print("A")
    elif value > 80:
        print("B")
    else :
        print("C")


is_active(False)
number_to_alphabet(90)