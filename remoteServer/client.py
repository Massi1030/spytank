import network
import click


ADDRESS ="10.0.0.0.113"
PORT=1111

print("z : avance\nq : gauche\ns : reculer\nd : droite\ne/r : led\na : stop\nc : exit")
print("entre une lettre pour piloter le robot comme dans la description")

continuer = True
while continuer

while True:

    socket = network.newClientSocket()
    socket.connect((ADDRESS,PORT))

    print("z : avance\nq : gauche\ns : reculer\nd : droite\ne/r : led\na : stop\nc : exit")
    print("entre une lettre pour piloter le robot comme dans la description")
   
    lettre = click.getchar()

  
    socket.send(lettre.encode())
    reponse = socket.recv(4096)
   
    print(reponse)
    
    if lettre == "c" :
        continuer = False

