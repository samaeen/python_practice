import pytube
import urllib.request
import urllib.parse

#a=urllib.request.urlopen('https://www.youtube.com/get_video_info?video_id=ZyTO4SwhSeE&index=3&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF')
#parsed=urllib.parse_qs(a.read())
#print(a.read())

realUrl='https://www.youtube.com/watch?v=ZyTO4SwhSeE&index=3&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF'
urlforParsing=realUrl.replace('watch?v','get_video_info?video_id')

print(urlforParsing)