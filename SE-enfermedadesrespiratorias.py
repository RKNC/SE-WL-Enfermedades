class Diagnostico:
    """Clase de hecho para el diagnóstico"""
    def __init__(self, fiebre=False, tos_seca=False, tos_productiva=False, dolor_garganta=False, dificultad_respirar=False, congestion_nasal=False, fatiga=False, dolor_cabeza=False, malestar_general=False):
        self.fiebre = fiebre
        self.tos_seca = tos_seca
        self.tos_productiva = tos_productiva
        self.dolor_garganta = dolor_garganta
        self.dificultad_respirar = dificultad_respirar
        self.congestion_nasal = congestion_nasal
        self.fatiga = fatiga
        self.dolor_cabeza = dolor_cabeza
        self.malestar_general = malestar_general

def diagnostico_enfermedad(datos):
    # Reglas de inferencia para determinar la enfermedad probable
    if datos.fiebre and datos.tos_seca and datos.dificultad_respirar and not datos.congestion_nasal and not datos.dolor_garganta:
        return "COVID-19"
    elif datos.fiebre and datos.tos_productiva and datos.dolor_garganta and datos.congestion_nasal and datos.dolor_cabeza and datos.malestar_general:
        return "Gripe"
    elif datos.tos_productiva and datos.dolor_garganta and datos.congestion_nasal and not datos.fiebre:
        return "Resfriado"
    elif datos.dificultad_respirar and datos.fatiga and datos.dolor_cabeza and datos.malestar_general and datos.tos_productiva:
        return "Bronquitis"
    elif datos.fiebre and datos.dolor_garganta and not datos.tos_seca and not datos.tos_productiva:
        return "Faringitis estreptocócica"
    elif datos.fiebre or datos.dolor_garganta or datos.dolor_cabeza:
        return "Catarro"
    elif datos.fatiga and datos.malestar_general and not datos.fiebre and not datos.tos_seca and not datos.tos_productiva:
        return "Infección viral"
    elif datos.tos_seca and datos.dolor_cabeza and datos.congestion_nasal:
        return "Sinusitis"
    else:
        return "Sin enfermedad grave"

def obtener_sintomas():
    fiebre = input("¿Tienes fiebre? (s/n): ").lower() == 's'
    tos_seca = input("¿Tienes tos seca? (s/n): ").lower() == 's'

    if tos_seca:
        tos_productiva = False
    else:
        tos_productiva = input("¿Tienes tos productiva (con flema)? (s/n): ").lower() == 's'

    dolor_garganta = input("¿Tienes dolor de garganta? (s/n): ").lower() == 's'
    dificultad_respirar = input("¿Tienes dificultad para respirar? (s/n): ").lower() == 's'
    congestion_nasal = input("¿Tienes congestión nasal? (s/n): ").lower() == 's'
    fatiga = input("¿Sientes fatiga o cansancio? (s/n): ").lower() == 's'
    dolor_cabeza = input("¿Tienes dolor de cabeza? (s/n): ").lower() == 's'
    malestar_general = input("¿Sientes malestar general en el cuerpo? (s/n): ").lower() == 's'

    return Diagnostico(fiebre, tos_seca, tos_productiva, dolor_garganta, dificultad_respirar, congestion_nasal, fatiga, dolor_cabeza, malestar_general)

def main():
    datos = obtener_sintomas()
    diagnostico = diagnostico_enfermedad(datos)
    print("Enfermedad probable:", diagnostico)

if __name__ == "__main__":
    main()
    