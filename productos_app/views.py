from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static

# Create your views here.
def index(request):
    return render(request, 'webproductos/index.html')
def usuario(request):
    document = """
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Cuadro de Usuario</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f5f5f5;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                     margin: 0;
                    }
        
                    .user-box {
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 20px;
            width: 300px;
            text-align: center;
                        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    }

                    .user-avatar {
                        width: 100px;
                        height: 100px;
                        border-radius: 50%;
                        background-color: #007BFF;
                        color: #fff;
                        font-size: 24px;
                        line-height: 100px;
                        margin: 0 auto 10px;
                    }
        
                    .user-name {
                        font-size: 18px;
                        font-weight: bold;
                        margin-bottom: 10px;
                    }
        
                    .user-email {
                       font-size: 14px;
                        color: #777;
                    }
                    .back-button {
                    position: absolute;
                    top: 10px; /* Ajustar la posición superior según sea necesario */
                    left: 10px; /* Ajustar la posición izquierda según sea necesario */
                    background-color: #007BFF;
                    color: #fff;
                    border: none;
                    padding: 5px 10px;
                    border-radius: 5px;
                    cursor: pointer;
                    }
                </style>
            </head>
            <body>
                
                <div class="user-box">
                    <div><a href="/"><button class="back-button">VOLVER</a></div>
                    <div class="user-avatar">M</div>
                    <div class="user-name">Marco Roa Lagos</div>
                    <div class="user-email">marco.roa04@inacapmail.cl</div>
                </div>
            </body>
            </html>"""
    return HttpResponse(document)

def juegos(request):
    data={"url1":"mk1/",
          "url2":"ratchet&clank/",
          "url3":"spiderman2/",
          "url4":"gow/",
          "titulo":"Video Juegos",
          "foto1":"mk1.png",
          "foto2":"ratchet.png",
          "foto3":"spiderman2.png",
          "foto4":"gow.png",
          "producto1":"Mortal Kombat 1",
          "producto2":"Ratchet & Clank Rift Apart",
          "producto3":"Spide-Man 2",
          "producto4":"God of War Ragnarok"
          }
    return render(request, 'webproductos/productos.html',data)

def figuras(request):
    data={
          "url1":"ashe/",
          "url2":"alien/",
          "url3":"genio/",
          "url4":"skeletor/",  
          "titulo":"Figuras",          
          "foto1":"ashe.jpg",
          "foto2":"alien.jpg",
          "foto3":"genio.jpg",
          "foto4":"skeletor.jpg",
          "producto1":"Figura Nendoroid Ashe",
          "producto2":"Figura Nendoroid Alien",
          "producto3":"Figura Nendoroid Genie",
          "producto4":"Figura Nendoroid Skeletor"
          }
    return render(request, 'webproductos/productos.html',data)


def juegosmesa(request):
    data={"titulo":"Juegos De Mesa",  
          "url1":"catan/",
          "url2":"dixit/",
          "url3":"kittens/",
          "url4":"burrito/",        
          "foto1":"catan.jpg",
          "foto2":"dixit.jpg",
          "foto3":"kittens.jpg",
          "foto4":"burrito.jpg",
          "producto1":"Catan",
          "producto2":"Dixit",
          "producto3":"Exploting Kittens",
          "producto4":"Throw Throw Burrito"
          }
    return render(request, 'webproductos/productos.html',data)



def mk1(request):
    data={
          "descripcion1":"Plataforma: PS5",
          "descripcion2":"Desarrollador: Warner Bros",
          "descripcion3":"Clasificacion: Mature 17+",
          "descripcion4":"Descubre un nuevo universo de Mortal Kombat creado por Liu Kang, Dios del Fuego. ¡Mortal Kombat 1 abre paso a una nueva era de esta icónica saga con un nuevo sistema de kombate, modos de juego y fatalities!",
          "volver":"/juegos"
          }
    return render(request, 'webproductos/descripcion.html',data)
def ratchet(request):
    data={"descripcion1":"Plataforma: PS5",
          "descripcion2":"Desarollador: Sony",
          "descripcion3":"Clasificacion: Everyone 10+",
          "descripcion4":"Salta entre dimensiones con Ratchet y Clank mientras enfrentan a un malvado emperador de otra realidad. Salta entre mundos repletos de acción y más allá a velocidades alucinantes, completo con un arte deslumbrante y un arsenal demencial, mientras los aventureros intergalácticos se abren paso a la consola PS5™"
          ,"volver":"/juegos"}
    return render(request, 'webproductos/descripcion.html',data)

def spiderman2(request):
    data={"descripcion1":"Plataforma: PS5",
          "descripcion2":"Desarrollador: Sony",
          "descripcion3":"Clasificacion: Teen",
          "descripcion4":"El próximo juego de la franquicia de Marvel's Spider-Man llega a la consola PlayStation®5. Marvel's Spider-Man 2 es el próximo juego de la franquicia Marvel's Spider-Man para PlayStation, aclamada por la crítica. Desarrollado por Insomniac Games para la consola PlayStation®5 en colaboración con PlayStation y Marvel Games"
          ,"volver":"/juegos"}
    return render(request, 'webproductos/descripcion.html',data)

