# Talentum Flask Tutorial: Haciendo un blog

##Descargar y configurar el proyecto

Link a las diapositivas: [https://slides.com/javierlunamolina/talentum-flask-tutorial](https://slides.com/javierlunamolina/talentum-flask-tutorial)

###Con git (versión que mola)
1. Haz un fork del proyecto en tu cuenta (Opcional, pero así puedes continuar añadiéndole cosas después)
2. Clona el repositorio ``` git clone urldetuproyecto talentum-flask-tutorial``` o usa la url de mi proyecto (```https://github.com/JavierLuna/talentum-flask-tutorial.git```) si decides no hacer tu propio fork.

3. Métete en la carpeta del proyecto que acabas de clonar (talentum-flask-tutorial) y crea un entorno virtual ``` virtualenv env```
4. Una vez creado, activarlo ```source env/bin/activate``` (o ```\env\Scripts\activate``` si estás en windows, o vete a [Ubuntu.com](https://www.ubuntu.com/) e instala un sistema operativo de verdad)
5. Una vez activado, instalaremos en él las librerias que usaremos ``` pip install -r requirements.txt ```



###Sin git (para seres despiadados y sin corazón)
1. Descárgate el zip con el código
2. Ir al paso 2 de la versión con git

Puedes ver los cambios que he ido realizando directamente en Github.


##Cómo usar el proyecto (si has usado git)
En el proyecto se han usado etiquetas por cada "versión" usada en las diapositivas. Si no estás siguiendo las diapositivas, en la sección "Tags" puedes encontrar la correspondencia entre las etiquetas y los cambios que he ido añadiendo.

##Tags
Uso: ``` git checkout etiqueta ``` 
Ejemplo: ```git checkout 01``` va a "Estructura"

Si navegando por las etiquetas la lías y no te deja hacer checkout: ``` git reset --hard ```

* **01 - Estructura**: Creamos la estructura y los ficheros sobre los que trabajaremos a continuación
* **02 - Configuraciones**: Estructuramos las diferentes configuraciones (dev, test, prod...) que queremos para nuestro blog
* **03 - App Factory**: Usamos un Factory de aplicaciones para hacer nuestro servidor un pelín más escalable
* **04 - Flask-SQLAlchemy**: Usamos SQLAlchemy para añadir los modelos de Post, User y Tag
* **05 - Falseando datos**: Usaremos Forgerypy para generar datos falsos, útil para desarrollo
* **06 - manage.py**: Añadimos contextos y comandos a nuestro script de gestión
* **07 - Vistas**: Usamos templates para diseñar la portada de nuestro blog, la vista detallada de un post y usamos una Blueprint para añadirlas a nuestra aplicación
* **08 - Creando Posts**: Crearemos un formulario y una vista para añadir Posts al sistema y adaptamos nuestras vistas para el uso de flash()
* **09 - Flask-Login**: Configuramos nuestro sistema de sesiones de usuario en una Blueprint distinta y protegemos las rutas que queramos
* **10 - Actualizamos vistas**: Actualizamos las vistas que teníamos para hacer uso de algunas características importantes de Flask-Login 
* **11 - Paginación**: Añadimos un sistema de paginación para no listar siempre todos los posts del blog
* **12 - REST API**: Diseñamos una REST API para el CRUD de posts de nuestro blog. Además, protegemos los endpoints que nos interesan con usuario y contraseña.

##¿Qué hacer una vez hayas terminado?
¡Genial! Espero que hayas aprendido un poco de Flask conmigo y que te hayas interesado al menos un poquito en esta framework (porque mola un montón).

Como habrás pensado a este blog le faltan algunas cosillas:

* Páginas para los usuarios
* Que cada usuario tenga foto, descripción... Y que pueda editar todos esos campos.
* Que un usuario pueda editar sus propios posts
* Interfaz más bonita (soy pésimo diseñando)
* Que un comentario pueda responder a otro comentario
* Búsqueda de posts por título
* Roles (Superuser, moderador, escritor...)

Es lo que se me pasa por la cabeza ahora mismo, pero seguro que a ti se te ocurren otras ideas mucho mejores.

Si te has quedado con ganas de seguir aprendiendo Flask, te recomiendo encarecidamente el [blog de Miguel Grinberg](https://blog.miguelgrinberg.com), en concreto el [Flask-MegaTutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). Trata algunas cosas que aquí no hemos dado y merece la pena leerlo.

Además de su blog Miguel ha dado charlas sobre Flask en casi todas las PyCon, aquí están mis favoritas:

* [Flask by example](https://www.youtube.com/watch?v=FGrIyBDQLPg)
* [Writing RESTful web services with Flask](https://www.youtube.com/watch?v=px_vg9Far1Y)
* [Flask at Scale](https://www.youtube.com/watch?v=tdIIJuPh3SI) (un pelín más avanzado)

Y lo que te recomiendo sobre todo es: 

####Haz tus proyectos, practica y documéntate, es como mejor se aprende.



##Librerías usadas
* [Flask](http://flask.pocoo.org/): Flask es una microframework web para Python basada en Werkzeug, Jinja 2 y buenas intenciones
* [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap): Complemento para el uso de [Bootstrap](https://getbootstrap.com/) en Flask de forma fácil
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/): Wrapper de SQLAlchemy para su uso sencillo en Flask
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/): Complemento para el uso de [WTForms](https://wtforms.readthedocs.io/en/latest/) en Flask
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/): Manager de sesiones en Flask
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/): Migraciones para SQLAlchemy basadas en [Alembic](http://alembic.zzzcomputing.com/en/latest/)
* [Flask-Script](https://flask-script.readthedocs.io/en/latest/): Escribir scripts usando Flask nunca había sido tan fácil
* [ForgeryPy](https://tomekwojcik.github.io/ForgeryPy/): Falsear datos like a pro
* [python-slugify](https://github.com/un33k/python-slugify): Convertir texto en slug