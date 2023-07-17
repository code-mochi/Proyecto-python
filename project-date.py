origen = [
    {
        "pais_origen": "Brasil",
        "valor_vuelo": 241524
    },
    {
        "pais_origen": "Argentina",
        "valor_vuelo": 72900
    },
    {
        "pais_origen": "España",
        "valor_vuelo": 823322
    },
    {
        "pais_origen": "EE.UU",
        "valor_vuelo": 554568
    },
    {
        "pais_origen": "Francia",
        "valor_vuelo": 976864
    },
    {
        "pais_origen": "Israel",
        "valor_vuelo": 1145922
    },
    {
        "pais_origen": "Mexico",
        "valor_vuelo": 459085
    },
    {
        "pais_origen": "Rusia",
        "valor_vuelo": 1463242
    },
    {
        "pais_origen": "Suecia",
        "valor_vuelo": 1094232
    },
    {
        "pais_origen": "Italia",
        "valor_vuelo": 1051508
    }
]

destino = [
    {
        "zona_pais": "Norte Grande",
        "region_1": "Arica y Parinacota"
    },
    {
        "zona_pais": "Norte Grande",
        "region_2": "Tarapacá"
    },
    {
        "zona_pais": "Norte Grande",
        "region_3": "Antofagasta"
    },
    {
        "zona_pais": "Norte Grande",
        "region_4": "Atacama"
    },
    {
        "zona_pais": "Norte Grande",
        "region_5": "Coquimbo"
    },
    {
        "zona_pais": "Zona Central",
        "region_6": "Valparaíso"
    },
    {
        "zona_pais": "Zona Central",
        "region_7": "Metropolitana"
    },
    {
        "zona_pais": "Zona Central",
        "region_8": "O'Higgins"
    },
    {
        "zona_pais": "Zona Central",
        "region_9": "Maule"
    },
    {
        "zona_pais": "Zona Central",
        "region_10": "Biobío"
    },
    {
        "zona_pais": "Zona Sur",
        "region_11": "Araucanía"
    },
    {
        "zona_pais": "Zona Sur",
        "region_12": "Biobío"
    },
    {
        "zona_pais": "Zona Sur",
        "region_13": "Los Lagos"
    },
    {
        "zona_pais": "Zona Sur",
        "region_14": "Los Ríos"
    },
    {
        "zona_pais": "Zona Austral",
        "region_15": "Aysén"
    }
]

fecha_viaje = None

def obtener_fecha_viaje():
    global fecha_viaje
    fecha_viaje = input("Ingrese la fecha para realizar el viaje (DD/MM/AAAA): ")

def obtener_origen(origen):
    opc = int(input(f"""
    Lista de Origen:
    1. {origen[0]["pais_origen"]}
    2. {origen[1]["pais_origen"]}
    3. {origen[2]["pais_origen"]}
    4. {origen[3]["pais_origen"]}
    5. {origen[4]["pais_origen"]}
    6. {origen[5]["pais_origen"]}
    7. {origen[6]["pais_origen"]}
    8. {origen[7]["pais_origen"]}
    9. {origen[8]["pais_origen"]}
    10. {origen[9]["pais_origen"]}
    Seleccione la Opción:
    """))

    if opc in range(1, len(origen) + 1):
        pais_origen = origen[opc - 1]["pais_origen"]
        valor_vuelo = origen[opc - 1]["valor_vuelo"]
        cantidad_personas = int(input("Ingresar cantidad de personas: "))
        total_vuelo = valor_vuelo * cantidad_personas
        print(f"País de origen seleccionado: {pais_origen}")
        print(f"Fecha para realizar el viaje: {fecha_viaje}")
        print(f"Total de pasajes: {total_vuelo}")

        return total_vuelo, cantidad_personas
    else:
        print("No ha ingresado un origen válido.")
        return None, None