def gow(request):
    data={"descripcion1":"Plataforma: PS5",
          "descripcion2":"Desarrollador: Sony",
          "descripcion3":"Clasificacion: Mature 17+",
          "descripcion4":"Kratos y Atreus se embarcan en una mítica aventura en busca de respuestas y aliados antes de la llegada del Ragnarök.Desde Santa Monica Studio llega la secuela del aclamado por la crítica God of War (2018). Kratos y Atreus deberán viajar a cada uno de los nueve reinos en busca de respuestas para prepararse para la vaticinada batalla que acabará con el mundo.Juntos, Kratos y Atreus se aventuran en cada uno de los nueve reinos en busca de respuestas mientras las fuerzas de Asgard se preparan para la guerra. A lo largo del camino, explorarán asombrosos paisajes mitológicos, reunirán aliados de los reinos y se enfrentarán a temibles enemigos con forma de monstruos y dioses nórdicos.A medida que se acerca la amenaza del Ragnarök, Kratos y Atreus tendrán que elegir entre la seguridad de su familia y la de los reinos..."
          ,"volver":"/juegos"}
    return render(request, 'webproductos/descripcion.html',data)

def ashe(request):
    data={"descripcion1":"Altura: 10cm aprox",
          "descripcion2":"Desarrollador: Good Smile Company",
          "descripcion3":"Origen: League of Legends",
          "descripcion4":"¡Del mundialmente popular juego 'League of Legends' llega un Nendoroid de Ashe, La arquera del invierno! Viene con tres caras: una expresión estándar seria, una expresión de combate y una expresión sonriente y segura.Ashe viene con su arco, una flecha y un espíritu de halcón como piezas opcionales. También se incluye una parte del efecto Enchanted Crystal Arrow. ¡Disfruta creando intensos escenarios de batalla en forma Nendoroid!"
          ,"volver":"/figuras"}
    return render(request, 'webproductos/descripcion.html',data)

def alien(request):
    data={"descripcion1":"Altura: 11cm",
          "descripcion2":"Desarrollador: Good Smile Company",
          "descripcion3":"Origen: Alien",
          "descripcion4":"De la película de terror de ciencia ficción 'Alien' llega un Nendoroid del Alien! Si bien el Alien se ha reducido al lindo tamaño de Nendoroid, su apariencia aterradora se ha conservado perfectamente con un modelado increíblemente detallado.La figura está completamente articulada, lo que le permite exhibirla en una variedad de poses diferentes. ¡Las piezas opcionales incluyen un Facehugger, un Chestburster y una hoja con efectos de huevos alienígenas! ¡Disfruta mezclando y combinando piezas opcionales para crear todo tipo de situaciones en forma Nendoroid!"
          ,"volver":"/figuras"}
    return render(request, 'webproductos/descripcion.html',data)

def genio(request):
    data={"descripcion1":"Altura: 12cm aprox",
          "descripcion2":"Desarrollador: Good Smile Company",
          "descripcion3":"Origen: Aladin",
          "descripcion4":"De 'Aladdin' de Disney viene un Nendoroid de Genie! ¡Su apariencia única ha sido capturada y reducida al tamaño de Nendoroid!Viene con una lámpara mágica y un sombrero como piezas opcionales, junto con ojos intercambiables y una mitad inferior intercambiable, lo que te permite recrear fácilmente poses de la película. ¡Asegúrate de agregarlo a tu colección!"
          ,"volver":"/figuras"}
    return render(request, 'webproductos/descripcion.html',data)

def skeletor(request):
    data={"descripcion1":"Altura: 10cm",
          "descripcion2":"Desarrollador: Good Smile Company",
          "descripcion3":"Origen: Masters of the Universe: Revelation",
          "descripcion4":"¡De 'Masters of the Universe: Revelation' llega un Nendoroid de Skeletor! Las piezas opcionales incluyen el bastón Havoc, el bastón moldeador, la espada de poder y el trono de Skeletor. Además, el embalaje interior de cartón de la caja del Nendoroid presenta una imagen de Snake Mountain. ¡Disfruta usándolo como fondo para recrear escenas de la serie en forma Nendoroid!"
          ,"volver":"/figuras"}
    return render(request, 'webproductos/descripcion.html',data)

def catan(request):
    data={"descripcion1":"Edad: Desde los 10 Años",
          "descripcion2":"Idioma: Español",
          "descripcion3":"Duracion: 45 Minutos",
          "descripcion4":"Jugadores: 3-4 jugadores "
          ,"volver":"/juegosmesa"}
    return render(request, 'webproductos/descripcion.html',data)

def dixit(request):
    data={"descripcion1":"Edad: Desde los 8 Años",
          "descripcion2":"Idioma: Español",
          "descripcion3":"Duracion: 30 Minutos",
          "descripcion4":"Jugadores: 3-8 jugadores"
          ,"volver":"/juegosmesa"}
    return render(request, 'webproductos/descripcion.html',data)

def kittens(request):
    data={"descripcion1":"Edad: Desde los 7 Años",
          "descripcion2":"Idioma: Español",
          "descripcion3":"Duracion: 15 Minutos",
          "descripcion4":"Jugadores:2-10 jugadores "
          ,"volver":"/juegosmesa"}
    return render(request, 'webproductos/descripcion.html',data)

def burrito(request):
    data={"descripcion1":"Edad: Desde los 7 Años",
          "descripcion2":"Idioma: Español",
          "descripcion3":"Duracion: 15 Minutos",
          "descripcion4":"Jugadores: 2-6 jugadores"
          ,"volver":"/juegosmesa"}
    return render(request, 'webproductos/descripcion.html',data)