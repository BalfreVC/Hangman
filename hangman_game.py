import pickle
import random
from os import system, name
from time import sleep, time
from datetime import datetime

score = 0 
FILENAME = "TopScores.pkl"

BANNER_WELCOME = """
                   ______________________________________
          ________|                                      |_______
          \       | Welcome to Hangman game . . .        |      /
           \      | Choose a category to start.          |     /
           /      |______________________________________|     \\
          /__________)                                (_________\\
"""

BANNER_HANGMAN = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
"""
IMAGES = [
    """      _______
     |/      |
     |      
     |      
     |      
     |      
     |
 bvc_|___""", 
 """      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 bvc_|___""",
 """      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 bvc_|___""",
 """      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 bvc_|___""",
 """      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 bvc_|___""",
 """      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 bvc_|___""",
 """      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
 bvc_|___""",
 """      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 bvc_|___"""]


# define our clear function
def clearScreen():
    if name == 'nt': # for windows
        _ = system('cls')
    else: # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


def show_categories(): 
    CATEGORIES = """
1.- C i t i e s 
2.- F r u i t s 
3.- C o l o r s 
4.- B e s t   S c o r e s
5.- E x i t
"""
    print(CATEGORIES)


def get_word(category): 
    WORD_LIST = []
    if category==1: # Cities
        WORD_LIST = ["Tijuana", "Ecatepec", "León", "Puebla", "Ciudad Juárez", "Guadalajara", "Zapopan", "Monterrey", "Ciudad Nezahualcóyotl", "Chihuahua", "Mérida", "Naucalpan", "Cancún", "Saltillo", "Aguascalientes", "Hermosillo", "Mexicali", "San Luis Potosí", "Culiacán", "Querétaro", "Morelia", "Chimalhuacán", "Reynosa", "Torreón", "Tlalnepantla", "Acapulco", "Tlaquepaque", "Guadalupe", "Durango", "Tuxtla Gutiérrez", "Veracruz", "Ciudad Apodaca", "Ciudad López Mateos", "Cuautitlán Izcalli", "Matamoros", "General Escobedo", "Irapuato", "Xalapa", "Tonalá", "Mazatlán", "Nuevo Laredo", "San Nicolás de los Garza", "Ojo de Agua", "Xico", "Celaya", "Tepic", "Ixtapaluca", "Cuernavaca", "Villahermosa", "Ciudad Victoria", "Ensenada", "Ciudad Obregón", "Ciudad Nicolás Romero", "Soledad", "Ciudad Benito Juárez", "Playa del Carmen", "Santa Catarina", "Gómez Palacio", "Uruapan", "Los Mochis", "Pachuca", "Tampico", "Tehuacán", "San Francisco Coacalco", "Nogales", "Oaxaca", "La Paz", "Campeche", "Monclova", "García", "Chilpancingo", "Puerto Vallarta", "Toluca", "Tapachula", "Buenavista", "Coatzacoalcos", "Ciudad Madero", "Cabo San Lucas", "Chicoloapan", "Ciudad del Carmen", "San Cristóbal de las Casas", "Poza Rica", "San Juan del Río", "San Luis Río Colorado", "Chalco", "Jiutepec", "Piedras Negras", "Guadalupe", "Chetumal", "Miramar", "Salamanca", "Ciudad Acuña", "Manzanillo", "San Pablo de las Salinas", "Cuautla", "Zamora", "Minatitlán", "Villa de Álvarez", "Colima"]
    elif category==2: # Fuits 
        WORD_LIST = ["Pomme","Apple","Apricots","Avocado","Banana","Blackberries","Blackcurrant","Blueberries","Breadfruit","Cantaloupe","Carambola","Cherimoya","Cherries","Clementine","Coconut Meat","Cranberries","Date Fruit","Durian","Elderberries","Feijoa","Figs","Gooseberries","Grapefruit","Grapes","Guava","Honeydew Melon","Jackfruit","Jujube Fruit","Kiwifruit","Kumquat","Lemon","lime","Longan","Loquat","Lychee","Mandarin","Mango","Mangosteen","Mulberries","Nectarine","Olives","Orange","Papaya","Passion Fruit","Peaches","Pear","Persimmon","Pitaya (Dragonfruit)","Pineapple","Pitanga","Plantain","Plums","Pomegranate","Prickly Pear","Prunes","Pummelo","Quince","Raspberries","Rhubarb","Rose-Apple","Sapodilla","Sapote","Soursop","Strawberries","Sugar-Apple","Tamarind","Tangerine","Watermelon"]
    elif category==3: # Colors        
        WORD_LIST = ["Absolute Zero","Acid green","Aero","Aero blue","African violet","Air superiority blue","Alabaster","Alice blue","Alloy orange","Almond","Amaranth","Amaranth pink","Amaranth purple","Amaranth red","Amazon","Amber","Amethyst","Android green","Antique brass","Antique bronze","Antique fuchsia","Antique ruby","Antique white","Apple green","Apricot","Aqua","Aquamarine","Arctic lime","Army green","Artichoke","Arylide yellow","Ash gray","Asparagus","Atomic tangerine","Auburn","Aureolin","Avocado","Azure","Baby blue","Baby pink","Baby powder","Baker-Miller pink","Banana Mania","Barbie Pink","Barn red","Battleship grey","Beau blue","Beaver","Beige","Bisque","Bistre","Bistre brown","Bitter lemon","Bitter lime","Bittersweet","Bittersweet shimmer","Black","Black bean","Black chocolate","Black coffee","Black coral","Black olive","Black Shadows","Blanched almond","Bleu de France","Blizzard blue","Blond","Blue","Blue bell","Blue-gray","Blue-green","Blue jeans","Blue sapphire","Blue-violet","Blue yonder","Bluetiful","Blush","Bole","Bone","Bottle green","Brandy","Brick red","Bright green","Bright lilac","Bright maroon","Bright navy blue","Brilliant rose","Brink pink","British racing green","Bronze","Brown","Brown sugar","Brunswick green","Bud green","Buff","Burgundy","Burlywood","Burnished brown","Burnt orange","Burnt sienna","Burnt umber","Byzantine","Byzantium","Cadet","Cadet blue","Cadet grey","Cadmium green","Cadmium orange","Cadmium red","Cadmium yellow","Café au lait","Café noir","Cambridge blue","Camel","Cameo pink","Canary","Canary yellow","Candy apple red","Candy pink","Capri","Caput mortuum","Cardinal","Caribbean green","Carmine","Carnation pink","Carnelian","Carolina blue","Carrot orange","Castleton green","Catawba","Cedar Chest","Celadon","Celadon blue","Celadon green","Celeste","Celtic blue","Cerise","Cerulean","Cerulean blue","Cerulean frost","CG blue","CG red","Champagne","Champagne pink","Charcoal","Charleston green","Charm pink","Chartreuse","Cherry blossom pink","Chestnut","Chili red","China pink","China rose","Chinese red","Chinese violet","Chinese yellow","Chocolate","Chocolate Cosmos","Chrome yellow","Cinereous","Cinnabar","Cinnamon Satin","Citrine","Citron","Claret","Cobalt blue","Cocoa brown","Coffee","Columbia Blue","Congo pink","Cool grey","Copper","Copper penny","Copper red","Copper rose","Coquelicot","Coral","Coral pink","Cordovan","Corn","Cornell red","Cornflower blue","Cornsilk","Cosmic cobalt","Cosmic latte","Coyote brown","Cotton candy","Cream","Crimson","Crystal","Cultured","Cyan","Cyber grape","Cyber yellow","Cyclamen","Dark blue-gray","Dark brown","Dark byzantium","Dark cornflower blue","Dark cyan","Dark electric blue","Dark goldenrod","Dark green","Dark jungle green","Dark khaki","Dark lava","Dark liver","Dark magenta","Dark moss green","Dark olive green","Dark orange","Dark orchid","Dark pastel green","Dark purple","Dark red","Dark salmon","Dark sea green","Dark sienna","Dark sky blue","Dark slate blue","Dark slate gray","Dark spring green","Dark turquoise","Dark violet","Dartmouth green","Deep cerise","Deep champagne","Deep chestnut","Deep jungle green","Deep pink","Deep saffron","Deep sky blue","Deep Space Sparkle","Deep taupe","Denim","Denim blue","Desert","Desert sand","Dim gray","Dodger blue","Dogwood rose","Drab","Duke blue","Dutch white","Earth yellow","Ebony","Ecru","Eerie black","Eggplant","Eggshell","Egyptian blue","Eigengrau","Electric blue","Electric green","Electric indigo","Electric lime","Electric purple","Electric violet","Emerald","Eminence","English green","English lavender","English red","English vermillion","English violet","Erin","Eton blue","Fallow","Falu red","Fandango","Fandango pink","Fashion fuchsia","Fawn","Feldgrau","Fern green","Field drab","Fiery rose","Firebrick","Fire engine red","Fire opal","Flame","Flax","Flirt","Floral white","Fluorescent blue","Forest green","French beige","French bistre","French blue","French fuchsia","French lilac","French lime","French mauve","French pink","French raspberry","French rose","French sky blue","French violet","Frostbite","Fuchsia","Fuchsia purple","Fuchsia rose","Fulvous","Fuzzy Wuzzy"]
    return random.choice(WORD_LIST)
    
def show_hangman(index):
    clearScreen()
    print(IMAGES[index])


def show_word(word, valid_letters):
    to_print = ""
    for x in word: 
        if x in valid_letters: 
            to_print = to_print + x + " "
        elif x == " ":
            to_print = to_print + "   "
        else: 
            to_print = to_print + "_ "
    print(to_print)
    if "_" in to_print:
        return True
    else: 
        return False


def add_points(word, valid_letters, completed, secounds, errors): 
    counter = 0 
    extra_points = 0 
    to_eval = ""
    # print("word:",word)
    # print("valid letters:",valid_letters)
    # print("completed:",completed)
    # print("secounds:",secounds)
    # print("errors:",errors)
    if completed: # Eval word
        to_eval = word
        extra_points += (len(word)//10)*10
        if (len(word)*2) > secounds: 
            extra_points += 5
    else: # Eval valid_letters
        to_eval = "".join(valid_letters)
    # print("to eval:",to_eval)
    vowels = ['a','e','i','o','u']
    for c in vowels: 
        if c in to_eval: 
            counter += 1 
    counter += (len(to_eval)-counter)*2
    counter += extra_points
    counter -= errors
    global score 
    score += counter 
    # print("extra points:",extra_points)
    # print("counter:",counter)
    # c = input("Only to wait...")


def eval_score():
    global score 
    # Abrir archivo 
    best_scores = []

    with open(FILENAME, "rb") as f:
        # Cargar lista
        best_scores = pickle.load(f)
    # Revisar si entra en los primeros 10 
    last_score = best_scores[-1]
    if last_score["Score"] < score: 
        name = input("Type your name:")
        score_item = { "Name": name, "Score": score }
        best_scores.append(score_item)
        best_scores = sorted(best_scores, key = lambda i: i["Score"], reverse=True)

    # Saving file 
    # create a binary pickle file 
    try: 
        f = open(FILENAME,"wb")
        if len(best_scores)>10:
            pickle.dump(best_scores[0:10],f)
        else: 
            pickle.dump(best_scores,f)
        print("File saved")
    except: 
        print("On exception...")
    finally:
        f.close()

    # Set score back to 0
    score = 0
    show_best_scores() 


def play_game(word): 
    valid_letters = []
    pending_letters = True
    errors = 0 
    game_start_time = datetime.now(tz=None)
    while (errors+1) < len(IMAGES) and pending_letters: 
        try: 
            show_hangman(errors)
            pending_letters = show_word(word, valid_letters)
            print("You have",(len(IMAGES)-(errors+1)),"options left.\n")
            # print("Search for ",word)
            # print("Game Started on",game_start_time)
            if pending_letters == False: 
                print("Excellent job, you find the word !!!")
                continue
            letter = input("Type a letter: ").lower()
            if letter in word: 
                valid_letters.append(letter)
            else: 
                errors += 1
        except: 
            pass
    else: 
        game_end_time = datetime.now(tz=None)
        # print("Game Ended on",game_end_time)
        time_difference = game_end_time - game_start_time
        # print("Time elapsed",time_difference)
        # print("Only secounds:",time_difference.total_seconds())
        add_points(word, valid_letters, not(pending_letters), int(time_difference.total_seconds()), errors) 

        if ((errors+1) < len(IMAGES)) == False: 
            print("Good luck for next time")
            eval_score()
        
        sleep(2)
        read_category()


def show_best_scores():
    best_scores = []
    place = 1 
    with open(FILENAME, "rb") as f:
        best_scores = pickle.load(f)
    print("This are the best scores...\n")
    print("Place | Score | Name ")
    
    for i in best_scores:
        print("{0:5d}".format(place),"|","{0:5d}".format(i["Score"]),"|",i["Name"])
        place += 1
    c = input("\nPress ENTER to continue...")
    read_category()


def read_category(): 
    try: 
        clearScreen()
        print(BANNER_HANGMAN)
        print(BANNER_WELCOME)
        show_categories()
        category = int(input("Select a category to play or quit (1-5): "))
        assert category > 0 and category < 6, "Invalid option"
        match category:
            case 5:
                print("Thank you for play!!! see you soon... ")
                if score > 0:
                    eval_score()
            case 4: 
                show_best_scores()
            case _:
                word = get_word(category).lower()
                play_game(word)


    except ValueError as ve: 
        print("Please type a valid option.")
        sleep(2)
        read_category()
    except AssertionError as ae:
        print(ae)
        sleep(2)
        read_category()


# De aqui se pueden obener los listados
# https://github.com/dariusk/corpora/tree/master/data/humans

# https://fruityvice.com/#3

# Buscar en google 
#     public api fruits names

# Elegir categoria
# Revisar si ya se descargo el catalogo
#     sino: descargar_catalogo
# Elegir palabra de catalogo 
# Iniciar juego 
#     Permitir 7 errores
# Al terminar
#     Hacer un ranking de los 10 mejores tiempos 
#         si entra en el ranking
#             pedir nombre 
#             guardar en orden 
#                 fecha y hora 
#                 nombre
#                 tiempo 
#                 errores 
#                 categoria / palabra 
#     Mostrar 
#         tiempo jugado 
#         cantidad de errores 
#     Preguntar si
#         volver a jugar
#         cambiar catalogo 
#         terminar 


def run():
    read_category()
    

if __name__ == "__main__":
    run()