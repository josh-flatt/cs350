from User import *

def test_email(object, input : str, expected : str):
    object.set_email(input)
    result = object.get_email()
    if result == expected:
        return True
    else:
        return False
    
if __name__ == "__main__":
    testGuy = User("tester", "1234", "tester@tester.com")
    print(test_email(testGuy, "newguy@cool.com", "newguy@cool.com"))
