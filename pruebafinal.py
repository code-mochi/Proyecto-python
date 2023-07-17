from datetime import datetime

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
        "region_1": "Arica y Parinacota",
        "actividad_1": "Paseo por el Valle de Azapa",
        "actividad_2": "Visita al Parque Nacional Lauca"
    },
    {
        "zona_pais": "Norte Grande",
        "region_2": "Tarapacá",
        "actividad_1": "Tour por el Salar de Huasco",
        "actividad_2": "Visita al Geoglifo Gigante de Pintados"
    },
    {
        "zona_pais": "Norte Grande",
        "region_3": "Antofagasta",
        "actividad_1": "Exploración en el Desierto de Atacama",
        "actividad_2": "Recorrido por la Mano del Desierto"
    },
    {
        "zona_pais": "Norte Grande",
        "region_4": "Atacama",
        "actividad_1": "Visita a los Geisers del Tatio",
        "actividad_2": "Observación Astronómica en San Pedro de Atacama"
    },
    {
        "zona_pais": "Norte Grande",
        "region_5": "Coquimbo",
        "actividad_1": "Tour por el Valle del Elqui",
        "actividad_2": "Avistamiento de Ballenas en la Bahía de Tongoy"
    },
    {
        "zona_pais": "Zona Central",
        "region_6": "Valparaíso",
        "actividad_1": "Recorrido por los Cerros de Valparaíso",
        "actividad_2": "Visita al Museo de Bellas Artes de Valparaíso"
    },
    {
        "zona_pais": "Zona Central",
        "region_7": "Metropolitana",
        "actividad_1": "City Tour por Santiago",
        "actividad_2": "Visita al Cerro San Cristóbal"
    },
    {
        "zona_pais": "Zona Central",
        "region_8": "O'Higgins",
        "actividad_1": "Tour por las Viñas de Colchagua",
        "actividad_2": "Visita al Parque Nacional Radal Siete Tazas"
    },
    {
        "zona_pais": "Zona Central",
        "region_9": "Maule",
        "actividad_1": "Exploración en el Parque Nacional Radal Siete Tazas",
        "actividad_2": "Tour por las Iglesias de Chiloé"
    },
    {
        "zona_pais": "Zona Central",
        "region_10": "Biobío",
        "actividad_1": "Visita al Parque Nacional Conguillío",
        "actividad_2": "Tour por los Saltos del Laja"
    },
    {
        "zona_pais": "Zona Sur",
        "region_11": "Araucanía",
        "actividad_1": "Exploración en el Parque Nacional Huerquehue",
        "actividad_2": "Visita al Mercado Municipal de Temuco"
    },
    {
        "zona_pais": "Zona Sur",
        "region_12": "Los Ríos",
        "actividad_1": "Tour por la Reserva Biológica Huilo Huilo",
        "actividad_2": "Recorrido por los Fuertes de Valdivia"
    },
    {
        "zona_pais": "Zona Sur",
        "region_13": "Los Lagos",
        "actividad_1": "Navegación por los Fiordos de la Región de Los Lagos",
        "actividad_2": "Visita a las Termas de Puyehue"
    },
    {
        "zona_pais": "Zona Sur",
        "region_14": "Aysén",
        "actividad_1": "Tour por el Glaciar Exploradores",
        "actividad_2": "Avistamiento de Cóndores en Coyhaique"
    },
    {
        "zona_pais": "Zona Austral",
        "region_15": "Magallanes y Antártica Chilena",
        "actividad_1": "Exploración en el Parque Nacional Torres del Paine",
        "actividad_2": "Navegación por los Glaciares Balmaceda y Serrano"
    }
]
def cambio_moneda(valor_vuelo, origen):
    cambio = [
        {
            "tipo de cambio" : "Real Brasileño (BRL)",
            "valor": 165.91
        },
        {
            "tipo de cambio" : "Peso Argentino (ARG)",
            "valor": 3.10
        },
        {
            "tipo de cambio" : "Euro (ESP)",
            "valor": 894.54
        },

        {
            "tipo de cambio" : "Dolar (USD)",
            "valor": 812.89
        },
        {
            "tipo de cambio" : "Euro (FRA)",
            "valor": 894.54
        },
         {
            "tipo de cambio" : "Shekel (ISR)",
            "valor": 219.70
        },
                
        {
            "tipo de cambio" : "Peso Mexicano (MXN)",
            "valor": 47.66
        },
        
       
        {
            "tipo de cambio" : "Corona Sueca (KR)",
            "valor": 75.60
        },
        {
            "tipo de cambio" : "Euro (ITA)",
            "valor": 894.54
        }
        
    ]

    if origen == 1:  # USD
        total_viaje = valor_vuelo / cambio[0]["valor"]
        print(f"Su cambio de dólares a pesos chilenos es: {round(total_viaje)} USD / {round(total_viaje * cambio[0]['valor'])} CLP")
    elif origen == 2:  # ARG
        total_viaje = valor_vuelo / cambio[1]["valor"]
        print(f"Su cambio de pesos argentinos a pesos chilenos es: {round(total_viaje)} ARG / {round(total_viaje * cambio[1]['valor'])} CLP")
    elif origen == 3:  # ESP
        total_viaje = valor_vuelo / cambio[2]["valor"]
        print(f"Su cambio de euros a pesos chilenos es: {round(total_viaje)} EUR / {round(total_viaje * cambio[2]['valor'])} CLP")
        total_viaje = valor_vuelo / cambio[2]["valor"]
        print(f"Su cambio de euros a pesos chilenos es: {round(total_viaje)} EUR / {round(total_viaje * cambio[2]['valor'])} CLP")
    elif origen == 6:  # MXN
        total_viaje = valor_vuelo / cambio[3]["valor"]
        print(f"Su cambio de pesos mexicanos a pesos chilenos es: {round(total_viaje)} MXN / {round(total_viaje * cambio[3]['valor'])} CLP")
    elif origen == 7:  # BRL
        total_viaje = valor_vuelo / cambio[4]["valor"]
        print(f"Su cambio de reales brasileños a pesos chilenos es: {round(total_viaje)} BRL / {round(total_viaje * cambio[4]['valor'])} CLP")
    elif origen == 8:  # ILS
        total_viaje = valor_vuelo / cambio[5]["valor"]
        print(f"Su cambio de shekels a pesos chilenos es: {round(total_viaje)} ILS / {round(total_viaje * cambio[5]['valor'])} CLP")
    elif origen == 9:  # KR
        total_viaje = valor_vuelo / cambio[6]["valor"]
        print(f"Su cambio de coronas suecas a pesos chilenos es:{round(total_viaje)} KR / {round(total_viaje * cambio[6]['valor'])} CLP")
    elif origen == 10:
        total_viaje_1 = valor_vuelo / cambio[0]["valor"]
        total_viaje_2 = valor_vuelo / cambio[1]["valor"]
        total_viaje_3 = valor_vuelo / cambio[2]["valor"]
        total_viaje_4 = valor_vuelo / cambio[3]["valor"]
        total_viaje_5 = valor_vuelo / cambio[4]["valor"]
        total_viaje_6 = valor_vuelo / cambio[5]["valor"]
        total_viaje_7 = valor_vuelo / cambio[6]["valor"]
        print(f"Su cambio de dólar a pesos chilenos es: {round(total_viaje_1)} USD / {round(total_viaje_1 * cambio[0]['valor'])} CLP")
        print(f"Su cambio de pesos argentinos a pesos chilenos es: {round(total_viaje_2)} ARG / {round(total_viaje_2 * cambio[1]['valor'])} CLP")
        print(f"Su cambio de euros a pesos chilenos es: {round(total_viaje_3)} EUR / {round(total_viaje_3 * cambio[2]['valor'])} CLP")
        print(f"Su cambio de pesos mexicanos a pesos chilenos es: {round(total_viaje_4)} MXN / {round(total_viaje_4 * cambio[3]['valor'])} CLP")
        print(f"Su cambio de reales brasileños a pesos chilenos es: {round(total_viaje_5)} BRL / {round(total_viaje_5 * cambio[4]['valor'])} CLP")
        print(f"Su cambio de shekels a pesos chilenos es: {round(total_viaje_6)} ILS / {round(total_viaje_6 * cambio[5]['valor'])} CLP")
        print(f"Su cambio de coronas suecas a pesos chilenos es: {round(total_viaje_7)} KR / {round(total_viaje_7 * cambio[6]['valor'])} CLP")

