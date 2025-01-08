# Generador de Memes

Este es un proyecto simple de generador de memes desarrollado con Flask. Permite a los usuarios subir una imagen y agregar texto en la parte superior e inferior para crear memes personalizados.

## Estructura del Proyecto

```plaintext
Meme/
├── static/
│   └── fonts/
│       └── Roboto-Regular.ttf  # Fuente para los textos del meme
├── templates/
│   └── index.html              # Página principal con el formulario de generación
├── app.py                      # Aplicación Flask principal
```

## Requisitos

    Python 3.10 o superior
    Flask
    Pillow

## Instalación

    Clona este repositorio:

git clone https://github.com/israelubeda/meme-generator.git
cd meme-generator

Crea un entorno virtual y actívalo:

python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

Instala las dependencias:

    pip install flask pillow

    Asegúrate de que la fuente Roboto-Regular.ttf esté en la carpeta static/fonts/.

Ejecución

    Ejecuta la aplicación Flask:

python app.py

Abre tu navegador y visita:

    http://127.0.0.1:5000

    Sube una imagen, agrega texto y genera tu meme. El archivo generado se descargará automáticamente.

## Personalización

Puedes personalizar el proyecto:

    Cambia la fuente en static/fonts/ y actualiza la ruta en app.py.
    Modifica el diseño de la página principal en templates/index.html.

## Capturas de Pantalla
Formulario

Meme Generado

Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.


---

### **Instrucciones Adicionales**
1. **Agrega capturas de pantalla**:
   - Sube ejemplos de memes generados al repositorio y actualiza las rutas en la sección "Capturas de Pantalla".

2. **Sube a GitHub**:
   - Si deseas que otros puedan colaborar o usar este proyecto, considera subirlo a GitHub:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git remote add origin https://github.com/tu-usuario/meme-generator.git
     git push -u origin main
     ```

