import logging
import colorama
import time
import os
from colorama import Fore
from colorama import Style
from aiogram import Bot, Dispatcher, executor, types

#=≠=≠=≠=≠=≠[TOKEN Y LLAMADO DEL BOT]
bot = Bot(token="5480356854:AAGdmsuPhqfP0ws21kNkeLqMUEGC4x7S0Ac", parse_mode=types.ParseMode.HTML)
iniciar = Dispatcher(bot)
#=≠=≠=≠[FIN TOKEN Y LLAMADO DEL BOT]

#=≠=≠=≠[NOMBRE DE USUARIO]
""" @Yaristelegram_bot """
#=≠=≠=≠[NOMBRE DE USUARIO]


#=≠=≠=≠=≠[COMANDOS]
#=≠=≠=≠=≠[INICIAR]
@iniciar.message_handler(commands=['start','iniciar'], commands_prefix='/')
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    info2 = await message.reply (f"""
 Hola @{message.from_user.username}!
""") 
    time.sleep(3)
    await info2.edit_text(f"""
<b>¿Que deseas hacer?</b>

Aqui puedes encontrar una lista de los comandos:

 /start /iniciar ------------Iniciar Bot      
 /help /ayuda ---------------Recibir ayuda               
 /update /context -----------Informacion del Bot   
 /cotizacion ----------------Hacer su cotizacion
       
""") 


#=≠=≠=≠=≠[CONTACTO]
@iniciar.message_handler(commands=['contacts','contacto'], commands_prefix='/')
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    await message.reply (f"""
 📞

 Gmail: yarisgomez255@gmail.com 
 Telefono: 3017877649
 Telegram: @Yaris0724
 Instagram: yarisn_24
""") 


#=≠=≠=≠=≠[INFORMACION]
@iniciar.message_handler(commands=['update','context'], commands_prefix='/')
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    info = await message.reply (f"""
    <b>El usuario @{message.from_user.username} ha solicitado informacion sobre el bot</b>
""")
    time.sleep(4)
    await info.edit_text(f"""
Este Bot fue creado por <b>Yaris Gomez</b> de <b>ADSO-1</b>
La funcion es hacer cotizaciones, de una cocina 

Para hacer su cotizacion tiene los siguientes comandos:

   /cotizacion /calcular /calculate
""") 
     
    
#=≠=≠=≠=≠[AYUDA]
@iniciar.message_handler(commands=['help','ayuda'], commands_prefix='/')
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    await message.reply (f"""
Aqui puede encontar todos los comandos con una pequeña descripcion

Iniciar el Bot 
 /start /iniciar 
     
-----------------------------------------

Recibir ayuda
 /help /ayuda   
-----------------------------------------

Informacion del Bot 
/update /context 
-----------------------------------------

Hacer su cotizacion
/cotizacion /calcular /calculate

 .....................................................
 Si desea recibir una ayuda un poco más personalizada, tiene algun problema o inquietud, puede contactarme con el siguiente comando /contacts /conatcto
""")
    

#=≠=≠=≠=≠[ERROR]
@iniciar.message_handler(commands=['start','iniciar','help','ayuda','update','context','calcular','calculate'], commands_prefix='')
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    await message.reply (f"""
 ERROR: Ingrese un comando valido, debe usar al inicio (/)
""") 


#=≠=≠=≠=≠[COTIZACION]
@iniciar.message_handler(commands=['cotizacion','calcular','calculate'], commands_prefix='/')
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    info3 = await message.reply (f"""
 <b>Calcula y personaliza</b>
Para hacer su cotizacion: 

•	https://keobra.com/calcula

"""
)


os.system("cls || clear")
# MAIN ##########################################
colorama.init()

print(Fore.GREEN+"""  
 __  __     ______     ______     __     ______        ______     ______     ______  
/\ \_\ \   /\  __ \   /\  == \   /\ \   /\  ___\      /\  == \   /\  __ \   /\__  _\ 
\ \____ \  \ \  __ \  \ \  __<   \ \ \  \ \___  \     \ \  __<   \ \ \/\ \  \/_/\ \/ 
 \/\_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\     \ \_____\  \ \_____\    \ \_\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/      \/_____/   \/_____/     \/_/ 
                                                                    C O D E : YARIS
"""+ Style.RESET_ALL)
print("""
[ Creador : YARIS - ADSO-1 ]
[ Program : PROYECTO BOT]
""")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
      executor.start_polling(iniciar, skip_updates=True)
