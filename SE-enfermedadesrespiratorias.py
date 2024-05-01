from pyknow import *

class SistemaDiagnostico(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.diagnostico = None
        self.puntaje_maximo = 0

    @DefFacts()
    def _inicializar(self):
        yield Fact(fiebre=None)
        yield Fact(tos_seca=None)
        yield Fact(tos_productiva=None)
        yield Fact(dolor_garganta=None)
        yield Fact(dificultad_respirar=None)
        yield Fact(congestion_nasal=None)
        yield Fact(fatiga=None)
        yield Fact(dolor_cabeza=None)
        yield Fact(malestar_general=None)

    @Rule(Fact(fiebre=True), Fact(dificultad_respirar=True), Fact(tos_seca=True))
    def covid19(self):
        self.diagnostico = "COVID-19"

    @Rule(AND(Fact(fiebre=True), Fact(tos_productiva=True), Fact(dificultad_respirar=True), Fact(congestion_nasal=True), Fact(fatiga=True)))
    def gripa_severa(self):
            self.diagnostico = "Gripe severa"

    @Rule(AND(Fact(fiebre=True), Fact(tos_seca=True), Fact(dolor_garganta=True), Fact(dolor_cabeza=True)))
    def faringitis(self):
        self.diagnostico = "Faringitis"

    @Rule(Fact(diagnostico=None))
    def sin_diagnostico(self):
        self.diagnostico = "No se puede determinar el diagnóstico con los síntomas proporcionados."

def obtener_sintomas():
    engine = SistemaDiagnostico()
    engine.reset()

    while True:
        fiebre = input("¿Tienes fiebre? (s/n): ").lower()
        if fiebre == 's' or fiebre == 'n':
            engine.declare(Fact(fiebre=fiebre == 's'))
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

    while True:
        tos_seca = input("¿Tienes tos seca? (s/n): ").lower()
        if tos_seca == 's' or tos_seca == 'n':
            engine.declare(Fact(tos_seca=tos_seca == 's'))
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

    if tos_seca == 'n':
        while True:
            tos_productiva = input("¿Tienes tos productiva (con flema)? (s/n): ").lower()
            if tos_productiva == 's' or tos_productiva == 'n':
                engine.declare(Fact(tos_productiva=tos_productiva == 's'))
                break
            else:
                print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")
    else:
        engine.declare(Fact(tos_productiva=False))

    while True:
        dolor_garganta = input("¿Tienes dolor de garganta? (s/n): ").lower()
        if dolor_garganta == 's' or dolor_garganta == 'n':
            engine.declare(Fact(dolor_garganta=dolor_garganta == 's'))
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

    while True:
        dificultad_respirar = input("¿Tienes dificultad para respirar? (s/n): ").lower()
        if dificultad_respirar == 's' or dificultad_respirar == 'n':
            engine.declare(Fact(dificultad_respirar=dificultad_respirar == 's'))
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")
    while True:
        congestion_nasal = input("¿Tienes congestión nasal? (s/n): ").lower()
        if congestion_nasal == 's' or congestion_nasal == 'n':
            engine.declare(Fact(congestion_nasal=congestion_nasal == 's'))
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

    while True:
        fatiga = input("¿Sientes fatiga o cansancio? (s/n): ").lower()
        if fatiga == 's' or fatiga == 'n':
            engine.declare(Fact(fatiga=fatiga == 's'))
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

    while True:
        dolor_cabeza = input("¿Tienes dolor de cabeza? (s/n): ").lower()
        if dolor_cabeza == 's' or dolor_cabeza == 'n':
            engine.declare(Fact(dolor_cabeza=dolor_cabeza == 's'))
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

    while True:
        malestar_general = input("¿Sientes malestar general en el cuerpo? (s/n): ").lower()
        if malestar_general == 's' or malestar_general == 'n':
            engine.declare(Fact(malestar_general=malestar_general == 's'))
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

    engine.run()

    print("\nDiagnóstico:", engine.diagnostico)

def main():
    while True:
        obtener_sintomas()
        respuesta = input("\n¿Desea realizar otra consulta? (s/n): ").lower()
        if respuesta != 's':
            break
        elif respuesta == 'n':
            print("Gracias por usar el sistema de diagnóstico. ¡Que te mejores pronto!")
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

if __name__ == "__main__":
    main()
