from flask import Blueprint, render_template, request
from flask_login import login_required,current_user
from flask.helpers import flash
import pickle
import pandas as pd
views=Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    f=pd.read_csv('./website/tracks.csv')
    return render_template("home.html",user=current_user,name=f['name'],artist=f['artist'],link=f['links.1'])
@views.route('/Recommendation')
@login_required
def recommendation():
    f=open('./website/recommendation.txt','rb+')
    recommended=pickle.load(f)
    user=pd.read_csv('./website/cleaned_user_data.csv')

    return render_template("Recommendation.html",user=current_user,recommended=recommended,name=user['name'],artist=user['artist'],link=user['link'])


