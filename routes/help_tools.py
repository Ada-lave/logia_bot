from vkbottle.bot import BotLabeler, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text,BaseStateGroup, OpenLink


bl = BotLabeler()

@bl.message(text=['Сервисы'])
async def help_services_info(message: Message):
    KEYBORD = (
        Keyboard(one_time=True)
        .add(Text("Улучшениие качества картинки", payload={"text":"services"}))
    )
    
    await message.answer("Сервисы:",keyboard=KEYBORD)

@bl.message(text="Улучшениие качества картинки")
async def help_services_list(message: Message):
    KEYBOARD = (Keyboard(one_time=True)
                .add(OpenLink("https://waifu2x.udp.jp/index.ru.html",label="Waifu"))
                .add(OpenLink("https://upscales.ai/ru",label="Upscales")))
    
    await message.answer("Сервисы по улучшению качества", keyboard=KEYBOARD)