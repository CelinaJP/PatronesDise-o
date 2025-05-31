#SIEMPRE USA EL MISMO GERENTE

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
