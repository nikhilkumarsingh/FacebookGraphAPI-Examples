import api_utils
from tqdm import tqdm           #for progress bar
from tabulate import tabulate   #for pretty table printing


def show_table(friends):
    count=0
    friends_table=[]
    
    for friend_name in sorted(friends, key=friends.get, reverse=True):       #get top 5 posts likers
        count+=1
   	friends_table.append([friend_name, friends[friend_name]])
   	if count == 5:
            break

    print tabulate(friends_table,headers=["Name","Likes"],tablefmt="fancy_grid")	
    return



def main():
   friends={}
   myposts = api_utils.get_user_posts() #get all posts on my wall
   print "%d posts found on your timeline!\n\nScanning posts\n\n"%(len(myposts))
   
   
   for post in tqdm(myposts):
      likes = api_utils.get_post_likes(post)      #get likes details for each post
      for like in likes:
         if like['name'] in friends.keys():
            friends[like['name']]+=1
         else:
            friends[like['name']] = 1

    
   print "\n\nHere are the people who have liked your posts max. no. of times:\n"
   show_table(friends)

   return


if __name__ == "__main__":
main()