def obtener_destino(destino):
    opc = int(input(f"""
    Lista de Destinos:
    1. {destino[0]["region_1"]}
    2. {destino[1]["region_2"]}
    3. {destino[2]["region_3"]}
    4. {destino[3]["region_4"]}
    5. {destino[4]["region_5"]}
    6. {destino[5]["region_6"]}
    7. {destino[6]["region_7"]}
    8. {destino[7]["region_8"]}
    9. {destino[8]["region_9"]}
    10. {destino[9]["region_10"]}
    11. {destino[10]["region_11"]}
    12. {destino[11]["region_12"]}
    13. {destino[12]["region_13"]}
    14. {destino[13]["region_14"]}
    15. {destino[14]["region_15"]}
    Seleccione la Opción:
    """))

    if opc in range(1, len(destino) + 1):
        region_destino = destino[opc - 1]["zona_pais"]
        print(f"Destino seleccionado: {region_destino}")
        return region_destino
    else:
        print("No ha ingresado un destino válido.")
        return None


def obtener_transporte(total_anterior=0, opciones_elegidas=[]):
    terrestre = [
        {
            'nombre': 'Transfer',
            'valor': 12000,
            'tipo': 'terrestre',
            'capacidad': 20
        },
        {
            'nombre': 'Rent a Car',
            'valor': 10000,
            'tipo': 'terrestre',
            'capacidad': 5
        },
        {
            'nombre': 'Bicicleta',
            'valor': 5000,
            'tipo': 'terrestre',
            'capacidad': 1
        }
    ]

    maritimo = [
        {
            'nombre': 'Transbordador',
            'valor': 8000,
            'tipo': 'maritimo',
            'capacidad': 100
        }
    ]

    aereo = [
        {
            'nombre': 'Avion',
            'valor': 70000,
            'tipo': 'aereo',
            'capacidad': 100
        }
    ]

    print("             MENU DE TRANSPORTES              ")
    print("----------------------------------------------")
    print("1. Nombre Transporte: ", terrestre[0]['nombre'])
    print("   Valor por Persona: ", terrestre[0]['valor'])
    print("   Capacidad:         ", terrestre[0]['capacidad'])
    print("----------------------------------------------")
    print("2. Nombre Transporte: ", terrestre[1]['nombre'])
    print("   Valor por Persona: ", terrestre[1]['valor'])
    print("   Capacidad:         ", terrestre[1]['capacidad'])
    print("----------------------------------------------")
    print("3. Nombre Transporte: ", terrestre[2]['nombre'])
    print("   Valor por Persona: ", terrestre[2]['valor'])
    print("   Capacidad:         ", terrestre[2]['capacidad'])
    print("----------------------------------------------")
    print("4. Nombre Transporte: ", maritimo[0]['nombre'])
    print("   Valor por Persona: ", maritimo[0]['valor'])
    print("   Capacidad:         ", maritimo[0]['capacidad'])
    print("----------------------------------------------")
    print("5. Nombre Transporte: ", aereo[0]['nombre'])
    print("   Valor por Persona: ", aereo[0]['valor'])
    print("   Capacidad:         ", aereo[0]['capacidad'])
    print("---------------------------------------------")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        seleccion = terrestre[0]
    elif opcion == 2:
        seleccion = terrestre[1]
    elif opcion == 3:
        seleccion = terrestre[2]
    elif opcion == 4:
        seleccion = maritimo[0]
    elif opcion == 5:
        seleccion = aereo[0]
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
        exit()

    cantidad_personas = int(input("Ingrese la cantidad de personas: "))
    subtotal = seleccion['valor'] * cantidad_personas
    total = total_anterior + subtotal
    opciones_elegidas.append({
        'nombre': seleccion['nombre'],
        'cantidad_personas': cantidad_personas,
        'valor_transporte': seleccion['valor'],
        'subtotal': subtotal
    })

    print()
    print("Has seleccionado:    ", seleccion['nombre'])
    print("Cantidad de personas:", cantidad_personas)
    print("Valor del transporte:", seleccion['valor'])
    print("Subtotal a pagar:    ", subtotal)
    print("Total acumulado:     ", total)

    opcion = input("¿Deseas usar otro transporte? (Sí/No): ")

    if opcion.lower() == "sí" or opcion.lower() == "si":
        return obtener_transporte(total, opciones_elegidas)
    else:
        print("Has finalizado con Transporte")
        print("-----------------------------------------------")
        print("Opciones elegidas:")
        for opcion in opciones_elegidas:
            print("----------------------------------------------")
            print("Nombre Transporte:    ", opcion['nombre'])
            print("Cantidad de personas: ", opcion['cantidad_personas'])
            print("Valor del transporte: ", opcion['valor_transporte'])
            print("Subtotal:             ", opcion['subtotal'])
        print("----------------------------------------------")
        print("Total acumulado:     ", total)
        return total, opciones_elegidas


