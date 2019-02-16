#file_to_links is left for editing & making it better. At this point it has no use
#Authentication problem still persists. But image loads & downloads successfully. Download count at unsplash is not going up this way.
#


from pyunsplash import PyUnsplash
from unsplash.api import Api
from unsplash.auth import Auth
import os
import requests
import csv


class UnsplashWallpaper(object):
    def __init__(self,api_key, client_id, client_secret, redirect_uri, code,query = None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.code = code
        self.query = query

    #authentication problem it's not working!!!!
    def authentication(self):
        auth = Auth( self.client_id, self.client_secret, self.redirect_uri, code = self.code)
        api = Api(auth)


    def client_id(self):
        return self.client_id
    def client_secret(self):
        return self.client_secret
    def redirect_uri(self):
        return self.redirect_uri
    def code(self):
        return self.code
    def api_key(self):
        return self.api_key

    def get_link(self):
        pu = PyUnsplash(api_key)
        photos = pu.photos(type_= 'random', order_by = 'latest', orientaion = 'landscape' ,count = 1)
        link = []
        for photo in photos.entries:
            photo.refresh()
            data = {'Photo Id':photo.id,'Url':photo.link_download}
            link.append(data)
            #print(data['Url'])
        self.download_links(Link = data)
        #self.file_of_links(link)

        #Still buggy need to use csv properly
    def file_of_links(self, link):
        with open('D:\\Links.csv','w') as csvFile:
            fields = ['Photo Id','Url']
            writer = csv.DictWriter(csvFile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(link)
        print('Completion')

    #to download the image to drive D:
    def download_links(self,Link):
        try:
            url = Link['Url']
            id = Link["Photo Id"]
            url = url.strip('https://')

            url = 'http://' + url + '?force=true'

            resp = requests.get(url)
            if resp.status_code == 200:
                with open('D:\\{}.jpeg'.format(id),'wb') as file:
                    file.write(resp.content)

        except Exception as e:
                print(str(e))
