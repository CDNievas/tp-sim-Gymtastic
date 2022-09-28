from PyInquirer import prompt

menuQuestions = [{
    "type":"input",
    "name":"CP",
    "message":"Cantidad de profesores: ",
    "filter": lambda val: int(val)
},{
    "type":"input",
    "name":"CAP",
    "message":"Cantidad alumnos por profesor: ",
    "filter": lambda val: int(val)
},{
    "type":"input",
    "name":"TF",
    "message":"Tiempo de ejecución en minutos: ",
    "filter": lambda val: int(val)
},{
    "type":"confirm",
    "name":"FIN_DE_SEMANA",
    "message":"Es fin de semana?",
    "default": False
}]

menuAgainQuestions = [{
    "type":"confirm",
    "name":"IS_AGAIN",
    "message":"Deseas correr otra simulación?",
    "default":True
}]


def printMenu():
    answers = prompt(menuQuestions)
    return answers.get("CP"), answers.get("CAP"), answers.get("FIN_DE_SEMANA"), answers.get("TF")

def printMenuAgain():
    answers = prompt(menuAgainQuestions)
    return answers.get("IS_AGAIN")