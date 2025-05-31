#SIGLETON
class GerenteLog:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(GerenteLog, cls).__new__(cls)
            cls._instancia.mensajes = []
        return cls._instancia

    def registrar(self, mensaje):
        self.mensajes.append(mensaje)
        print(f"Registrado: {mensaje}")

# Uso: Siempre obtendrás el mismo gerente
log1 = GerenteLog()
log1.registrar("Primer evento.")
log2 = GerenteLog() # Aunque parezca que creas otro, es el mismo
log2.registrar("Segundo evento.")
print(log1.mensajes) # Verás ambos mensajes, porque es el mismo objeto




#ADAPTER
class EnchufeViejo:
    def conectar(self, dispositivo):
        print(f"Enchufe viejo conectando: {dispositivo}")

class AparatoNuevo:
    def encender_con_nuevo_enchufe(self, voltaje):
        print(f"Aparato nuevo encendido con {voltaje}V.")

class AdaptadorDeEnchufe:
    def __init__(self, aparato_nuevo):
        self._aparato_nuevo = aparato_nuevo

    def conectar(self, dispositivo): # Adapta la forma vieja a la nueva
        print(f"Adaptador conectando {dispositivo}...")
        self._aparato_nuevo.encender_con_nuevo_enchufe("220") # Traduce a la forma nueva

# Uso:
viejo_enchufe = EnchufeViejo()
viejo_enchufe.conectar("Lámpara")

nuevo_aparato = AparatoNuevo()
# nuevo_aparato.encender_con_nuevo_enchufe("220") # No puedo usarlo directamente con el enchufe viejo

adaptador = AdaptadorDeEnchufe(nuevo_aparato)
adaptador.conectar("Teléfono") # Ahora el teléfono (nuevo aparato) puede usar la forma de conectar del enchufe viejo




#STRATEGY
import abc

class EstrategiaEnvio(abc.ABC):
    @abc.abstractmethod
    def enviar(self, paquete):
        pass

class EnvioMoto(EstrategiaEnvio):
    def enviar(self, paquete):
        print(f"Enviando '{paquete}' por moto.")

class EnvioCamion(EstrategiaEnvio):
    def enviar(self, paquete):
        print(f"Enviando '{paquete}' por camión.")

class SistemaEnvios:
    def __init__(self, estrategia: EstrategiaEnvio):
        self._estrategia_envio = estrategia

    def despachar(self, paquete):
        self._estrategia_envio.enviar(paquete)

# Uso:
sistema_moto = SistemaEnvios(EnvioMoto())
sistema_moto.despachar("Libro")

sistema_camion = SistemaEnvios(EnvioCamion())
sistema_camion.despachar("Mesa")

# Si mañana hay Envío por Dron, solo creo la clase EnvioDron y la uso.




