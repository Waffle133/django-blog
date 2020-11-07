# Guía para montar proyecto Django en MacOs 

# Preparando entorno

## Configuración de entorno
Nos aseguramos que tengamos `Python 3` instalado con el siguiente comando:
```sh
python3
```
Esto nos debería de abrir el CLI de `Python 3`.  
En el caso contrario procedemos a descargar [Python3](https://www.python.org/) desde su página oficial.  

Teniendo instalado `Python 3` procedemos a verificar la instalación de `pip` usando el comando:
```sh
pip3
```
Verificaremos que el comando esté instalado si esto nos arroja la lista de comandos disponibles.
En caso de no tener `pip` en nuestra máquina lo instalamos mediante:
```sh
curl -O https://bootstrap.pypa.io/ez_setup.py
python3 ez_setup.py
```
Para instalar las setuptools de `Python` y:
```sh
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
```  
Para finalmente instalar `pip`

#Guía para montar proyecto Django en Windows
 ## Configuración de entorno
 Usando PowerShell de Windows comprobamos si tenemos instalado `Python 3` usando el comando: 
  ```sh
python3
```
Esto nos debería de abrir el CLI de `Python 3`.  
En el caso contrario procedemos a descargar [Python3](https://www.python.org/) desde su página oficial.

## Creacion de entorno virtual con Python
Vamos a crear un entorno virtual para nuestro proyecto, el cual contendra todas las dependencias que exclusivas del proycto. Para crearlo ejecutamos:

```
python -m venv venv
```

o bien
```
python -m venv .env
```
si lo queremos en una carpeta escondida.


## Comandos del entorno

Para **activar** nuestro entorno ejecutamos:

```
source .env/bin/activate
```

Si estamos en Windows entonces ejecutamos:
```
./.env/Scripts/activate
```



Y para **desactivarlo**

```
deactivate
```

Si queremos **listar las librerias instaladas** usamos

```
pip freeze
```

## Instalación de Django
Para **instalar** la ultima version de Django ejecutamos

```
pip install django -U
```

## Django Admin
Es una interfaz instalada junto con Django que contiene subcomandos que utiles. Para listar los subcomandos utilizamos

```
django-admin
```

## Creación de proyecto
Para **crear** un proyecto ejecutamos

```
django-admin startproject admin-panel .
```

## Instalando pipenv
Pipenv es una alternativa para crear nuestros entornos de desarrollo, para instalarlo usamos:  

`pip install pipenv`

Una vez instalado podemos usarlo globalmente como `pipenv`  

Ya que lo tenemos configurado entramos a la raíz de nuestro proyecto y generamos un entorno virutal para `Python 3` con:  

`pipenv --three`  

y usando  

`pipenv install django`  

instalamos django dentro de nuestro entorno.

Para activar nuestro entorno ejecutamos:  

`pipenv shell`  



https://github.com/toml-lang/toml  

https://platzi.com/tutoriales/1104-python/2292-pipenv-virtualenv-y-pip-en-un-solo-comando/

https://www.w3.org/Provider/Style/URI

https://docs.djangoproject.com/en/3.0/ref/templates/builtins/




