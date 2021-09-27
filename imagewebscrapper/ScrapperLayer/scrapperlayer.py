# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:14:32 2021

@author: sush1
"""
import requests
import sys
import json
import urllib.request
import urllib.error
import urllib.parse
from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
import os

class Scrapper:
    
    def searchpage(self,text, header):
        url = "https://www.google.co.in/search?q=" + text + "&source=lnms&tbm=isch"
        
        
        request= urllib.request.Request(url, headers=header)
        
    
        response = urllib.request.urlopen(request)
        
        responsedata = response.read()
        
        soup = BeautifulSoup(responsedata, 'html.parser') #get the page
       
        imagelist=[]
        for a in soup.find_all('img', {'class':"rg_i Q4LuWd"}):
            try:
                link=a['data-src']
                imagelist.append(link)
            except Exception as e:
                print(e)
            
        
        print(f'There are total of {len(imagelist)} images')
                
        
        return imagelist
            
        
        
        
    def saveimages(self, image_url, seachtxt,n, header):
        counter = 1
        i=0
        #to display the images , store them in a list and return for the next function
        masterlistimage=[]
        if 'static' in os.listdir():
            print('Dierctory exists')
        else:
            os.makedirs('static')
        
        for image in image_url:
            if i < int(n):
                
                imagepath = urllib.request.Request(image, headers=header)
                try:
                    urllib.request.urlretrieve(image,"./static/"+seachtxt+str(counter)+".jpg")
                    counter = counter +1
                    i = i+1
                except Exception as e:
                    print("something Wrong")
                    counter = counter +1
                responseimage = urllib.request.urlopen(imagepath)
                rawimage = responseimage.read()
            
                #masterlistimage.append(rawimage)
            else:
                break
        #return masterlistimage
    
    
   