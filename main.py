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

    #Ajout de l'heure en haut
    font = ImageFont.truetype('fonts/LTInternet-Regular.ttf', size = 30)
    image_editable.text(xy = (41,15), text = heure_actuelle, fill = (255, 255, 255), font=font, )#stroke_width= 0)

    #Ajout de l'heure d'arrivee
    font = ImageFont.truetype('fonts/font_heures_bold.otf', size = 27)
    image_editable.text(xy = (35,1360), text = heure_arrivee[0], fill = (0, 0, 0), font=font,)# stroke_width= 1)
    image_editable.text(xy = (48,1360), text = heure_arrivee[1], fill = (0, 0, 0), font=font,)# stroke_width= 1)
    image_editable.text(xy = (65,1360), text = heure_arrivee[2], fill = (0, 0, 0), font=font,)# stroke_width= 1)
    image_editable.text(xy = (80,1360), text = heure_arrivee[3], fill = (0, 0, 0), font=font,)# stroke_width= 1)
    image_editable.text(xy = (95,1360), text = heure_arrivee[4], fill = (0, 0, 0), font=font,)# stroke_width= 1)

    #Ajout de l'heure de depart
    font = ImageFont.truetype('fonts/font_heures_bold.otf', size = 27)
    image_editable.text(xy = (35,717), text = heure_depart[0], fill = (0, 0, 0), font=font,)# stroke_width= 1)
    image_editable.text(xy = (48,717), text = heure_depart[1], fill = (0, 0, 0), font=font,)# stroke_width= 1)
    image_editable.text(xy = (65,717), text = heure_depart[2], fill = (0, 0, 0), font=font,)# stroke_width= 1)
    image_editable.text(xy = (80,717), text = heure_depart[3], fill = (0, 0, 0), font=font,)# stroke_width= 1)
    image_editable.text(xy = (95,717), text = heure_depart[4], fill = (0, 0, 0), font=font,)# stroke_width= 1)

    #Ajout de la date de depart en haut

    font = ImageFont.truetype('fonts/font_heures_bold.otf', size = 27)
    image_editable.text(xy = (247,268), text = date, fill = (250, 250, 250), font=font,)# stroke_width= 1)
    image_editable.text(xy = (320,235), text = "ALLER", fill = (250, 250, 250), font=font,)# stroke_width= 1)

#   Sauvegarde
    image.save("fake_image.jpg")


if __name__ == "__main__":
    main()