def aplicar_descuentos(cantidad_personas, total_vuelo):
    descuento = 0

    edad_valida = False
    while not edad_valida:
        edad = input("Ingrese su edad: ")
        try:
            edad = int(edad)
            edad_valida = True
        except ValueError:
            print("Ingrese una edad válida.")

    if 2 <= edad < 11:
        descuento = 0.10
    elif 11 <= edad <= 59:
        descuento = 0
    elif 60 <= edad:
        descuento = 0.30

    if cantidad_personas >= 20:
        descuento += 0.05

    total_con_descuento = total_vuelo - (total_vuelo * descuento)
    print(f"\nDescuento aplicado: {descuento * 100}%")
    print(f"Total con descuento: {total_con_descuento} CLP")

    discapacidad = input("¿Tiene alguna discapacidad? (S/N): ")
    if discapacidad.upper() == "S":
        descuento_discapacidad = 0.80
        total_con_descuento_discapacidad = total_con_descuento - (total_con_descuento * descuento_discapacidad)
        print(f"\nDescuento por discapacidad aplicado: {descuento_discapacidad * 100}%")
        print(f"Total con descuento por discapacidad: {total_con_descuento_discapacidad} CLP")

def seleccionar_menu(zona):
    if zona == "Zona Norte":
        menu = [
    { "Menú": "Ceviche de pescado",
    "valor_menu": 5990
    },
    {"Menú": "Locro de papas",
    "valor_menu": 7990
    },
    {"Menú": "Seco de cordero",
    "valor_menu": 7990
    },
    {"Menú": "Pollo Asado con Papas fritas",
    "valor_menu": 7990
    },
    {"Menú": "Chupe de Jaiba",
    "valor_menu": 7990
    },
    {"Menú": "Arroz con Asado",
    "valor_menu": 7990
    },
    {"Menú": "Pescado con Ensalada",
    "valor_menu": 7990
    }]
        
    elif zona == "Zona Central":
        menu = [
    { "Menú": "Porotos con riendas",
    "valor_menu": 5990
    },
    {"Menú": "Pescado frito",
    "valor_menu": 7990
    },
    {"Menú": "Pastel de choclo",
    "valor_menu": 7990
    },
    {"Menú": "Cazuela de vacuno",
    "valor_menu": 7990
    },
    {"Menú": "Asado a la parrilla",
    "valor_menu": 7990
    },
    {"Menú": "Paila marina",
    "valor_menu": 7990
    },
    {"Domingo": "Porotos con riendas",
    "valor_menu": 7990
    }]
        
    elif zona == "Zona Sur" :
        menu = [
    { "Menú": "Porotos con riendas",
    "valor_menu": 5990
    },
    {"Menú": "Curanto",
    "valor_menu": 7990
    },
    {"Menú": "Cazuela de ave",
        "valor_menu": 7990
    },
    {"Menú": "Empanadas de mariscos",
    "valor_menu": 7990
    },
    {"Menú": "Centolla gratinada",
    "valor_menu": 7990
    },
    {"Menú": "Congrio frito",
    "valor_menu": 7990
    },
    {"Menú": "Curry de congrio",
    "valor_menu": 7990
    }]
        
    elif zona == "Zona Lacustre":
        menu = [
    { "Menú": "Curanto en hoyo",
    "valor_menu": 7990
    },
    {"Menú": "Pescado frito",
    "valor_menu": 7990
    },
    {"Menú": "Machas a la Parmesana con pebre",
        "valor_menu": 7990
    },
    {"Menú": "Caldillo de mariscos",
    "valor_menu": 7990
    },
    {"Menú": "Trucha a la parrilla",
    "valor_menu": 7990
    },
    {"Menú": "Cazuela de cordero",
    "valor_menu": 7990
    },
    {"Menú": "Asado de cordero",
    "valor_menu": 7990
    }]   

    else:
        return None
    
    return menu

