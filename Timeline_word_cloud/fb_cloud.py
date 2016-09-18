import sys
sys.path.insert(0,"C:\\Users\\vivek\\Desktop\\nikhil_work\\fb_messenger\\FacebookGraphAPI_Examples\\")
from api_utils import graph,get_all_pages
import WC



def main(): 
   myposts = graph.get_connections("me",connection_name="feed")     #get first page
   all_posts = get_all_pages(myposts)                               #get all posts on my wall

   print "%d posts found on your timeline!\nNow creating word cloud...\n"%(len(all_posts))

   all_text = ' '.join(post['message'] for post in all_posts[:60] if 'message' in post)  #create single string for all posts text
   
   WC.wcloud(all_text)
   return


if __name__ == "__main__":
    main()
