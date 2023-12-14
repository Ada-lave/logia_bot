from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler
import os 
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
vk_api_key = os.getenv("VK_KEY")
fb_key = os.getenv("FB_KEY")
fb_secret = os.getenv("FB_SECRET")

api = API(vk_api_key)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()