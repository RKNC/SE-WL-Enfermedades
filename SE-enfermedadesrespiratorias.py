from pyknow import *

class SistemaDiagnostico(KnowledgeEngine):
    def __init__(self):
        super().__init__()

    @DefFacts()
    def _inicializar(self):
        yield Fact(fiebre=False)
        yield Fact(tos_seca=False)
        yield Fact(tos_productiva=False)
        yield Fact(dolor_garganta=False)
        yield Fact(dificultad_respirar=False)
        yield Fact(congestion_nasal=False)
        yield Fact(fatiga=False)
        yield Fact(dolor_cabeza=False)
        yield Fact(malestar_general=False)
        yield Fact(diagnostico_establecido=False)

    @Rule(AND(Fact(fiebre=True),
              Fact(tos_seca=True),
              Fact(dificultad_respirar=True),
              Fact(congestion_nasal=False),
              Fact(dolor_garganta=False),
              NOT(Fact(diagnostico_establecido=True))))
    def covid19(self):
        self.diagnostico_establecido = True
        print("\nEnfermedad probable: COVID-19")
        print("Descripción: COVID-19 es una enfermedad infecciosa causada por el coronavirus SARS-CoV-2. Los síntomas comunes incluyen fiebre, tos seca y dificultad para respirar.")
        print("Posibles causas: Contacto con una persona infectada o superficies contaminadas.")
        print("Duración: Varía, puede ser desde unos pocos días hasta varias semanas.")
        print("Tratamiento: Reposo, hidratación adecuada y medicamentos para aliviar los síntomas. Consulte a un médico para un tratamiento adecuado.")
    @Rule(Fact(fiebre=True),
      Fact(tos_productiva=True),
      Fact(dolor_garganta=True),
      Fact(dificultad_respirar=True),
      Fact(congestion_nasal=True),
      Fact(fatiga=True),
      Fact(dolor_cabeza=True),
      Fact(malestar_general=True),
      NOT(Fact(diagnostico_establecido=True)))
    def gripa_severa(self):
        self.diagnostico_establecido = True
        print("\nEnfermedad probable: Gripe severa")
        print("Descripción: La gripe severa es una forma grave de la enfermedad viral conocida como gripe. Los síntomas comunes incluyen fiebre, tos productiva, dolor de garganta, dificultad para respirar, congestión nasal, fatiga, dolor de cabeza y malestar general.")
        print("Posibles causas: Infección con una cepa particularmente virulenta del virus de la influenza.")
        print("Duración: Por lo general, dura de una a dos semanas, pero puede prolongarse si se presentan complicaciones.")
        print("Tratamiento: Reposo, hidratación adecuada, medicamentos antivirales y analgésicos para aliviar los síntomas. Es recomendable consultar a un médico de inmediato para un tratamiento adecuado y evitar complicaciones graves.")
    # Aqui se pueden aumentar los datos y reglas para tener más enfermedades dosponibles (By:Rogger)
    @Rule(Fact(diagnostico_establecido=False),
          NOT(OR(Fact(fiebre=True),
                 Fact(tos_seca=True),
                 Fact(tos_productiva=True),
                 Fact(dolor_garganta=True),
                 Fact(dificultad_respirar=True),
                 Fact(congestion_nasal=True),
                 Fact(fatiga=True),
                 Fact(dolor_cabeza=True),
                 Fact(malestar_general=True))))
    def sin_diagnostico(self):
        print("\nNo se puede determinar el diagnóstico con los síntomas proporcionados. Se recomienda consultar a un médico para un diagnóstico preciso y un tratamiento adecuado.")
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

def main():
    obtener_sintomas()

if __name__ == "__main__":
    main()
