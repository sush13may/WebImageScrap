# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from flask import Flask, render_template,jsonify, request
from flask_cors import CORS, cross_origin
from BusinessLayer.businesslayer import BusinessLayer
from ScrapperLayer.scrapperlayer import Scrapper

app = Flask(__name__)


@app.route('/')
@cross_origin()
def home():
    
    return render_template('home.html')


@app.route('/searchimage', methods=['GET','POST'])
@cross_origin()
def searchimage():
    print('IN searchimage')
    if request.method == 'POST':
        search_item = request.form['keyword']
        n_item= request.form['count']
        header = {
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
            }
        print(os.listdir())
        if 'static' in os.listdir():
            
            files = os.listdir('static')
            print(files)
            if len(files)> 0:
                remove_files()
        search_string= '+'.join(search_item.split())
        businesslayeritem = BusinessLayer()
        scrapperitem = Scrapper()
        list_image=businesslayeritem.searchImageUrl(search_string,n_item, header)
        
            
            
        return displayimages()
    
def displayimages():
    if 'static' in os.listdir():
            files = os.listdir('static')
            if len(files) > 0:
                print(files)
            else:
                files=[]
            return render_template('showimage.html', images=files)
    else:
        print('static folder does not exist')
        
def remove_files():
    print('in_remove')
    for item in os.listdir('static'):
        try:
            os.remove('static/'+item)
        except Exception as e:
            print(e)
        
if __name__=='__main__':
    
    app.run(host='127.0.0.1', port=8000, debug=True) #run on the localhost

    #app.run(debug=True)
    