fecha_viaje = None

def obtener_fecha_viaje():
    global fecha_viaje
    fecha_viaje = input("Ingrese la fecha para realizar el viaje (DD/MM/AAAA): ")
    return fecha_viaje

def obtener_descuento_por_fecha(fecha):
    mes = fecha.month

    if mes in [1, 2]:  # Verano: enero y febrero
        descuento = 0.05  # 5% de descuento en verano
        temporada = "Verano"
    elif mes in [6, 7]:  # Invierno: junio y julio 
        descuento = 0.08  # 8% de descuento en invierno
        temporada = "Invierno"
    elif mes in [10, 11]:  # Primavera: octubre y noviembre
        descuento = 0.12  # 12% de descuento en primavera
        temporada = "Primavera"
    elif mes in [4, 5]:  # Otoño: abril y mayo
        descuento = 0.10  # 10% de descuento en otoño
        temporada = "Otoño"
    else:
        descuento = 0  # Sin descuento para otros meses
        temporada = "N/A"

    return descuento, temporada

# Obtener la fecha proporcionada por el usuario
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

global fecha_previa
fecha_previa = datetime(año, mes, dia)

# Obtener el descuento y la temporada correspondiente
descuento_obtenido, temporada_obtenida = obtener_descuento_por_fecha(fecha_previa)
print("La temporada es", temporada_obtenida)
print("El descuento para la fecha", dia, "/", mes, "/", año, "es del", descuento_obtenido * 100, "%.")

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
    Seleccione la Opción:
    """))

    if opc in range(1, len(origen) + 1):
        global pais_origen
        pais_origen = origen[opc - 1]["pais_origen"]
        valor_vuelo = origen[opc - 1]["valor_vuelo"]
        cantidad_personas = int(input("Ingresar cantidad de personas: "))
        global total_vuelo
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
        global region_destino1
        region_destino1 = destino[opc - 1]["zona_pais"]
        print(f"Destino seleccionado: {region_destino1}")
        return region_destino1
    else:
        print("No ha ingresado un destino válido.")
        return None

def elegir_actividad(destino):
    print("Regiones de Chile:")
    for num, region in enumerate(destino, start=1):
        print(f"{num}. {region['zona_pais']} - {region[f'region_{num}']}")

    region_elegida = int(input("Elige el número de la región de Chile: "))

    if region_elegida in range(1, len(destino) + 1):
        region = destino[region_elegida - 1][f"region_{region_elegida}"]
        actividad_1 = destino[region_elegida - 1][f"actividad_1"]
        actividad_2 = destino[region_elegida - 1][f"actividad_2"]

        print(f"\nActividades turísticas en {region}:")
        print(f"1. {actividad_1}")
        print(f"2. {actividad_2}")

        actividad_elegida = int(input("Elige el número de la actividad turística: "))

        if actividad_elegida == 1:
            actividad = actividad_1
        elif actividad_elegida == 2:
            actividad = actividad_2
        else:
            print("El número de actividad turística seleccionado no es válido.")
            return

        print(f"\n¡Excelente elección! Disfruta de {actividad} en {region}.")
    else:
        print("El número de región seleccionado no es válido.")
      
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
    global total
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
    { "Lunes": "Ceviche de pescado",
    "valor_menu": 5990
    },
    {"Martes": "Locro de papas",
    "valor_menu": 7990
    },
    {"Miércoles": "Seco de cordero",
    "valor_menu": 7990
    },
    {"Jueves": "Pollo Asado con Papas fritas",
    "valor_menu": 7990
    },
    {"Viernes": "Chupe de Jaiba",
    "valor_menu": 7990
    },
    {"Sábado": "Arroz con Asado",
    "valor_menu": 7990
    },
    {"Domingo": "Pescado con Ensalada",
    "valor_menu": 7990
    }]
        
    elif zona == "Zona Central":
        menu = [
    { "Lunes": "Porotos con riendas",
    "valor_menu": 5990
    },
    {"Martes": "Pescado frito",
    "valor_menu": 7990
    },
    {"Miércoles": "Pastel de choclo",
    "valor_menu": 7990
    },
    {"Jueves": "Cazuela de vacuno",
    "valor_menu": 7990
    },
    {"Viernes": "Asado a la parrilla",
    "valor_menu": 7990
    },
    {"Sábado": "Paila marina",
    "valor_menu": 7990
    },
    {"Domingo": "Porotos con riendas",
    "valor_menu": 7990
    }]
        
    elif zona == "Zona Sur" :
        menu = [
    { "Lunes": "Porotos con riendas",
    "valor_menu": 5990
    },
    {"Martes": "Curanto",
    "valor_menu": 7990
    },
    {"Miércoles": "Cazuela de ave",
        "valor_menu": 7990
    },
    {"Jueves": "Empanadas de mariscos",
    "valor_menu": 7990
    },
    {"Viernes": "Centolla gratinada",
    "valor_menu": 7990
    },
    {"Sábado": "Congrio frito",
    "valor_menu": 7990
    },
    {"Domingo": "Curry de congrio",
    "valor_menu": 7990
    }]
        
    elif zona == "Zona Lacustre":
        menu = [
    { "Lunes": "Curanto en hoyo",
    "valor_menu": 7990
    },
    {"Martes": "Pescado frito",
    "valor_menu": 7990
    },
    {"Miércoles": "Machas a la Parmesana con pebre",
        "valor_menu": 7990
    },
    {"Jueves": "Caldillo de mariscos",
    "valor_menu": 7990
    },
    {"Viernes": "Trucha a la parrilla",
    "valor_menu": 7990
    },
    {"Sábado": "Cazuela de cordero",
    "valor_menu": 7990
    },
    {"Domingo": "Asado de cordero",
    "valor_menu": 7990
    }]   

    else:
        return None
    
    return menu

def seleccionar_hoteles(zona):
    if zona == "Norte Grande":
        hoteles = [
            ("Hotel Holiday Inn", {
                "Simple": 50000,
                "Matrimonial": 70000,
                "Twins": 80000,
                "Cama extra": 90000,
                "Servicio especial para bebés": 100000
            }),
            ("Hotel Dreams", {
                "Simple": 60000,
                "Matrimonial": 80000,
                "Twins": 90000,
                "Cama extra": 100000,
                "Servicio especial para bebés": 110000
            }),
            ("Hotel Casa Grande", {
                "Simple": 70000,
                "Matrimonial": 90000,
                "Twins": 100000,
                "Cama extra": 110000,
                "Servicio especial para bebés": 120000
            })
        ]
    elif zona == "Zona Central":
        hoteles = [
            ("Hotel Diego Portales", {
                "Simple": 35000,
                "Matrimonial": 55000,
                "Twins": 65000,
                "Cama extra": 75000,
                "Servicio especial para bebés": 85000
            }),
            ("Hotel Dreams", {
                "Simple": 40000,
                "Matrimonial": 60000,
                "Twins": 70000,
                "Cama extra": 80000,
                "Servicio especial para bebés": 90000
            }),
            ("Hotel Holiday Inn", {
                "Simple": 45000,
                "Matrimonial": 65000,
                "Twins": 75000,
                "Cama extra": 85000,
                "Servicio especial para bebés": 95000
            })
        ]
    elif zona == "Zona Sur":
        hoteles = [
            ("Hotel Holiday Inn", {
                "Simple": 40000,
                "Matrimonial": 60000,
                "Twins": 70000,
                "Cama extra": 80000,
                "Servicio especial para bebés": 90000
            }),
            ("Hotel Dreams", {
                "Simple": 45000,
                "Matrimonial": 65000,
                "Twins": 75000,
                "Cama extra": 85000,
                "Servicio especial para bebés": 95000
            }),
            ("Hotel Diego Portales", {
                "Simple": 50000,
                "Matrimonial": 70000,
                "Twins": 80000,
                "Cama extra": 90000,
                "Servicio especial para bebés": 100000
            })
        ]
    elif zona == "Zona Austral":
        hoteles = [
            ("Hotel Dreams", {
                "Simple": 60000,
                "Matrimonial": 80000,
                "Twins": 90000,
                "Cama extra": 100000,
                "Servicio especial para bebés": 110000
            }),
            ("Hotel Diego de Almagro", {
                "Simple": 70000,
                "Matrimonial": 90000,
                "Twins": 100000,
                "Cama extra": 110000,
                "Servicio especial para bebés": 120000
            }),
            ("Hospedaje Centro Lagos", {
                "Simple": 80000,
                "Matrimonial": 100000,
                "Twins": 110000,
                "Cama extra": 120000,
                "Servicio especial para bebés": 130000
            })
        ]
    else:
        return None

    return hoteles
       

def mostrar_opciones_hoteles(hoteles):
    print("Opciones de hoteles disponibles:")
    for i, (nombre_hotel, habitaciones) in enumerate(hoteles, start=1):
        print(f"{i}. {nombre_hotel}")

    opcion_hotel = int(input("Seleccione una opción de hotel: "))
    hotel_seleccionado, habitaciones_hotel_seleccionado = hoteles[opcion_hotel - 1]

    print(f"\nHabitaciones disponibles en {hotel_seleccionado}:")
    for i, (tipo_habitacion, precio_habitacion) in enumerate(habitaciones_hotel_seleccionado.items(), start=1):
        precio_habitacion_formateado = "${:,.0f} CLP".format(precio_habitacion)
        print(f"{i}. {tipo_habitacion}: {precio_habitacion_formateado}")

    opcion_habitacion = int(input("Seleccione una opción de habitación: "))
    habitacion_seleccionada = list(habitaciones_hotel_seleccionado.keys())[opcion_habitacion - 1]
    precio_habitacion = habitaciones_hotel_seleccionado[habitacion_seleccionada]

    return hotel_seleccionado, habitacion_seleccionada, precio_habitacion

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
        global total_menu
        total_menu = menu[opcion_menu_elegido - 1]['valor_menu'] * cantidad
        total_menu_formateado = f"{total_menu:,} CLP"  
        print(f"Total Menús: {total_menu_formateado}")
        return total_menu

    else:
        print("Ingrese una opción válida.\n")
        return None

def seleccionar_opcion_habitacion(hoteles, hotel_seleccionado):
    if hotel_seleccionado in hoteles:
        habitaciones = hoteles[hotel_seleccionado]
        print("Opciones de habitaciones disponibles:")
        for i, (tipo_habitacion, precio_habitacion) in enumerate(habitaciones.items(), start=1):
            precio_habitacion_formateado = "${:,.0f} CLP".format(precio_habitacion)
            print(f"{i}. {tipo_habitacion}: {precio_habitacion_formateado}")
        opcion_habitacion = int(input("Seleccione una opción de habitación: "))
        habitacion_seleccionada = list(habitaciones.keys())[opcion_habitacion - 1]
        
        precio_habitacion = list(habitaciones.values())[opcion_habitacion - 1]
        return habitacion_seleccionada, precio_habitacion
    else:
        print("El hotel seleccionado no es válido.")
        return None, None
    
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

def total_costo(total_menu, total_vuelo, precio_habitacion):
    costo_total_final = total_menu + total_vuelo + total + precio_habitacion
    return costo_total_final

def generar_boleta(fecha_viaje, region_destino1, pais_origen, hotel_seleccionado, habitacion_seleccionada, precio_habitacion, cantidad_noches, costo_total_final):
    print("********************************************")
    print("             AGENCIA DE VIAJES              ")
    print("********************************************")
    print("Fecha de viaje: " + fecha_viaje)
    print("Origen: " + str(pais_origen))
    print("Destino: " + str(region_destino1) + " Chile")
    print("********************************************")
    print("                DETALLES DEL HOTEL          ")
    print("********************************************")
    print("Hotel: " + hotel_seleccionado)
    print("Habitación: " + habitacion_seleccionada)
    print("Precio de habitación: $" + str(precio_habitacion) + " CLP")
    print("Cantidad de noches: " + str(cantidad_noches))
    print("Costo total: $" + str(costo_total_final) + " CLP")
    print("********************************************")
    print("            ¡GRACIAS POR SU COMPRA!         ")
    print("********************************************")


# Menú principal
print("¡Bienvenido a su Agencia de Viajes!")

while True:
    print("\nMenú Principal:")
    print("1. Confirmar Fecha de Viaje")
    print("2. Seleccione Origen")
    print("3. Seleccione Destino")
    print("4. Seleccione Actividades")
    print("5. Seleccione Menú de alimentación")
    print("6. Seleccione Transporte")
    print("7. Boleta")
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
        region_destino1 = obtener_destino(destino)
        if region_destino1:
            hoteles = seleccionar_hoteles(region_destino1)
            if hoteles is None:
                print("No hay hoteles disponibles para esta región.")
            else:
                hotel_seleccionado, habitacion_seleccionada, precio_habitacion = mostrar_opciones_hoteles(hoteles)
                cantidad_noches = validar_cantidad_noches()
                
    elif opcion_menu == 4:
        elegir_actividad(destino)
        
    elif opcion_menu == 5:
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
  
    elif opcion_menu == 6:
        total_transporte, opciones_transporte = obtener_transporte()
  
    elif opcion_menu == 7:
        costo_total_final = total_costo(total_menu, total_vuelo, precio_habitacion)
        boletita = generar_boleta(fecha_viaje, region_destino1, pais_origen, hotel_seleccionado, habitacion_seleccionada, precio_habitacion, cantidad_noches, costo_total_final)
        print(boletita)
        break
    elif opcion_menu == 0:
        print("Gracias por utilizar nuestro servicio. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")