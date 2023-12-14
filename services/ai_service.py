import aiohttp
import requests
import json
import base64
import time
from PIL import Image
from io import BytesIO
import asyncio
from config import fb_key, fb_secret


url = "https://api-key.fusionbrain.ai/"
AUTH_HEADERS = {
            "X-Key": f"Key {fb_key}",
            "X-Secret": f"Secret {fb_secret}",
        }

    
class AI:
    
    def __init__(self) -> None:
        self.url = url
        self.AUTH_HEADERS = AUTH_HEADERS
    
    async def get_model(self):
        async with aiohttp.ClientSession() as session: 
            async with session.get(self.url + "key/api/v1/models", headers=self.AUTH_HEADERS) as response:
                data =  await response.json()
            return data[0]['id']
    
    async def generate(self, promt, model, images=1, width=1024, heigth=1024):
        params = {
            "type": "GENERATE",
            
            "numImages": images,
            "width": width,
            "height": heigth,
            "style":"ANIME",
            "censored": True,
            "generateParams": {
                "query": promt
            }
        }
        
        data = aiohttp.FormData()
        
        data.add_field("model_id",
                       value=str(model),
                        )
        
        data.add_field('params',
                       value=json.dumps(params),
                       content_type="application/json"
                       )
        
        
        
        
        
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url + "key/api/v1/text2image/run", headers=self.AUTH_HEADERS, data=data) as response:
                data = await response.json()
            return data['uuid']
        
    async def check_generation(self, request_id, attempts=10, delay=5):
        while attempts > 0:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + "key/api/v1/text2image/status/" + request_id, headers=self.AUTH_HEADERS) as response:
                    data = await response.json()
                    print(data['status'])
            
            if data['status'] == "DONE":
                return data["images"]
            attempts -= 1
            time.sleep(delay)



async def save_image(path, promt):
    ai = AI()
    model_id = await ai.get_model()
    resp_id = await ai.generate(promt, model_id)
    img_byte = await ai.check_generation(resp_id)
    img_byte = base64.b64decode(img_byte[0])
    img = Image.open(BytesIO(img_byte))
    img.save(path)
    




