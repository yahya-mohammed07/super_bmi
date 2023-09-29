from constants import TOKEN, BOT_USR
import telebot

bot = telebot.TeleBot(token=TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def start(message):
  bot.reply_to(message, "Welcome to BMI calculator BOT!, send your height and weight like this ex: 170 60 in kg")

# helper function to get bmi
def cal_bmi(height, weight) -> float:
  return (weight / (height/100) ** 2)

#get bmi category
def bmi_category(bmi: float) -> str:
  if bmi < 18.5: return "Underweight"
  elif bmi >= 18.5 and bmi < 25: return "Normal"
  elif bmi >= 25 and bmi < 30: return "Overweight"
  else: return "Obese"

# TODO: add validation checks
#send result to user
@bot.message_handler(func= lambda message : True)
def calculate_bmi(message):
  height = float(message.text.split()[0])
  weight = float(message.text.split()[1])

  bmi = cal_bmi(weight=weight, height=height)
  category = bmi_category(bmi)
  bot.send_message(message.chat.id, f"Your BMI is {bmi:.2f} ({category}).")


print(f'bot started...')
bot.infinity_polling()
