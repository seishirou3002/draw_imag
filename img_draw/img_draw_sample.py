#画像に文字を埋め込み出力するプログラム
from PIL import Image,ImageDraw,ImageFont
import pandas as pd

#画像のパスと画像に埋め込む文字を指定して画像に書き込む関数
def drawImage(imgPath,text):
	img = Image.open(imgPath)	#画像のパスを指定
	draw = ImageDraw.Draw(img)	#画像を読みこむ
	font = ImageFont.truetype("C:\Windows\Fonts\meiryob.ttc", 27) #フォントを設定(こちらを要望で変更)
	draw.text((100,96),text,fill=(255,0,0),font=font) #画像の大きさが全て同じなら変更は(100,96)とfill=(255,0,0)のみ
	img.save("sample.jpg")	#要望でファイル名を変更します

#excelから画像に埋め込む文字を取得する(excelフォーマットによっては修正)
def get_excel_text(path):
	df = pd.read_excel(path)
	textList = df
	return textList

#今回の要望に沿ったプログラムに修正する場合
#-----------ここから処理が始まります

#最初にexcelから画像に埋め込む文字を取得
#text = get_excel_text(path)

#10枚分の画像に書き込む処理を記載

drawImage("shutterstock_395310790-300x192.jpg","はじめまして")