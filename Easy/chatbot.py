# -*- coding: UTF8 -*-
import requests
import datetime
import random

greetings=['hola','Hola','hey','Hey','Hello','hello','hi','Hi','hai','Hai']
random_greeting = random.choice(greetings)
question = ['How are you?','how are you?','How are you doing?','how are you doing?']
ques = ['What can you do?']


class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '621401613:AAEHojlz1VVFWPDxEKI5R7ovgqGhgg-NX1A' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name



def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"
                if first_chat_text in greetings:
                    magnito_bot.send_message(first_chat_id,random_greeting+" "+ first_chat_name)
                    new_offset = first_update_id + 1
                elif first_chat_text in question:
                    magnito_bot.send_message(first_chat_id,'Yeah I am doing great !! ')
                    new_offset = first_update_id + 1
                elif first_chat_text in ques:
                    magnito_bot.send_message(first_chat_id,'I can crack a joke ,I can tell your name,I can tell me name,I can tell name of few great movies,I can tell few good books ')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Tell me a Joke':
                    magnito_bot.send_message(first_chat_id,'Once there were three turtles. One day they decided to go on a picnic. When they got there, they realized they had forgotten the soda. The youngest turtle said he would go home and get it if they would not eat the sandwiches until he got back. A week went by, then a month, finally a year, when the two turtles said,"oh, come on, let us eat the sandwiches." Suddenly the little turtle popped up from behind a rock and said, "If you do, I will not go!" ')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'What is my name?':
                    magnito_bot.send_message(first_chat_id,'Your name is '+" "+first_chat_name)
                    new_offset = first_update_id + 1
                elif first_chat_text == 'What is your name?':
                    magnito_bot.send_message(first_chat_id,'My name is SWORD')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Tell me few good movies':
                    magnito_bot.send_message(first_chat_id,'The Godfather,The Shawshank Redemption,Pulp Fiction,Star wars,Dark Knight are few of the very good movies')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Tell me few good books':
                    magnito_bot.send_message(first_chat_id,'White Tiger,The Great Indian Novel ,Train to Pakistan,Palace of Illusions,The Guide,The God of Small Things are few best books of Indian Authors')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Bye':
                    magnito_bot.send_message(first_chat_id,'Bye!! It was fun interacting with you')
                    new_offset = first_update_id + 1
                
							
				

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
							exit()
