#!/usr/bin/python3

# Importing required module
import subprocess
import paramiko
from getpass import getpass
# Importar el módulo
import json

def conecta_ssh(ip, comando):
    # Inicia un cliente SSH
    ssh_client = paramiko.SSHClient()
    # Establecer política por defecto para localizar la llave del host localmente
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    
    # Conectarse
    ssh_client.connect(ip, 22, 'profesor', clave )
    # Ejecutar un comando de forma remota capturando entrada, salida y error estándar
    entrada, salida, error = ssh_client.exec_command(comando)
    # Mostrar la salida estándar en pantalla
    print (salida.read())
    print (error.read())
    # Cerrar la conexión
    ssh_client.close()


# Lee fichero de datos alumnado en formato JSON
with open("alumnado3.json", "r") as j:
    fichero = json.load(j)
#print (fichero['alumnado'][2]['nombre']+' '+fichero['alumnado'][2]['ip'])

clave = getpass('Clave: ')

comando = 'echo '+clave+' | sudo -S apt update && sudo apt install -y pip && sudo apt install -y virtualenvwrapper'
comando +=' && sudo cp /usr/share/virtualenvwrapper/virtualenvwrapper.sh /usr/local/bin/'
comando +=' && export WORKON_HOME=~/Envs && mkdir -p $WORKON_HOME && source /usr/local/bin/virtualenvwrapper.sh'
#conecta_ssh(fichero['alumnado'][2]['ip'],comando)

#for alumnado in fichero['alumnado']:
    #conecta_ssh(alumnado['ip'],comando)

# Using system() method to
# execute shell commandj
#subprocess.Popen('ssh profesor@172.26.41.55', shell=True)

