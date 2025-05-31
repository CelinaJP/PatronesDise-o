### Pereyra Celina Jazmin


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

### Respuesta 2:
-Singleton (UNICA INSTANCIA) : Asegura que una clase solo tenga una única "copia" en todo el programa. Si intentas crear otra, te da la misma que ya existe.
Ejemplo: programa "Gerente de Log". Solo quiero un gerente que anote todo lo que pasa. Con Singleton, siempre voy a usar el mismo gerente, no importa cuántas veces intento "crear" uno nuevo.
-Adapter (El adaptador/traductor): Permite que dos objetos que no "hablan el mismo idioma" (tienen diferentes formas de funcionar) puedan trabajar juntos. Actúa como un traductor.
Ejemplo: Hay un "Enchufe Viejo" y un "Aparato Nuevo" que solo encaja en "enchufes nuevos". Un AdaptadorDeEnchufe (como los que usas para viajar) permite que el Aparato Nuevo use el Enchufe Viejo.
-Strategy (Comportamiento): Múltiples formas de hacer algo. Permite cambiar la forma en que un objeto hace algo sin cambiar el objeto en sí. Es como tener varias estrategias para resolver un problema y elegir una en el momento.
Ejemplo: Un "Sistema de Envíos" que puede usar diferentes métodos de envío: "Envío en Moto", "Envío por Camión" o "Envío por Avión". El sistema elige la estrategia de envío que necesita sin tener que reescribir su código cada vez.

### Ejercicio 3:
Piense en 3 problemas habituales de su vida diaria en los cuales podría aplicar patrones de diseño
Piensa en 3 problemas comunes donde podrías usar patrones:

### Respuesta 3:
-Manejar notificaciones: Tu aplicación puede enviar mensajes por email, SMS o WhatsApp.
Patrón: Strategy. Elige la forma de enviar el mensaje (email, SMS, etc.) según lo necesites, sin cambiar el código principal que envía la notificación.
-Configuración de una app: Solo quieres una única configuración para todo tu programa (idioma, tema, etc.).
Patrón: Singleton. Asegura que solo exista una copia de la configuración en todo tu programa.
-Exportar informes: Generas un informe y lo quieres guardar en PDF, Excel o CSV.
Patrón: Factory Method (o Fábrica). Le dices al programa "quiero un exportador de PDF" y te lo crea, sin que tengas que saber cómo se hace por dentro.

### Ejercicio 4:
Los patrones de diseño suelen poseer distintos nombres o denominaciones. Busque y arme una tabla con
los posibles distintos nombres usados.

 ### Respuesta 4:
- ABSTRACT FACTORY 1. KIT
- FACTORY METHOD 2. VIRTUAL CONSTRUCTOR
- ADAPTER 3. WRAPPER, ENVOLTURA
- DECORADOR 4. WRAPPER
- PROXY 5.SURROGATE
- COMMAND 6. ACTION, TRANSACTION
- ITERATOR 7. CURSOR
- MEMENTO 8. TOKEN
- STATE 9. OBJECTS FOR STATES
- STRATEGY 10. POLICY

### Ejercicio 5:
¿Qué son los antipatrones de diseño? Ejemplifique algunos casos.

### Respuesta 5:
Los antipatrones de diseño son soluciones comunes a problemas recurrentes que, a pesar de parecer efectivas a primera vista, resultan ser ineficientes o contraproducentes, llevando a problemas mayores en el futuro del desarrollo de software. Son, en esencia, "malas prácticas" o "errores a evitar".

-God Object / God Class: Una clase que centraliza demasiada funcionalidad, conoce o controla demasiados otros objetos, y es responsable de una gran parte del sistema. Se vuelve excesivamente grande, difícil de mantener, probar y extender.

-Spaghetti Code: Código con una estructura de control de flujo enrevesada, un gran número de if-else anidados y escasa modularidad. Es muy difícil de leer, entender, depurar y modificar.

-Lava Flow: Código obsoleto o redundante que existe en el sistema pero no se utiliza, o al menos no de manera obvia. Se mantiene porque se teme que eliminarlo pueda romper algo, pero nadie sabe realmente qué hace o si es realmente necesario.

### Ejercicio 6 (opcional):
Investigue el uso de otras buenas prácticas, como por ejemplo SOLID.

### Respuesta 6:
Interface Segregation Principle (ISP - Principio de Segregación de Interfaces): Los clientes no deben ser forzados a depender de interfaces que no utilizan. Es mejor tener muchas interfaces pequeñas y específicas que una sola interfaz grande y general.

Ejemplo (Malo): Una interfaz Worker con métodos work(), eat(), sleep(), manage_team(), code(). Un RobotWorker que implementa Worker se vería obligado a implementar manage_team() y code() incluso si no tiene esas capacidades.
Ejemplo (Bueno): Interfaces más específicas como Workable, Eatable, Sleepable, Manager, Coder. HumanWorker podría implementar Workable, Eatable, Sleepable, Manager, Coder. RobotWorker solo implementaría Workable y Sleepable.
