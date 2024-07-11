from math import radians, cos, sin, sqrt, atan2

# Coordenadas de una ciudad de Chile y una de Argentina
ciudades = {
    "Santiago": (-33.4489, -70.6693),
    "Buenos Aires": (-34.6037, -58.3816),
}

def calcular_distancia(coord1, coord2):
    R = 6371.0  # Radio de la Tierra en km
    
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distancia_km = R * c
    distancia_millas = distancia_km * 0.621371
    return distancia_km, distancia_millas

def obtener_distancia_duracion(origen, destino, transporte):
    coord_origen = ciudades.get(origen)
    coord_destino = ciudades.get(destino)
    
    if not coord_origen or not coord_destino:
        raise ValueError("Ciudad no encontrada en la base de datos")
    
    distancia_km, distancia_millas = calcular_distancia(coord_origen, coord_destino)
    
    if transporte == "auto":
        velocidad_kmh = 100
    elif transporte == "avion":
        velocidad_kmh = 800
    else:
        velocidad_kmh = 50
    
    duracion_horas = distancia_km / velocidad_kmh
    
    return distancia_km, distancia_millas, duracion_horas

# Función principal
def main():
    while True:
        print("\nBienvenido al calculador de distancias entre ciudades.")
        origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ")
        if origen.lower() == 's':
            break
        
        destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ")
        if destino.lower() == 's':
            break
        
        print("\nSeleccione el medio de transporte:")
        print("1. Auto")
        print("2. Avión")
        print("3. Bicicleta")
        
        opcion = input("Ingrese el número de la opción (o 's' para salir): ")
        if opcion.lower() == 's':
            break
        
        if opcion == "1":
            transporte = "auto"
        elif opcion == "2":
            transporte = "avion"
        elif opcion == "3":
            transporte = "bicicleta"
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            continue
        
        try:
            distancia_km, distancia_millas, duracion_horas = obtener_distancia_duracion(origen, destino, transporte)
            
            print(f"\nLa distancia entre {origen} y {destino} es de:")
            print(f"{distancia_km:.2f} kilómetros")
            print(f"{distancia_millas:.2f} millas")
            print(f"La duración del viaje es aproximadamente {duracion_horas:.2f} horas en {transporte}.")
            
            print(f"\nNarrativa del viaje:")
            print(f"Si viaja desde {origen} hasta {destino} en {transporte}, recorrerá aproximadamente {distancia_km:.2f} kilómetros o {distancia_millas:.2f} millas.")
            print(f"El viaje tomará alrededor de {duracion_horas:.2f} horas, dependiendo de las condiciones del tráfico y otros factores.\n")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
