import serial
import dbus

player = dbus.SessionBus().get_object('org.kde.amarok', '/Player', 'org.freedesktop.MediaPlayer')
# Estou usando Amarok, mas voce pode usar outros players, como VLC, por exemplo
serial = serial.Serial('/dev/ttyACM0')
# Verifique qual a porta serial voce esta usando, por exemplo, /dev/ttyACM1 ou COM1

playing = False

def play():
    player.Play() 
    playing = True

def pause():
    player.Pause()
    playing = False
    
def ler_porta_serial():
    while serial.read():
        if playing:
            pause()
        else:
            play()
 
ler_porta_serial()

