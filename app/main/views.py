from flask import render_template
from . import main
from ..request import get_sources,get_headlines,get_news_from_source,get_category_news
from datetime import datetime

@main.route('/')
def index():
  news_sources=get_sources()
  news_headlines=get_headlines()
  print(news_sources)
  time=datetime.now()
  date_today=time.strftime("%b %d, %Y %H:%M:%S")
  return render_template('index.html',news_sources=news_sources,news_headlines=news_headlines,date_today=date_today)


@main.route('/source/<string:source_id>')
def news_source(source_id):
  news_from_source=get_news_from_source(source_id)
  return render_template('news.html',news_from_source=news_from_source)

@main.route('/category/<string:category_name>')
def category(category_name):
  category_news=get_category_news(category_name)
  return render_template('index.html',news_headlines=category_news)