# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:12:49 2021

@author: sush1
"""
from ScrapperLayer.scrapperlayer import Scrapper

class BusinessLayer:
    
    def searchImageUrl(self,searchtext, n,header):
        scrapper = Scrapper()
        image_urls=scrapper.searchpage(searchtext,header)
        masterlistimage=scrapper.saveimages(image_urls, searchtext,n, header)
        return masterlistimage
        #scrapper.displayimage(masterlistimage)