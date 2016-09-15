#  *FacebookGraphAPI-Examples*

# Examples this repository contains
- Python script to create a [likes-counter](https://github.com/nikhilkumarsingh/FacebookGraphAPI-Examples/blob/master/likes_counter.py) of your timeline posts.
- Python script to [share your post to multiple groups](https://github.com/nikhilkumarsingh/FacebookGraphAPI-Examples/tree/master/multiple_group_post_sharer) at once (with a pretty nice UI ;) )

# Requirements
- Python 2.X
- Python Facebook-SDK
    > pip install facebook-sdk
- Python requests module
  > pip install requests
- tqdm (for progress bar)
  > pip install tqdm
- tabulate (for fancy table)
  > pip install tabulate
- Facebook app user access token.(See the steps below to get a token)


# Getting a User Access Token

- Create a Facebook App which will be used to access Facebook's Graph API.

- Go to [Facebook Apps dashboard](https://developers.facebook.com/apps) -> Click *Add a New App* -> Choose platform WWW -> Choose a new name for your app -> Click *Create New Facebook App ID* -> Create a New App ID -> Choose Category -> Click *Create App ID* again.

- Go back to [Apps dashboard](https://developers.facebook.com/apps) -> Select the new app -> Settings -> Basic -> Enter Contact Email. This is required to take your app out of the sandbox.

- Go to *App Review* -> Do you want to make this app and all its live features available to the general public? -> Toggle the button to Yes -> *Make App Public?* -> Yes. This will enable others to see posts by your app in their timelines - otherwise, only you will see the wall posts by the app. 
Now,you should see a green dot next to app's name, and the text This app is public and available to all users.

- Make a note of the App ID and App Secret (Click *Show* next to it; you will be asked to re-enter your Facebook password).

- Now,go to [Graph API  Explorer](https://developers.facebook.com/tools/explorer) -> In the Application drop down -> Select the app created in Step 2 -> Click *Get Access Token* -> In Permissions popup go to Extended Permissions tab -> Select the permissions you want -> Click *Get Access Token* 

- Make a note of the short-lived token shown in Graph API Explorer.
   Facebook has deprecated offline access, the next best thing is long-lived token which expires in 60 days. We will convert the short-lived access token noted above to a long-lived token.

- For that, fill in the values in the URL below and open it in a browser:
    >https://graph.facebook.com/oauth/access_token?
    >client_id={APP_ID}&
    >client_secret={APP_SECRET}&
    >grant_type=fb_exchange_token&
    >fb_exchange_token={EXISTING_ACCESS_TOKEN}

- You should see access_token={...}&expires={...}. This new access_token is the long-lived token you can use in your Python script.
