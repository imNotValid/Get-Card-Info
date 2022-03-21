from requests import post
from re import findall, match
from json import dumps
from socket import gethostbyname, gethostname; IP = gethostbyname(gethostname()); print('YOUR SERVER IP: %s' % IP)
from flask import Flask, request, Response
from logging import getLogger, ERROR; getLogger('werkzeug').setLevel(ERROR)
r, g, y, w ='\033[1;31m', '\033[32;1m', '\033[1;33m', '\033[1;37m'
faList = [' ', 'ح' ,'چ' ,'ج' ,'ث' ,'ت' ,'پ' ,'ب' ,'ا' ,'ش' ,'س' ,'ژ' ,'ز' ,'ر' ,'ذ' ,'د' ,'خ' ,'ق' ,'ف' ,'غ' ,'ع' ,'ظ' ,'ط' ,'ض' ,'ص' ,'ی' ,'ه' ,'و' ,'ن' ,'م' ,'ل' ,'گ' ,'ک']
banks = {
    '627412': 'بانک اقتصاد نوین',
    '207177': 'بانک توسعه صادرات ایران',
    '627381': 'بانک انصار',
    '502229': 'بانک پاسارگاد',
    '505785': 'بانک ایران زمین',
    '622106': 'بانک پارسیان',
    '639194': 'بانک پارسیان',
    '639347': 'بانک پاسارگاد',
    '505801': 'موسسه اعتباری کوثر',
    '502908': 'بانک توسعه تعاون',
    '603799': 'بانک ملی ایران',
    '502938': 'بانک دی',
    '589463': 'بانک رفاه کارگران',
    '610433': 'بانک ملت',
    '621986': 'بانک سامان',
    '589210': 'بانک سپه',
    '639607': 'بانک سرمایه',
    '627353': 'بانک تجارت',
    '639346': 'بانک سینا',
    '502806': 'بانک شهر',
    '603769': 'بانک صادرات ایران',
    '627648': 'بانک توسعه صادرات ایران',
    '606373': 'بانک قرض الحسنه مهر ایران',
    '627884': 'بانک پارسیان',
    '627488': 'بانک کارآفرین',
    '627961': 'بانک صنعت و معدن',
    '502910': 'بانک کارآفرین',
    '603770': 'بانک کشاورزی',
    '628157': 'موسسه اعتباری توسعه',
    '636214': 'بانک تات',
    '505416': 'بانک گردشگری',
    '636795': 'بانک مرکزی',
    '636949': 'بانک حکمت ایرانیان',
    '628023': 'بانک مسکن',
    '639194': 'بانک پارسیان',
    '639217': 'بانک کشاورزی',
    '639370': 'بانک مهر اقتصاد',
    '627760': 'پست بانک ایران',
    '639599': 'بانک قوامین',
    '991975': 'بانک ملت'
}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.42',}
url = 'https://estelam.net/checkSheba'
def isCard(card): return True if match(r"\d{16}", card) else False
def getCard(card):
    if isCard(card):
        startCard = card[0:6]
        res = post(url, {'card': card}, headers=headers).text
        return {'status': True, 'card': card, 'holder': "".join(x for x in list(filter(lambda x: x in faList, res.split('|')[-1]))), 'bankName': banks[startCard] if startCard in banks else None, 'coder': '@imNotValid'} if findall(r"[\d\w]{24}", res) else {'status': False, 'card': card}
    else: return {'status': False}
app = Flask(__name__)
@app.route('/checkCard', methods=['GET', 'POST'])
def reCard():
    checked = getCard(request.args.get('card'))
    return Response(dumps(checked, indent=4, ensure_ascii=False), status=200 if checked['status'] else 400)
app.run(IP, 80, debug=False)