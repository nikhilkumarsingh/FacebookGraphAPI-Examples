import sys
sys.path.insert(0,"...\\FacebookGraphAPI_Examples\\")     #fill ... with complete path to the parent directory
from api_utils import graph
from checkbox import CHECKBOX
import json
import FBgroups

'''
A collection is a list of groups.
We can post to a complete collection at one time.
'''

def update_group_info():
    all_groups = FBgroups.get_groups()
    with open('user_groups.txt','w') as f:
        f.write(json.dumps(all_groups))
    print "FB groups info updated."
    return
    


def add_groups(collection,collection_name):
    with open('user_groups.txt','r') as f:
        all_groups = json.load(f)

    all_groups = [group for group in all_groups if group not in collection]
    group_names = [group['name'] for group in all_groups]
    groups_selected = CHECKBOX(group_names).checked

    for x in range(len(all_groups)):
        if groups_selected[x]:
            collection.append(all_groups[x])

    with open(collection_name+".txt",'w') as myfile:
        myfile.write(json.dumps(collection))
    
    return


def create_collection():
    opt = raw_input("Update an existing collection?(y/n):")

    if opt == 'y':
        collection = open_collection()
    else:
        collection_name = raw_input("Choose a name for your new collection:")
        collection = []
        
    while(1):
        add_groups(collection,collection_name)
        opt = raw_input("Add more groups to this collection?(y/n):")
        if opt == 'n':
            break
        
    print "Done"
    return
    

def open_collection():
    collection_name = raw_input("Enter collection name:")

    try:
        with open(collection_name+".txt",'r') as myfile:
            collection = json.load(myfile)
    except IOError:
         print "No such collection found."
         return
            
    return collection


def show_collection():
    collection = open_collection()

    if collection == None:
        return
    
    print "Collection contains following groups:"    
    for group in collection:
        print group['name'].encode("utf8")

    return    

    
def share_post():
    collection = open_collection()
    link = raw_input("Enter the link of the post you want to share:")
    message = raw_input("Enter the message for shared post:")
    for group in collection:
        try:
            graph.put_object(parent_object = group['id'], connection_name = 'feed', message=message, link=link)
            print "Post successfully shared with %s"%(group['name'].encode('utf8'))
        except:
            print "Post can't be shared with %s"%(group['name'].encode('utf8'))
            pass
    return    





def main():
    print "Use following commands:\n1. 'create' to create or update a collection.\n2. 'show' to see groups in a collection.\n3. 'share' to share a post to any collection.\n4. 'update' to update the FB groups info. \n5. 'exit' to exit the program.\n\nP.S: A collection is a list of groups."

    while(1):
        opt = raw_input('\n>>>')
        if opt == 'create':
            create_collection()
        elif opt == 'show':
            show_collection()
        elif opt == 'share':
            share_post()
        elif opt == 'update':
            update_group_info()
        elif opt == 'exit':
            break
        else:
            print "Unknown command."
    
    return



if __name__=="__main__":
    main()

