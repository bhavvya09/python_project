from project import speak


def main():
    test_speak()
    test_wishMe()
    test_takeCommand()

#Lets test speak


def test_speak():
    assert speak("Hello")==0
    assert speak("Hello,Bhavya")==0
    assert speak("Hello Bhavya. Iam Dora Maam")==0

#Now testing WishMe

def test_wishMe():
    assert speak[0] == "Good Morning Bhavya!"
    assert speak[1] == "I am Dora Maam. Please tell me how may I help you"

    
#lets test takeCommand


def test_takeCommand():
    
    assert speak[0] == "Listening..."
    assert speak[1] == "Recognizing..."
    assert speak[2] == "User said: Hello, world!"

   