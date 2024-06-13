import jsonpath
import requests
import telebot
from PIL import Image
from bs4 import BeautifulSoup

API_KEY = str("TOKEN")
bot = telebot.TeleBot(API_KEY)

# --------------------------------
# Pixiv Ranking Func
def get_prank(rmode, index):
  pixiv_rank_url = 'https://www.pixiv.net/ranking.php'
  pixiv_ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
  pixiv_args = {
      'content': 'illust'
  }
  args = pixiv_args.copy()
  if rmode == 0:
    args['mode'] = 'daily'
  elif rmode == 1:
    args['mode'] = 'weekly'
  elif rmode == 2:
    args['mode'] = 'monthly'
  pixiv_request = requests.get(pixiv_rank_url, params=args, headers=pixiv_ua)
  pixiv_content = pixiv_request.text
  pixiv_soup = BeautifulSoup(pixiv_content, 'html.parser')
  all_res = pixiv_soup.find_all('div', class_="ranking-image-item")
  img_url = all_res[index - 1].find('img')['data-src']
  img_url_i = img_url.find('/img-master/img/') + len('/img-master/img/')
  img_url_j = img_url.find('_master')
  url = "https://i.pixiv.re/img-original/img/" + img_url[img_url_i:img_url_j] + ".jpg"
  print(url)
  return url

# --------------------------------
# Pixiv Ranking Part
@bot.message_handler(commands=['day'])
def p_day(message):
  if message.text[:4] == "/day":
    url = ""
    chat_id = message.chat.id
    if len(message.text) == 4:
      url = get_prank(0, 1)
      req_get = requests.get(url, stream=True)
      if req_get.status_code == 200:
        photo = Image.open(req_get.raw)
        bot.send_photo(chat_id, photo)
      else:
        bot.reply_to(message, "無法返回圖片內容(404)")
    else:
      if message.text[:5] == "/day ":
        str_index = message.text[5:]
        if str_index.isnumeric():
          get_index = int(str_index)
          if get_index >= 1 and get_index <= 50:
            url = get_prank(0, get_index)
            req_get = requests.get(url, stream=True)
            if req_get.status_code == 200:
              photo = Image.open(req_get.raw)
              bot.send_photo(chat_id, photo)
            else:
              bot.reply_to(message, "無法返回圖片內容(404)")
          else:
            bot.reply_to(message, "排名仅限前50")
        else:
          bot.reply_to(message, "請輸入正確的排名")
      else:
        bot.reply_to(message, "輸入格式有誤")
  else:
    bot.reply_to(message, "輸入格式有誤")

@bot.message_handler(commands=['week'])
def p_week(message):
  if message.text[:5] == "/week":
    url = ""
    chat_id = message.chat.id
    if len(message.text) == 5:
      url = get_prank(1, 1)
      req_get = requests.get(url, stream=True)
      if req_get.status_code == 200:
        photo = Image.open(req_get.raw)
        bot.send_photo(chat_id, photo)
      else:
        bot.reply_to(message, "無法返回圖片內容(404)")
    else:
      if message.text[:6] == "/week ":
        str_index = message.text[6:]
        if str_index.isnumeric():
          get_index = int(str_index)
          if get_index >= 1 and get_index <= 50:
            url = get_prank(1, get_index)
            if url == "0":
              bot.reply_to(message, "請檢驗請求內容是否正確")
            else:
              req_get = requests.get(url, stream=True)
              if req_get.status_code == 200:
                photo = Image.open(req_get.raw)
                bot.send_photo(chat_id, photo)
              else:
                bot.reply_to(message, "無法返回圖片內容(404)")
          else:
            bot.reply_to(message, "排名仅限前50")
        else:
          bot.reply_to(message, "請輸入正確的排名")
      else:
        bot.reply_to(message, "輸入格式有誤")
  else:
    bot.reply_to(message, "輸入格式有誤")

@bot.message_handler(commands=['month'])
def p_month(message):
  if message.text[:6] == "/month":
    url = ""
    chat_id = message.chat.id
    if len(message.text) == 6:
      url = get_prank(2, 1)
      req_get = requests.get(url, stream=True)
      if req_get.status_code == 200:
        photo = Image.open(req_get.raw)
        bot.send_photo(chat_id, photo)
      else:
        bot.reply_to(message, "無法返回圖片內容(404)")
    else:
      if message.text[:7] == "/month ":
        str_index = message.text[7:]
        if str_index.isnumeric():
          get_index = int(str_index)
          if get_index >= 1 and get_index <= 50:
            url = get_prank(2, get_index)
            if url == "0":
              bot.reply_to(message, "請檢驗請求內容是否正確")
            else:
              req_get = requests.get(url, stream=True)
              if req_get.status_code == 200:
                photo = Image.open(req_get.raw)
                bot.send_photo(chat_id, photo)
              else:
                bot.reply_to(message, "無法返回圖片內容(404)")
          else:
            bot.reply_to(message, "排名仅限前50")
        else:
          bot.reply_to(message, "請輸入正確的排名")
      else:
        bot.reply_to(message, "輸入格式有誤")
  else:
    bot.reply_to(message, "輸入格式有誤")
