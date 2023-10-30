
user = list()

def PostCreation():
    global user
    username = input("username:")
    caption = input("caption:")
    likes = 0
    comments = list()
    user.append({"username": username, "caption": caption, "likes": likes, "comments": comments})
    return "Post created"
    



def PostViewing():
    global user
    return user

def PostDeletion():
    try:
        ind = int(input("Post Index:"))
        global user
        user.pop(ind)
        return "Post deleted successfully"
    except:
        print("Please write correct Index")
        PostDeletion()

def LikeFeature():
    try:
        ind = int(input("Post Index to like:"))
        global user
        if(user[ind]):
            user[ind]["likes"] = user[ind]["likes"] + 1
            return user[ind]
        else:
            print("Please write correct Index")
            LikeFeature()
    except:
        print("Please write correct Index")
        LikeFeature()


def CommentFeature():
    try:
        ind = int(input("Post Index to comment:"))
        txt = input("write comment:")
        global user
        if(user[ind]):
            commentLst = list(user[ind]["comments"])
            commentLst.append(txt) 
            user[ind]["comments"] = commentLst
            return user[ind]
        else:
            print("Please write correct Index")
            CommentFeature()

    except:
        print("Please write correct Index")
        CommentFeature()



def WelcomeScreen():
    print("--------Facebook---------")
    print("     1. Post Creation    ")
    print("     2. Post Viewing     ")
    print("     3. Post Deletion    ")
    print("     4. Like Post        ")
    print("     5. Comment on Post  ")
    print("     6. Exit             ")
    print("-------------------------")
    try:
        opt = int(input("enter choice:"))
        if(opt == 1):
            val = PostCreation()
            print(val)
            WelcomeScreen()
        elif(opt == 2):
            print(PostViewing())
            WelcomeScreen()
        elif(opt == 3):
            print(PostDeletion())
            WelcomeScreen()
        elif(opt == 4):
            print(LikeFeature())
            WelcomeScreen()
        elif(opt == 5):
            print(CommentFeature())
            WelcomeScreen()
        elif(opt == 6):
            print("good bye...")
    except:
        print("please choose correct one")
        WelcomeScreen()

WelcomeScreen()