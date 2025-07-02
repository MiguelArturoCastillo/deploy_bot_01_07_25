import re

def process_message(message, response_array, response):
    # Dividir el mensaje y la puntuacion dentro del array
    list_message =re.findall(r"[\w']+|[.,¡¿!?;]",message.lower())
    
    #Puntua el conjunto de palabras en el mensaje
    score = 0 
    for word in list_message:
        if word in response_array:
            score = score + 1
            
    #Retorna las respuestas y el score de la respuesta
    print(score, response) #Esto essolamente para debbuging
    return [score,response]
    
def get_response(message):
    #agrega tu respuesta personalizada, ¡SE agraga algunas respuestas para adaptarla al sitio web del instituto! 
    response_list =[
        process_message(message,['hola','hey','buenas','holis'],'Hola! ¿Como estas?, coloca /start para iniciar la conversacion.'),
        process_message(message, ['bye', 'chau','adios','hasta', 'luego'],'Chau, que la pases bien!'),
        process_message(message,['como','cómo','estas','vos'],'yo estoy muy bien, muchas gracias!'),
        process_message(message,['01'],'Bien, bien debes visitar nuestro sitio web en soportes'), 
        process_message(message,['Si','no','No','si'],'Bien, En este caso se contatactaran con tigo.'),       
        process_message(message,['01','02', '03', '04','05','06','07'],'Bien, en breve te contactaremos para informarte, gracias.'),
        process_message(message,['me','puedes', 'ayudar', 'help'],'Si, para recibir ayuda oprime 04?')
        
        #Si quieres, puedes agregar mas respuestas    
    ]
    
    # Revisa todas las respuestas score y retorna la mejor conexion posible
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])
    
    #Obtener el mayor valor posible para la mejor respuesta y almacenarlo dentro de una variable
    winning_response =max(response_scores)    
    matching_response =response_list[response_scores.index(winning_response)]
    
    #retorna el matching response al usuario
    if winning_response == 0:
        bot_response ='Yo no logro entender lo que escribiste'
    else:
        bot_response = matching_response[1]
    
    print('la respuesta del Bot:', bot_response)
    return bot_response          