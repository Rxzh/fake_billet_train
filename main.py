from whaaaaat import prompt, print_json, Separator
from PIL import Image, ImageFont, ImageDraw 


def set_heure_depart(heure_arrivee):
    """
    Retourne l'heure d'arrivee moins 1h56, durée typique d'un trajet Paris-Lyon
    """
    total_minutes = ((60 * int(heure_arrivee[:2]) + int(heure_arrivee[3:])) - 116 )
    heure = str(total_minutes//60)
    minutes = str(total_minutes%60)
    heure = (len(heure)==1)*'0' + heure
    minutes = (len(minutes)==1)*'0' + minutes
    
    return heure + 'h' + minutes


questions = [
    {
        "type": "list",
        "name": "jour",
        "message": "Choisis une date",
        "choices": [
            "Lundi",
            "Mardi",
            "Mercredi",
            "Jeudi",
            "Vendredi",
            "Samedi",
            "Dimanche"

        ],
    },
    {
        "type": "list",
        "name": "num",
        "message": "Choisis une date",
        "choices": [(i < 10)*'0'+str(i) for i in range(1,32)],

    },
        {
        "type": "list",
        "name": "mois",
        "message": "Choisis une date",
        "choices": ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"],

    },
]


def main():
    image = Image.open('train.jpg')
    heure_actuelle = "08:18"

    image_editable = ImageDraw.Draw(image)
    answers = prompt(questions)

    heure_arrivee = input('Heure d\'arrivée à gare de Lyon (ex "19h35") : ')
    heure_depart = set_heure_depart(heure_arrivee)

    jour = answers['jour']
    n_jour = answers['num']
    mois = answers['mois']

    date = jour[:3]+'. ' + n_jour +' '+ mois[:3]+'. ' + heure_depart


    font1 = ImageFont.truetype('fonts/LTInternet-Regular.ttf', size = 30)
    font2 = ImageFont.truetype('fonts/font_heures_bold.otf', size = 27)

    #Ajout de l'heure en haut
    
    image_editable.text(xy = (41,15), text = heure_actuelle, fill = (255, 255, 255), font=font1)

    #Ajout de l'heure d'arrivee
    
    L_x = [35,48,65,80,95]
    for x in L_x:
        image_editable.text(xy = (x,1360), text = heure_arrivee[L_x.index(x)], fill = (0, 0, 0), font=font2) #Ajout de l'heure d'arrivee
        image_editable.text(xy = (x,717), text = heure_depart[L_x.index(x)], fill = (0, 0, 0), font=font2) #Ajout de l'heure de depart 

    #Ajout de la date de depart en haut

    image_editable.text(xy = (247,268), text = date, fill = (250, 250, 250), font=font2)
    image_editable.text(xy = (320,235), text = "ALLER", fill = (250, 250, 250), font=font2)

    #Ajout de la date de depart en haut


    image_editable.text(xy = (247,268), text = date, fill = (250, 250, 250), font=font2)
    image_editable.text(xy = (320,235), text = "ALLER", fill = (250, 250, 250), font=font2)

#   Sauvegarde
    image.save("fake_image.jpg")


if __name__ == "__main__":
    main()