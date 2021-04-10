from chatbot import WXChatBot

bot = WXChatBot()

def get_response_dict(question):
    global  bot
    return bot.get_response_dict(question)

if __name__ == '__main__':
    p_list = ['你好','我是路人甲','我心绞痛','应该是痛风性心肌病','怎么治疗','我疲劳','我还有点胸痛','最近还有点头晕','有什么忌口',
                 '多大概率能治好','怎么预防','用什么药物治疗','治疗周期是多久']
    for p in p_list:
        print(bot.get_response_dict(p))