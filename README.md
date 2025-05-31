# T1: Patrones de diseño
## Actividad práctica
### Ejercicio 1: 
Investigar y documentar críticas a los patrones de diseño. Mencione ejemplos concretos.
### Respuesta 1:
Se lo critica por:
Complicar cosas simples: Usar un patrón para un problema fácil puede hacer el código más difícil de entender de lo necesario. Imagina usar un martillo gigante para clavar un pequeño clavo.
Diseñar de más: A veces, la gente se obsesiona con aplicar patrones y crea soluciones demasiado complejas para un problema que no las necesita. Es como construir un cohete para ir a la esquina.
Falsa seguridad: Creer que, solo por usar un patrón, el diseño será perfecto. No siempre es así si no se entiende bien por qué se usa.
Cuesta aprenderlos: Entender y usarlos bien lleva tiempo. Si se usan mal, pueden empeorar el código.

### Ejercicio 2:
Seleccione 3 patrones de diseño e implementarlos en Python. Arme ejemplos concretos de uso. Lo ideal es
elegir un patrón de cada clasificación.
-Singleton (UNICA INSTANCIA) : Asegura que una clase solo tenga una única "copia" en todo el programa. Si intentas crear otra, te da la misma que ya existe.
Ejemplo: programa "Gerente de Log". Solo quiero un gerente que anote todo lo que pasa. Con Singleton, siempre voy a usar el mismo gerente, no importa cuántas veces intento "crear" uno nuevo.
-Adapter (El adaptador/traductor): Permite que dos objetos que no "hablan el mismo idioma" (tienen diferentes formas de funcionar) puedan trabajar juntos. Actúa como un traductor.
Ejemplo: Hay un "Enchufe Viejo" y un "Aparato Nuevo" que solo encaja en "enchufes nuevos". Un AdaptadorDeEnchufe (como los que usas para viajar) permite que el Aparato Nuevo use el Enchufe Viejo.
-Strategy (Comportamiento): Múltiples formas de hacer algo. Permite cambiar la forma en que un objeto hace algo sin cambiar el objeto en sí. Es como tener varias estrategias para resolver un problema y elegir una en el momento.
Ejemplo: Un "Sistema de Envíos" que puede usar diferentes métodos de envío: "Envío en Moto", "Envío por Camión" o "Envío por Avión". El sistema elige la estrategia de envío que necesita sin tener que reescribir su código cada vez.

### Ejercicio 3:
Piense en 3 problemas habituales de su vida diaria en los cuales podría aplicar patrones de diseño
### Ejercicio 4:
Los patrones de diseño suelen poseer distintos nombres o denominaciones. Busque y arme una tabla con
los posibles distintos nombres usados.
### Ejercicio 5:
¿Qué son los antipatrones de diseño? Ejemplifique algunos casos.
### Ejercicio 6 (opcional):
Investigue el uso de otras buenas prácticas, como por ejemplo SOLID.