def seleccionar_hoteles(zona):
    if zona == "Norte Grande":
        hoteles = {
            "Hotel Holiday Inn": {
                "Simple": 50000,
                "Matrimonial": 70000,
                "Twins": 80000,
                "Cama extra": 90000,
                "Servicio especial para bebés": 100000
            },
            "Hotel Dreams": {
                "Simple": 60000,
                "Matrimonial": 80000,
                "Twins": 90000,
                "Cama extra": 100000,
                "Servicio especial para bebés": 110000
            },
            "Hotel Casa Grande": {
                "Simple": 70000,
                "Matrimonial": 90000,
                "Twins": 100000,
                "Cama extra": 110000,
                "Servicio especial para bebés": 120000
            }
        }
    elif zona == "Zona Central":
        hoteles = {
            "Hotel Diego Portales": {
                "Simple": 35000,
                "Matrimonial": 55000,
                "Twins": 65000,
                "Cama extra": 75000,
                "Servicio especial para bebés": 85000
            },
            "Hotel Dreams": {
                "Simple": 40000,
                "Matrimonial": 60000,
                "Twins": 70000,
                "Cama extra": 80000,
                "Servicio especial para bebés": 90000
            },
            "Hotel Holiday Inn": {
                "Simple": 45000,
                "Matrimonial": 65000,
                "Twins": 75000,
                "Cama extra": 85000,
                "Servicio especial para bebés": 95000
            }
        }
    elif zona == "Zona Sur":
        hoteles = {
            "Hotel Holiday Inn": {
                "Simple": 40000,
                "Matrimonial": 60000,
                "Twins": 70000,
                "Cama extra": 80000,
                "Servicio especial para bebés": 90000
            },
            "Hotel Dreams": {
                "Simple": 45000,
                "Matrimonial": 65000,
                "Twins": 75000,
                "Cama extra": 85000,
                "Servicio especial para bebés": 95000
            },
            "Hotel Diego Portales": {
                "Simple": 50000,
                "Matrimonial": 70000,
                "Twins": 80000,
                "Cama extra": 90000,
                "Servicio especial para bebés": 100000
            }
        }
    elif zona == "Zona Austral":
        hoteles = {
            "Hotel Dreams": {
                "Simple": 60000,
                "Matrimonial": 80000,
                "Twins": 90000,
                "Cama extra": 100000,
                "Servicio especial para bebés": 110000
            },
            "Hotel Diego de Almagro": {
                "Simple": 70000,
                "Matrimonial": 90000,
                "Twins": 100000,
                "Cama extra": 110000,
                "Servicio especial para bebés": 120000
            },
            "Hospedaje Centro Lagos": {
                "Simple": 80000,
                "Matrimonial": 100000,
                "Twins": 110000,
                "Cama extra": 120000,
                "Servicio especial para bebés": 130000
            }
        }
    else:
        return None

    return hoteles


def mostrar_opciones_hoteles(hoteles):
    print("Opciones de hoteles disponibles:")
    for i, hotel in enumerate(hoteles, start=1):
        print(f"{i}. {hotel}")
        habitaciones = hoteles[hotel]
        
def mostrar_menu_disponible(menu):
    print("Opciones de alimentación disponibles: ")
    for i, dia in enumerate(menu, start=1):
        nombre_dia = list(dia.keys())[0]
        nombre_plato = list(dia.values())[0]
        precio_menu = dia["valor_menu"]
        precio_formateado = f"{precio_menu:,} CLP" 
        print(f"{i}. {nombre_dia}: {nombre_plato}, precio menú: {precio_formateado}")

    opcion_menu_elegido = int(input("Ingrese el número de menú que desea agregar: "))

    if opcion_menu_elegido >= 1 and opcion_menu_elegido <= len(menu):
        cantidad = int(input("Ingrese la cantidad de menús que desea llevar: "))
        total_menu = menu[opcion_menu_elegido - 1]['valor_menu'] * cantidad
        total_menu_formateado = f"{total_menu:,} CLP"  
        print(f"Total Menús: {total_menu_formateado}")
        return total_menu

    else:
        print("Ingrese una opción válida.\n")
        return None


