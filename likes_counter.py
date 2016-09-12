import user_details
from tqdm import tqdm
from tabulate import tabulate


def show_table(friends):
    count=0
    friends_table=[]
    for friend_name in sorted(friends, key=friends.get, reverse=True):
        count+=1
   	friends_table.append([friend_name, friends[friend_name]])
   	if count == 5:
            break

    print tabulate(friends_table,headers=["Name","Likes"],tablefmt="fancy_grid")	
    



def main():
   friends={}
   myposts = user_details.get_user_posts() #get all posts on my wall
   print "%d posts found on your timeline!\n\nScanning posts\n\n"%(len(myposts))
   
   
   for post in tqdm(myposts):
      likes = user_details.get_post_likes(post)  #get likes details for each post
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
