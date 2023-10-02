# Anaconda

Anaconda es una plataforma de distribución de código abierto que se utiliza para el desarrollo y gestión de paquetes en el lenguaje de programación Python. Esta herramienta, creada por Continuum Analytics, proporciona un entorno completo y fácil de usar para científicos de datos y desarrolladores, permitiendo la instalación rápida y sencilla de paquetes y librerías esenciales para el análisis de datos, la visualización y la creación de modelos predictivos. 

Además, Anaconda incluye un gestor de ambientes virtuales que ayuda a mantener proyectos independientes y aislados, evitando conflictos entre distintas versiones de paquetes. En resumen, Anaconda es una herramienta imprescindible para aquellos que trabajan con Python en el campo del análisis de datos, proporcionando una base sólida y eficiente para su trabajo.

Aquí tienes una guía paso a paso para utilizar Miniconda con la línea de comandos y crear ambientes virtuales:

1. Descarga Miniconda:
   - Ve al sitio web oficial de Miniconda: https://docs.conda.io/en/latest/miniconda.html
   - Elige la versión adecuada para tu sistema operativo (Windows, macOS o Linux).
   - Descarga el instalador y ejecútalo.

2. Instala Miniconda:
   - Sigue las instrucciones del instalador y acepta los términos de licencia.
   - Elige la ubicación de instalación (puedes dejarla por defecto).
   - Asegúrate de marcar la opción "Agregar Anaconda al PATH" durante la instalación para poder usar Conda desde cualquier directorio en la línea de comandos.

3. Abre una terminal o línea de comandos:
   - En Windows, abre el menú Inicio, busca "Anaconda Prompt" y haz clic en él.
   - En macOS o Linux, abre una terminal.

4. Crea un nuevo ambiente virtual:
   - Ejecuta el siguiente comando para crear un nuevo ambiente virtual con el nombre "myenv":
     ```sh
     conda create --name myenv
     ```

5. Activa el ambiente virtual:
   - Ejecuta el siguiente comando para activar el ambiente virtual recién creado:
     ```sh
     conda activate myenv
     ```

6. Instala paquetes en el ambiente virtual:
   - Utiliza el siguiente comando para instalar paquetes en el ambiente virtual activado:
     ```sh
     conda install nombre_paquete
     ```
   - Utiliza el siguiente comando para instalar paquetes en el ambiente virtual activado con pip:
     ```sh
     pip install nombre_paquete
     ```

7. Desactiva el ambiente virtual:
   - Cuando hayas terminado de trabajar en tu ambiente virtual, puedes desactivarlo ejecutando el siguiente comando:
     ```sh
     conda deactivate
     ```

8. Elimina el ambiente virtual:
   - Si ya no necesitas un ambiente virtual, puedes eliminarlo ejecutando el siguiente comando:
     ```sh
     conda remove --name myenv --all
     ```

Para generar el respaldo del ambiente de anaconda que se quiere compartir se requiere lo siguiente:

1. Abre una terminal o línea de comando.
2. Navega hasta el directorio donde está ubicado el ambiente de Anaconda que deseas respaldar.
3. Ejecuta el siguiente comando para generar un archivo YAML que contiene la información del ambiente:

   ```sh
   conda env export -f environment.yml
   ```
	donde la bandera `-f` significa que el resultado lo guardará en el archivo `environment.yml`

5. Ahora puedes compartir el archivo `environment.yml`  con otras personas para que puedan recrear tu ambiente de Anaconda en sus propias máquinas.

Para recrear el ambiente a partir del respaldo, la otra persona debe seguir estos pasos:

1. Descargar los archivos environment.yml y packages.txt.
2. Abrir una terminal o línea de comando.
3. Navegar hasta el directorio donde se encuentran los archivos descargados.
4. Ejecutar el siguiente comando para crear un nuevo ambiente basado en el archivo YAML:

   ```sh
   conda env create -f environment.yml
   ```

Una vez finalizados estos pasos, la otra persona tendrá un ambiente de Anaconda idéntico al que respaldaste.

1. Tener instalado Anaconda en el sistema.
2. Abrir el Anaconda Navigator.
3. Seleccionar el ambiente que se desea respaldar en la pestaña "Environments".
4. Hacer clic en el botón de "Export" que se encuentra junto al nombre del ambiente.
5. Guardar el archivo de respaldo en una ubicación deseada con un nombre descriptivo (por ejemplo, "my_env_backup.yml").
6. Compartir el archivo de respaldo con las personas con las que se desea compartir el ambiente de Anaconda.

Para utilizar el respaldo del ambiente de Anaconda:

1. Tener instalado Anaconda en el sistema.
2. Abrir una terminal o línea de comandos.
3. Navegar a la ubicación donde se encuentra guardado el archivo de respaldo del ambiente (por ejemplo, mediante el comando `cd`).
4. Ejecutar el siguiente comando para crear un nuevo ambiente a partir del respaldo:

   ```sh
   conda env create -f my_env_backup.yml
   ```

   Donde `my_env_backup.yml`es el nombre del archivo de respaldo.

5. Esperar a que la creación del nuevo ambiente finalice.
6. Activar y utilizar el nuevo ambiente mediante los comandos habituales, como `conda activate my_env` o `source activate my_env` dependiendo del sistema operativo.

De esta manera, se podrá compartir y utilizar un respaldo completo del ambiente de Anaconda con otras personas sin tener que instalar las mismas dependencias y configuraciones manualmente.