def seleccionar_opcion_habitacion(hoteles, hotel):
    print(f"Habitaciones disponibles en {hotel}:")
    hoteles_disponibles = hoteles[hotel]
    for i, habitacion in enumerate(hoteles_disponibles, start=1):
        print(f"{i}. {habitacion}")

    opcion = int(input("Seleccione una opción de habitación: "))
    habitacion_seleccionada = list(hoteles_disponibles.keys())[opcion - 1]
    precio_habitacion = hoteles_disponibles[habitacion_seleccionada]

    return habitacion_seleccionada, precio_habitacion


def validar_cantidad_noches():
    while True:
        try:
            cantidad_noches = int(input("Ingrese la cantidad de noches de estadía: "))
            if cantidad_noches > 0:
                return cantidad_noches
            else:
                print("La cantidad de noches debe ser mayor a 0.")
        except ValueError:
            print("Ingrese un número válido.")


# Menú principal
print("¡Bienvenido a su Agencia de Viajes!")

while True:
    print("\nMenú Principal:")
    print("1. Fecha de Viaje")
    print("2. Seleccione Origen")
    print("3. Seleccione Destino")
    print("4. Seleccione Menú de alimentación")
    print("5. Seleccione Transporte")
    print("0. Salir")

    opcion_menu = int(input("Ingrese el número de opción: "))

    if opcion_menu == 1:
        fecha_viaje = input("Ingrese la fecha para realizar el viaje (DD/MM/AAAA): ")
        print(f"Fecha de viaje seleccionada: {fecha_viaje}")

    elif opcion_menu == 2:
        total_vuelo, cantidad_personas = obtener_origen(origen)
        if total_vuelo and cantidad_personas:
            aplicar_descuentos(cantidad_personas, total_vuelo)

    elif opcion_menu == 3:
        region_destino = obtener_destino(destino)
        if region_destino:
            hoteles = seleccionar_hoteles(region_destino)
            if hoteles is None:
                print("No hay hoteles disponibles para esta región.")
            else:
                mostrar_opciones_hoteles(hoteles)
                opcion_hotel = int(input("Seleccione una opción de hotel: "))
                hotel_seleccionado = list(hoteles.keys())[opcion_hotel - 1]
                habitacion_seleccionada, precio_habitacion = seleccionar_opcion_habitacion(hoteles, hotel_seleccionado)

                cantidad_noches = validar_cantidad_noches()
                costo_total = precio_habitacion * cantidad_noches
                if cantidad_noches == 2:
                    print(f"\nHa seleccionado el hotel {hotel_seleccionado} en la región {region_destino}.")
                    print(f"Ha elegido la habitación {habitacion_seleccionada} por {cantidad_noches} noches.")
                    print(f"El costo total de la estadía es de ${costo_total} CLP + Desayuno Gratis.")

                elif cantidad_noches > 2:
                    costo_total -= precio_habitacion
                    print(f"\nHa seleccionado el hotel {hotel_seleccionado} en la región {region_destino}.")
                    print(f"Ha elegido la habitación {habitacion_seleccionada} por {cantidad_noches} noches.")
                    print(f"El costo total de la estadía es de ${costo_total} CLP.")

                else:
                    print("Cantidad de noches inválida.")

    elif opcion_menu == 4:
        opcion_zona = 0
        while opcion_zona not in [1,2,3,4]:
            opcion_zona = int(input("""Seleccione una opción de zona: 
                1. Norte
                2. Centro
                3. Sur
                4. Lacustre                                           
                """))
            if opcion_zona == 1:
                zona = "Zona Norte"           
            elif opcion_zona == 2:
                zona = "Zona Central"         
            elif opcion_zona == 3:
                zona = "Zona Sur"
            elif opcion_zona == 4:
                zona = "Zona Lacustre"
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        
        menu_alimentacion = seleccionar_menu(zona)
        if menu_alimentacion is None:
            print("No hay menús disponibles para esta zona.")
        else:
            total_menu = mostrar_menu_disponible(menu_alimentacion)
        if total_menu:
            pass

    elif opcion_menu == 5:
        total_transporte, opciones_transporte = obtener_transporte()
    elif opcion_menu == 0:
        print("Gracias por utilizar nuestro servicio. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
