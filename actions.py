import random
from scraper import Item
import re


def get_response(message: str) -> str:
    p_message = message.lower()[1:]

    if p_message.startswith('info'):
        print("1")
        id = re.findall(r'\d+', p_message)[0]
        #TODO Make it so that multiple IDs will be used and multiple info will be returned
        print(id)
        return str(getItemInformation(id))

    if p_message == 'roll':
        return "nice"

    if p_message == 'boll':
        return '`This is a help message that you can modify.`'

    return 'I didn\'t understand what you wrote. Try typing "!help".'

def getItemInformation(itemID):
    item = Item(itemID)
    return item.getItemName(), item.getMarketPrice()
