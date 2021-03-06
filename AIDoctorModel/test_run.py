from chatbot import WXChatBot

if __name__ == '__main__':
    bot = WXChatBot()

    # bot.inter_start()
    bot.local_start()

    name = '感冒'
    cannot_list = ['什么药治疗','为什么会头疼']
    #为了测试 intent所问的问题
    intent_list = ['感冒的症状','怎么会感冒','感冒并发症','什么药治疗感冒','请问感冒的治疗周期',
              '多大概率能治好感冒','感冒怎么预防']
    #测试 sysptom
    sysptom_list = ['我心绞痛','我耳堵']
    #患病概率
    prob_list = ['多大概率能治好感冒']
    test_list = ['感冒的症状','多大概率能治好','我心绞痛','肺动脉高压','怎么治疗','复方胆通胶囊能治疗什么',
                 '我疲劳','我还有点恶心与呕吐','有什么忌口']
    test_list = ['你好','我是路人甲','我心绞痛','应该是肺动脉高压','怎么治疗','我疲劳','我还有点恶心与呕吐','最近还有点抑郁','有什么忌口',
                 '多大概率能治好','怎么预防','用什么药物治疗','治疗周期是多久']
    test_list  = ['你好','我是路人甲','我心绞痛','应该是痛风性心肌病','怎么治疗','我疲劳','我还有点胸痛','最近还有点头晕','有什么忌口',
                 '多大概率能治好','怎么预防','用什么药物治疗','治疗周期是多久']

    bot.my_test(test_list)