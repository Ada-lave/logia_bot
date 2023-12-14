from vkbottle.bot import BotLabeler, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text,BaseStateGroup



bl = BotLabeler()


bl.message(text="Помощь")
async def help(message: Message):
        help_text = "1. Что бы вновь начать диалог с ботом необходимо заново Прописать команду Начать.\n\
                    2. Если у вас возникли какие либо предложения по улучшению или идеи пишите в лс администратору.\n\
                    3. Незабывайте соблюдать соглашение об использовании бота"
        
        await message.answer(help_text)
