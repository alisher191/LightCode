import openai
import telebot


openai.api_key = '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'
bot = telebot.TeleBot('5995067479:AAEQc4hjltvXtXOv5Y-Y-8gIclknCme6tf0')

@bot.message_handler(func=lambda _:True)
def handle_message(message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.5,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


bot.polling()
