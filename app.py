from flask import Flask,render_template,url_for,request
from bs4 import BeautifulSoup
import requests 

app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
   url="https://fashionunited.in/news/fashion"
   req=requests.get(url)
   soup= BeautifulSoup(req.content,"html.parser")
   outerdata=soup.find_all("h2",class_="MuiTypography-root MuiTypography-h5 css-12a7eiy MuiTypography-colorTextPrimary",limit=6)
   finalnews=""
   for data in outerdata:
       news=data.text
       finalnews +="\u2022"+news+"\n"      
       #print("\u2022"+data.text)
   return render_template("index.html",News=finalnews)     


