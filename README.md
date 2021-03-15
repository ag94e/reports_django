# Simulando reportes en línea con Django

_Usando Django se creó una página para un proyecto escolar, en el que consiste en hacer un crud sobre inventarios de una empresa._

### Pre-requisitos 📋

_Requerimientos mínimos para el uso de este proyecto_

```
Django 3.x.x
Python 3
virtualenv (este último para utilizar entornos virtuales)
```

### Instalación 🔧

_Para la instalación se requiere hacer los siguientes pasos._

```
virtualenv python3 .env (se crea el entorno virtual .env)
source .env/bin/activate (activamos el entorno virtual)
pip install -r requirements.txt (instalamos con pip todo lo necesario en el archivo requirements.txt)
```

### Despliegue 📦

_Para el despliegue de modo local utilizando Django._

```
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver
```
_Así se podra observar la página corriendo en el localhost._

### Autor 

* **Antonio Guerrero** - [Github](https://github.com/ag94e)

### Referencias

* [Documentación Django](https://docs.djangoproject.com/en/3.1/ref/)

### Licencia

* [MIT](https://opensource.org/licenses/mit-license.php)