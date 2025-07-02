import logging
from telegram.ext import *
from telegram import Update
import responses
API_KEY = "7720207067:AAGZDs5T_4ESxOndx_eo7tWTCBGajQZD-6I"

#configuracion del logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Iniciando el bot....')
#Se cambia el texto de Start para que presente opciones!!!
async def start_command(update:Update, context):
    await update.message.reply_text('Hola!!! como estas? Soy el bot miguel a tu servicio para darte asistencia en preguntas frecuentes \n Si no entiendes como insertar datos de alumnos, docentes, materias marca 01 \n Si no puedes encontrar la forma de generar listados con datos de alumnos, cursos, escuelas  oprime 02 \n Si necesitas comunicarte con un asistente oprime 03')
async def help_command(update:Update, context):
    await update.message.reply_text('Escribe tu problema y tratare de darle solucion') 
    
async def custom_command(update:Update, context):   
    await update.message.reply_text('Este es un comando con el que puedes escribir todo lo que desees ')  

async def handle_message(update:Update, context): 
    texto = str(update.message.text).lower()
    logging.info(f'User({update.message.chat.id}) escribe: {texto}') 
    response = responses.get_response(texto) 
    
    # Las respuestas del bot
    await update.message.reply_text(response)

async def error(update: Update, context):
    # Los errores que estan el log
    logging.error(f'Update {update} caused error {context.error}')
if __name__== '__main__':
    Application = Application.builder().token(API_KEY).build()    
    
    #comandos
    Application.add_handler(CommandHandler('start',start_command))
    Application.add_handler(CommandHandler('help',help_command))
    Application.add_handler(CommandHandler('custom',custom_command))
    
    # mensajes
    Application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #todos los errores en el log
    Application.add_error_handler(error)
    
    #Ejecucion del bot
    Application.run_polling(poll_interval=0.0)