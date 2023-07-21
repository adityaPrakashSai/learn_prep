
"""
Factory Design Pattern
    - Creational design pattern
    - Objects are created without exposing the logic to the client.
    - the client uses the same common interface to create the new type of object.

Example:
notifications: SMS, Email, Push

"""
class SMSNotifier:
    def notify(self):
        print("SMS notification sent")

class EmailNotifier:
    def notify(self):
        print("Email notification sent")

class PushNotifier:
    def notify(self):
        print("Push notification sent")

def Factory(notification_type):

    notifiers = {"SMS":SMSNotifier,
                 "Email":EmailNotifier,
                 "Push":PushNotifier}
    return notifiers[notification_type]()


if __name__ == "__main__":
    
    sms = Factory("SMS")
    email = Factory("Email")
    push = Factory("Push")
    
    sms.notify()
    email.notify()
    push.notify()


# Another Example
class FrenchTranslator:

    def __init__(self):
        self.translations = {"word1": "french_word1",
                             "word2": "french_word2", 
                             "word3": "french_word3",}
    def translate(self, word):
        return self.translations[word]
    
class SpanishTranslator:

    def __init__(self):
        self.translations = {"word1": "spanish_word1",
                             "word2": "spanish_word2", 
                             "word3": "spanish_word3",}
    def translate(self, word):
        return self.translations[word]
    
class EnglishTranslator:

    def translate(self, word):
        return word
    
def Factory(language = "English"):

    translators = {"French": FrenchTranslator,
                   "English": EnglishTranslator,
                   "Spanish": SpanishTranslator}
    return translators[language]()

if __name__ == "__main__":
    
    f = Factory("French")
    e = Factory("English")
    s = Factory("spanish")
    
    f.translate()
    e.translate()
    s.translate()
