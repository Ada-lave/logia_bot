from vkbottle import Bot
from config import api, state_dispenser, labeler
from routes import labelers
from vkbottle.bot import BotLabeler, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text,BaseStateGroup, PhotoMessageUploader, OpenLink
from services.ai_service import save_image
from states.menu_state import MenuState



bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser
)

photo_upld = PhotoMessageUploader(bot.api)


@bot.on.message(text="Начать")
async def menu(message: Message):
    KEYBOARD = (
        Keyboard(one_time=True,inline=False)
        .add(Text("Аниме", {"cmd":'anime'}), color=KeyboardButtonColor.POSITIVE)
    )
    await message.answer("Выберите режим из доступных:", keyboard=KEYBOARD)
    await bot.state_dispenser.set(message.peer_id, MenuState.START)
    

@bot.on.message(state=MenuState.START, payload={"cmd": "anime"})
async def get_promt_desc(message: Message):
    await message.answer("Введи описание того что должно быть и(или) должно происходить на картинке")
    await bot.state_dispenser.set(message.peer_id, MenuState.ANIME)

@bot.on.message(state=MenuState.ANIME)
async def generate_image(message: Message):
    await message.answer("Генерация картинки 🔄")
    
    path = f"imgs/{message.from_id}.png"
    await bot.state_dispenser.set(message.peer_id, MenuState.GENERATE)
    await save_image(promt=message.text,path=path)
    
    photo = await photo_upld.upload(file_source=path, peer_id=message.peer_id)
    
    await message.answer(attachment=photo)
    await menu(message)

for label in labelers:
    bot.labeler.load(label)

@bot.on.message(text=["Помощь","помощь","помощ","помошь","помош","помошщ","помошц","помошш","помошщь","помошшь","Помошь",'Help','help'])
async def help(message: Message):
        help_text = "1. Что бы вновь начать диалог с ботом необходимо заново Прописать команду Начать.\n\n2. Если у вас возникли какие либо предложения по улучшению или идеи пишите в лс администратору.\n\n3. Незабывайте соблюдать соглашение об использовании бота."
        KEYBOARD = (
            Keyboard(one_time=True)
            .add(OpenLink("https://vk.com/topic-188992540_50173854", "Соглашение"))
            .row()
            .add(Text("Начать"), color=KeyboardButtonColor.POSITIVE)
        )
        
        await message.answer(help_text, keyboard=KEYBOARD)

bot.run_forever()
