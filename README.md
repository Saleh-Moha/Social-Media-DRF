DRF APP using technologies like : 
- djoser
- rest framework
- django filters
- docker
- sqllite3 => (you can use any database)
  

*Users App:

        --models:
            -> custom user model which allow user to signup & login
            -> user profile model that creates an account after regiteration
            -> follow model that allow users to follow eachothers and see the followings and followers
            -> follow request model that send a notification for user who is private that somone follows thier account 
    
    
    --urls:
        -> using one endpoint:
            - /user-profile/{pk} => to get the data of the user
            - /user-profile-info/{pk} => to get the signup data of the user
            - /folloe/{pk} => to follow account
            - /follow-requests => to get all the requests if your account is private
            - /follow-requests/{pk} => to handle each request 
            - /followers => to get followers
            - /followings => to get following 
        ____________________________________________

*Authentication:
___________________

    --Using Djoser To Signup Or Signin User Using The Custom User Serializer.
        -> endpoints:
            - /auth/users/ => to signup
            - /auth/token/login/ => to signin and generate token

    -- Using DRF => authtoken To Generate Tokens.
        ________________________________________________

* Post App:
___________________
    
    --models:
        -> Written Posts Model => allow user to write their own post
        -> Shared Post Model => allow user to share post from anther user
    
    --urls:
        -> using four endpoints:
            /post => allow user to post
            /post-list/{pk} => allow user to get posts of user
            /edit-post/<int:pk> => allow user to edit thier posts
            /{username}/<int:id>/share => allow user to share posts
            /sharedpost-list/{pk} => allow user to get shared posts of user
            /edit-sharedpost/<int:pk> => allow user to edit thier shared posts
                    ____________________________________________


*Likes App:
___________________
    
    --models:
        -> Like Written Posts Model => allow user to like written posts
        -> Like_Notification_on_WrittenPosts => notify user when he gets a like on thier posts
        -> Like Shared Post Model => allow user to like shared posts
        -> Like_Notification_on_SharedPosts => notify user when he gets a like on thier shared posts
    
    --urls:
        -> using six endpoints:
            like-written-post/<int:id>' => to like a written posts
            list-likes-on-written-post/<int:id>' => to show count and user who reacted on a written posts
            like-written-post-delete/<int:pk>' => to allow only owner of the like to delete it
            like-shared-post/<int:id>' => to like a shared posts
            list-likes-on-shared-post/<int:id> => to show count and user who reacted on a shared posts
            like-shared-post-delete/<int:pk> => to allow only owner of the like to delete it
            written-posts-likes-notifications => get a notification of any like on your written posts
            shared-posts-likes-notifications =>  get a notification of any like on your shard posts
                    ____________________________________________


*Comments App:
___________________
    
    --models:
        -> Comment Written Posts Model => allow you to comment on any post
        -> Comment Shared Post Model => allow you to comment on any shard post
        -> Comment Notification on WrittenPosts Model => get notifications if anyone commmented on your post
        -> Comment Notification on SharedPosts Model => get notifications if anyone commmented on your shared post
    
    --urls:
        -> using six endpoints:
            /comment-written-post/<int:id>' => to like a written posts
            /list-comment-on-written-post/<int:id>' => to show count and user who reacted on a written posts
            /delete-comment-on-written-post/<int:pk>' => to allow only owner of the like to delete it
            /comment-shared-post/<int:id>' => to like a shared posts
            /list-comment-on-shared-post/<int:id> => to show count and user who reacted on a shared posts
            /delete-comment-on-shared-post/<int:pk> => to allow only owner of the like to delete it
            /written-posts-comment-notification => get notifications when anyone comments on your post
            /shared-posts-comment-notification => get notificatios when anyone comments on your shared post
                    ____________________________________________

