
def verificar_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "VLAN del rango normal"
    elif 1006 <= vlan_id <= 4094:
        return "VLAN del rango extendido"
    else:
        return "VLAN fuera del rango permitido"

if __name__ == "__main__":
    try:
        vlan_id = int(input("Ingrese el número de VLAN: "))
        resultado = verificar_vlan(vlan_id)
        print(resultado)
    except ValueError:
        print("Por favor, ingrese un número válido.")
