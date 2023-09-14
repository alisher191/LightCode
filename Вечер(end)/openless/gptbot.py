import openai
import telebot


openai.api_key = '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'
bot = telebot.TeleBot('5721945909:AAFY-SECRiiBkl4KAfAazxiyz1DAJ5M9mTM')

@bot.message_handler(func=lambda _: True)
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