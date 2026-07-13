post = "Ajay is a hardworking and determined person who never gives up on his dreams. He believes that success comes through consistent effort and learning. No matter how difficult the journey becomes, Ajay keeps moving forward with confidence."

name = input("Enter Your name: ")
name1 = "Ajay"
if name1.lower() in name.lower():
    if name1.lower() in post.lower():
        print("Yes, This paragraph talking about Ajay")

else:
    print("NO, This post not talking about Ajay!..")