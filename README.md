# ITAM - Maestría en Ciencia de Datos

Repo para trabajos y tareas de la Maestría en Ciencia de Datos del ITAM


## Instancia gratuita de AWS - EC2

Para algunas asignaturas del programa es necesario tener una instancia de AWS-EC2. Para ello el ITAM pone a disposición una **cuenta estudiantil** con la cual no es necesario registrar información bancaria en el portal de AWS. Sin embargo, también existe la posibilidad de utilizar **clusters gratuitos** que permiten satisfacer los requerimientos de dichas asignaturas y que, desde mi punto de vista, tienen mayor respaldo documental en AWS así como soporte de la comunidad.

### Lanzamiento de la instancia
Es necesario ingresar a la [consola de AWS](https://aws.amazon.com/es/console/) y seguir los siguientes pasos:
1) Crear un usuario de AWS e iniciar sesión en la consola
2) Verificar en la esquina superior derecha la región de AWS, en mi caso: **N. Virgina** `us-east-1`
3) Usar la barra de navegación para buscar y seleccionar el servicio EC2
4) Seleccionar la opción `instancias`, al principio no se mostrarán instancias activas
5) Seleccionar el botón `Lanzar instancia`, esto va a redirigir a la pestaña de configuración de la instancia
6) Configurar la instancia de EC2, la configuración que yo utilicé es la siguiente:
    * Tipo: `Amazon Linux`
    * AMI: `Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type`
    * Arquitectura: `64 bits (x86)`
    * Instancia. `t2.micro`
    * Par de claves: Generé un par nuevo con valores `default` </br>**IMPORTANTE**: Guardar el archivo `.pem` que se genera al crear un nuevo par de claves
    * Red: valores default
    * Almacenamiento: valores default, `1x 8 GiB, gp2`
    * Avanzados: `none`
7) Finalmente, a la derecha se muestra el resumen de la instancia, seleccionar el botón `Lanzar instancia`. El lanzamiento de la instancia toma de 5-10 mins.
    
Para la descripción general de los pasos anteriores me basé en el siguiente [video](https://www.youtube.com/watch?v=a8CBE_WN7rA)

### Conexión a la instancia con WSL2
En general me fue suficiente con seguir los pasos descritos en la [guía de AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/WSL.html)
