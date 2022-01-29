from flask import render_template
from . import main
from ..request import get_sources
from datetime import datetime

@main.route('/')
def index():
  news_sources=get_sources()
  print(news_sources)
  time=datetime.now()
  date_today=time.strftime("%b %d, %Y")
  return render_template('index.html',news_sources=news_sources,date_today=date_today)

