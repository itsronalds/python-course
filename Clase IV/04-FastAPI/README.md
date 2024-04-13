# fastapi

# ¿Qué es un entorno virtual (venv)?

Un entorno virtual es un contenedor de Python donde guardamos todas las dependencias de nuestro proyecto, de esta manera evitamos guardar las dependencias instaladas dentro de la inslación Python de nuestra PC.

- Para crear un entorno virtual, ejecutar el siguiente comando en la raíz de nuestro proyecto:

```$
# python -m venv <nombre de nuestro venv>

# Ejemplo:

python -m venv venv
```

- Ahora necesitamos activar nuestro entorno virtual, esto lo logramos con los siguientes comandos:

```$
# En Windows
venv\Scripts\activate

# En Linux
venv/bin/activate
```

- Para desactivar nuestro entorno ejecutamos el siguiente comando:

```$
# En Windows
venv\Scripts\deactivate

# En Linux
venv/bin/deactivate
```

# Instalando FastAPI

Luego de tener nuestro entorno virtual y activarlo correctamente debemos instalar **FastAPI** con el siguiente comando:

```$
pip install fastapi
```

- Luego de instalar FastAPI necesitamos instalar nuestro servidor para ejecutar apps de FastAPI llamado **Uvicorn**:

```$
pip install uvicorn
```

# Iniciar nuestra app

- Primero necesitamos crear nuestro archivo main donde tendremos la instancia y origen de nuestra app:

```$
# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def message():
    return 'Hello World'
```

- Luego, para iniciar nuestra app ejecutamos el siguiente comando:

```$
uvicorn main:app
```

# Hot reload en FastAPI utilizando Uvicorn

Iniciar nuestra app de la forma anterior es correcto, pero que pasa si al agregar cambios a nuestro server este parece no tomarlos? 🤔

Esto lo solucionamos con una opción en nuestro servidor de Uvicorn:

```$
uvicorn main:app --reload
```

Con el comando --reload cada vez que implementemos un cambio nuestro servidor se reiniciará automáticamente.

> Esto solo se utiliza en **desarrollo**, no es **producción**

# Cambiar el puerto por donde se ejecuta nuestra app

Esto se logra ejecutando el siguiente comando:

```$
uvicorn main:app --reload --port 5000
```

# ¿Cómo hacer que nuestro servidor sea accesible para todos los dispositivos de nuestra red?

Esto se logra a través de otra bandera llamada host:

```$
uvicorn main:app --reload --port 5000 --host 0.0.0.0
```

# Generar documentación automática con Swagger en FastAPI

Para generar una documentación de Swagger para nuestra REST API tenemos que ir al navegador y colocar la url raíz de nuestro proyecto, por ejemplo:

```$
http://localhost:5000/docs
```

Esto lo redireccionará a una documentación REST API creada utilizando Swagger

> [Swagger](https://swagger.io/) es un servicio basado en el estandar OPEN API que nos permite diseñar y construir REST API's
