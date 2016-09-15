import requests
import facebook


#authentication
access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
graph = facebook.GraphAPI(access_token=access_token, version='2.5')


def get_all_pages(posts):
   allposts=[]
   allposts = posts['data']
   while(1):
      try:
         next_page_url=posts['paging']['next']  #get url for next page
      except KeyError:
         break
      posts = requests.get(next_page_url).json()
      allposts += posts['data']
   return allposts
   


def get_post_likes(post):
   mylikes=[]
   try:
     likes=graph.get_connections(post['id'],"likes")
     mylikes = get_all_pages(likes)
   except:
     pass 
   return mylikes


def get_liked_pages():
   mypages=[]
   pages = graph.get_connections('me',connection_name='likes')
   mypages = get_all_pages(pages)
   return mypages


def get_user_posts():
   myposts=[]

   #get my posts on page 1
   posts = graph.get_connections('me',connection_name='posts')
   #visit all pages
   myposts = get_all_pages(posts)
   return myposts


def get_user_details():
   #graph api does not allow to access all fields at once...so you have to list the fields you require!
   user = graph.get_object('me',fields='name,id,email,education,friends,age_range,birthday')
   return user

   





