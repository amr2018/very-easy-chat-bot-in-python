

text = '''
My name is Amr | my age is 18 year | I live in Egypt | I live alone |
 I have a friend who is you | I hope to love, but I do not have money
 | I'm here to help you I love computer science and programming
 | I cannot live alone for long, that's why I'm talking to you
 | I cannot understand some of the messages but I try to be better I'm fine now

'''

class ChatBot:
    def __init__(self, text):
        self.message = input(': ').lower()
        self.my_story = text.lower().split('|')


    def chat(self):
        if self.message != '':
            count = 0
            Similarity_count = []
            for i in self.my_story:
                for word in self.message.split(' '):
                    if word in i:
                        count += 1

                Similarity_count.append(count)
                count = 0

            large_num = max(Similarity_count)
            index = Similarity_count.index(large_num)
            result = self.my_story[index]
            print(result)

while True:
    c = ChatBot(text)
    c.chat()
