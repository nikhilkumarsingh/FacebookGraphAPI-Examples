import requests
import facebook


#authentication
access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
graph = facebook.GraphAPI(access_token=access_token, version='2.5')



def get_user_posts():
   myposts=[]

   #get my posts on page 1
   posts = graph.get_connections('me',connection_name='posts')
   myposts = posts['data']

   while(1):
      try:
         next_page_url=posts['paging']['next']  #get url for next page
      except KeyError:
         break
      posts = requests.get(next_page_url).json()
      myposts += posts['data']

   return myposts





   



