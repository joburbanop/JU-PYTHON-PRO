#PASOS PARA INGRESAR A giyHub
#1. Abre tu navegador web y ve a la página principal de GitHub en www.github.com.
#2. En la página de inicio, verás un botón verde que dice "Sign up" o "Registrarse". Haz clic en ese botón.
#3. Se te pedirá que completes algunos datos, como tu nombre de usuario, dirección de correo electrónico y contraseña. Elige un nombre de usuario único que sea fácil de recordar. Asegúrate de utilizar una dirección de correo electrónico válida y una contraseña segura.
#4. Después de completar tus datos, haz clic en el botón "Sign up" o "Registrarse" para crear tu cuenta.
#5. En la siguiente pantalla, se te pedirá que elijas un plan de GitHub. Puedes elegir entre el plan gratuito o los planes de pago, dependiendo de tus necesidades. Para comenzar, recomiendo seleccionar el plan gratuito.
#6. Una vez que hayas seleccionado tu plan, se te pedirá que completes un breve cuestionario para ayudar a personalizar tu experiencia en GitHub. Puedes optar por completarlo o saltarlo y hacerlo más tarde.
#7. ¡Felicidades! Has creado tu cuenta de GitHub. Ahora tendrás acceso a todas las funciones y herramientas que ofrece la plataforma.

#PASOS PARA CREAR UN REPOSITORIO
#1. En la página principal de GitHub, haz clic en el botón verde "New" o "Nuevo" en la esquina superior derecha de la pantalla.
#2. Se te redirigirá a una nueva página donde podrás configurar los detalles de tu repositorio.
#3. En la sección "Repository name" o "Nombre del repositorio", elige un nombre descriptivo para tu proyecto. Por ejemplo, "Generador de contraseñas" o "Mi primera aplicación web".
#4. Opcionalmente, puedes agregar una descripción breve del proyecto en la sección "Description" o "Descripción".
#5. Puedes elegir si quieres que tu repositorio sea público o privado. Si quieres compartir tu código con otros y recibir contribuciones, selecciona "Public" o "Público". Si prefieres mantener tu código privado, selecciona "Private" o "Privado" (ten en cuenta que los repositorios privados suelen requerir una suscripción de pago).
#6. Una vez que hayas configurado los detalles, haz clic en el botón "Create repository" o "Crear repositorio".
#7. ¡Listo! Has creado tu repositorio en GitHub. Ahora tendrás acceso a la página de inicio del repositorio, donde podrás ver diferentes opciones y configuraciones.

#CODIGO ECHO EN CLASE
import random
datos = ["edad: 17","nombre: nn","mi videojuego favorito es: nn"]
print(random.choice(datos))

#SINTAXIS DE VARAIBLES En Python, los nombres de variables válidos deben seguir ciertas reglas:
#Los nombres de variables pueden contener letras (mayúsculas y minúsculas), dígitos y guiones bajos (_).
#El primer carácter del nombre de la variable no puede ser un dígito.
#Python distingue entre mayúsculas y minúsculas, por lo que mi_variable y Mi_Variable se consideran diferentes.
#Evita utilizar nombres de variables que sean palabras clave reservadas en Python, como print, len, if, etc.
#Se recomienda utilizar nombres descriptivos y significativos para las variables, lo cual ayuda a comprender el propósito de la variable en el código.
mi_variable = 10


#El comando input() se utiliza en Python para recibir la entrada del usuario desde la consola. 

a = input()

#El comando len(a) devuelve la longitud de la lista, es decir, la cantidad de elementos que contiene.
len(datos)

#TIPOS DE DATOS
#1. Números:
#  - `int`: representa enteros, por ejemplo, 1, 100, -10.
#  - `float`: representa números de punto flotante (números decimales), por ejemplo, 3.14, -0.5, 2.0.
# Entero
edad = 25
temperatura = -10

# Punto flotante
pi = 3.1416
altura = 1.85

#2. Cadenas de caracteres:
#   - `str`: representa una secuencia de caracteres, se utilizan comillas simples o dobles para delimitar una cadena, por ejemplo, 'Hola', "Python", "123".
nombre = "Juan"
mensaje = 'Hola, ¿cómo estás?'
direccion = "Calle Principal 123"


#3. Booleanos:
#   - `bool`: representa un valor de verdad, que puede ser `True` (verdadero) o `False` (falso). Este tipo de dato se utiliza en expresiones lógicas y control de flujo.
es_verdadero = True
es_falso = False


#4. Listas:
#   - `list`: representa una colección ordenada y mutable de elementos. Los elementos pueden ser de diferentes tipos y se acceden mediante índices. Se definen utilizando corchetes [], por ejemplo, [1, 2, 3], ['a', 'b', 'c'].
numeros = [1, 2, 3, 4, 5]
colores = ['rojo', 'verde', 'azul']
mezclado = [1, 'dos', True, 3.14]


#5. Diccionarios:
#   - `dict`: representa una colección de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente. Se definen utilizando llaves {} y pares clave-valor separados por dos puntos :, por ejemplo, {'nombre': 'Juan', 'edad': 25}.
persona = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
estudiante = {'nombre': 'María', 'edad': 20, 'carrera': 'Informática'}



