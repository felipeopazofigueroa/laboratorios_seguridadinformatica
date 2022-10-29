IMPORTANTE

Primero se deben instalar las siguientes librerias mediante el cmd utilizando el siguiente comando (sin las "")
Esto con el propósito de utilizar los módulos del cifrado DES, 3DES y AES

"python -m pip install pycryptodome"
"python -m pip install pycryptodomex"
"python -m pip install pycryptodome-test-vectors"

También para la depuración paralela de ambos programas Cliente/Servidor y el desarrrollo en general del código, 
se usó el entorno de desarrollo "Visual Studio Code", por lo que se recomienda usar este para poder probarlo.

Para correr el programa, se debe depurar primero "servidor.py", y luego "cliente.py", de esta forma inicia la conexión
de "Cliente-Servidor".

Nota: En la ejecución del codigo, se escriben los mensajes tanto cifrados como descifrados 
en un txt en formato BYTES, por lo que dentro del codigo se va trabajando con este formato
y se va convirtiendo en STRING para que el usuario vea al ejecutar el código el respectivo
mensaje cifrado en ASCII, así como el mensaje descifrado en texto plano.

Nota2: "nonce.txt" guarda un nonce, correspondiente a una secuencia aleatoria de bytes para así utilizarla
en el proceso de descifrado posterior para cada cifrado, con el proposito de asegurar autenticidad.