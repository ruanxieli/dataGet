# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 上午11:12
# @Author  : Xieli Ruan
# @Site    : 
# @File    : calc.py
# @Software: PyCharm
import datetime

def toDigiBox():
    boxOffices=[
        568254.0,267088,221345,174866,165206,155123,129912,118794,117990,115891,115301,112517,110949,104604,103780,77475,75611,74370,74050,73008,
        69653,69054,68611,62560,61010,60694,59030,57721,54938,53980,53473,52262,52110,47719,47427,46884,45932,43403,40952,40360,
        40185,40050,33990,31899,31385,31116,30416,29910,29517,29292,29184,27132,27022,26570,25162,24725,23710,23015,21886,21569,
        21393,21075,20248,20126,19842,19500,17555,17507,17392,17258,17053,16965,16072,15636,15237,14890,13979,13711,13576,13388,
        12614,12527,12425,12167,11369,10895,10883,10738,10602,10584,10371,10345,10296,10128,10010,9566,9176,8760,8143,7954,
        7866,7696,7648,7545,7484,7372,6951,6781,6685,6632,6535,6512,6485,6465,6370,6295,5938,5706,5622,5577,
        5446,5392,5064,5026,4778,4688,4476,4454,4369,4318,4298,4241,4199,4099,4072,4025,4020,3870,3740,3673,
        3317,3299,3261,3233,3169,3041,3040,3005,2946,2873,2750,2717,2616,2565,2555,2530,2519,2461,2430,2221,
        2144,2109,2023,1825,1783,1762,1762,1733,1717,1645,1625,1602,1591,1568,1510,1487,1473,1455,1412,1388,
        1369,1361,1355,1347,1294,1294,1287,1280,1277,1262,1251,1216,1210,1162,1151,1149,1137,1081,1033,1023,
        1015,1011,1006,982,982,963,940,937,905,903,890,882,872,847,840,818,798,796,793,777,
        770,769,766,754,710,710,704,681,651,610,593,592,570,554,548,547,509,502,496,491,
        487,484,473,470,467,458,451,447,435,430,393,391,387,384,377,377,376,375,374,370,
        369,367,354,335,334,329,325,315,314,308,307,306,292,291,291,268,266,257,251,244,
        243,240,236,234,233,228,227,227,226,226,222,215,214,214,206,206,203,200,199,198


    ]
    digiBoxOffices=[]
    for boxOffice in boxOffices:
        digiBoxOffices.append(round(100*boxOffice/sum(boxOffices),4))
    print(digiBoxOffices)

    # for i in boxOffices:
    #     print(i,round(100*i/sum(boxOffices),4))


def digiDate(releaseDate):
    date=datetime.datetime.strptime(releaseDate,'%Y-%m-%d')
    if date >=datetime.datetime(2016,12,29) and date<=datetime.datetime(2017,1,4):
        return 1
    elif date >=datetime.datetime(2017,1,25) and date<=datetime.datetime(2017,2,5):
        return 1
    elif date >=datetime.datetime(2017,3,31) and date<=datetime.datetime(2017,4,6):
        return 1
    elif date >=datetime.datetime(2017,4,27) and date<=datetime.datetime(2017,5,3):
        return 1
    elif date >=datetime.datetime(2017,5,26) and date<=datetime.datetime(2017,6,1):
        return 1
    elif date >=datetime.datetime(2017,9,29) and date<=datetime.datetime(2017,10,10):
        return 1
    else:
        return 0

def toDigidate():
    try:
        digiReleaseDate=[]
        fo = open('rawdate.txt', 'r')
        for line in fo.readlines():
            # print(line)
            digiReleaseDate.append(digiDate(line.strip('\n')))
        print(digiReleaseDate)

    finally:
        fo.close()


def toDigiLabel(str):
    Labels = ['剧情', '喜剧', '动作', '爱情', '科幻', '惊悚', '犯罪', '传记', '战争', '冒险', '灾难']
    label=[0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(Labels)):
        if Labels[i]==str:
            label[i]=1
            return label

def toDigiLabel2(str):
    Labels = ['剧情', '喜剧', '动作', '爱情', '科幻', '惊悚', '犯罪', '传记', '战争', '冒险', '灾难']
    res=[]

    for label in Labels:
        if label == str:
            res.append(1)
        else:
            res.append(0)
    return res

# print(toDigiLabel2('动作'))

filmName=["战狼2", "速度与激情8", "羞羞的铁拳", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "芳华", "加勒比海盗5：死无对证", "金刚：骷髅岛", "寻梦环游记", "极限特工：终极回归", "生化危机：终章", "乘风破浪", "神偷奶爸3", "蜘蛛侠：英雄归来", "大闹天竺", "雷神3：诸神黄昏", "猩球崛起3：终极之战", "金刚狼3：殊死一战", "悟空传", "正义联盟", "银河护卫队2", "新木乃伊", "神奇女侠", "一条狗的使命", "美女与野兽", "追龙", "情圣", "英伦对决", "三生三世十里桃花", "杀破狼·贪狼", "熊出没·奇幻空间", "星球大战外传：侠盗一号", "王牌特工2：黄金圈", "妖猫传", "缝纫机乐队", "全球风暴", "星际特工：千星之城", "建军大业", "嫌疑人x的献身", "拆弹·专家", "敦刻尔克", "空天猎", "太空旅客", "异形：契约", "心理罪", "奇门遁甲", "前任3：再见前任", "记忆大师", "机器之血", "天才枪手", "铁道飞虎", "绣春刀II：修罗战场", "妖铃铃", "爱乐之城", "侠盗联盟", "东方快车谋杀案", "京城81号2", "欢乐好声音", "心理罪之城市之光", "喜欢·你", "攻壳机动队", "逆时营救", "帕丁顿熊2", "长城", "春娇救志明", "大话西游之大圣娶亲", "蓝精灵：寻找神秘村", "看不见的客人", "二十二", "二代妖精之今生有幸", "刺客信条", "非凡任务", "解忧杂货店", "哆啦A梦：大雄的南极冰冰凉大冒险", "王牌保镖", "赛车总动员3：极速挑战", "异星觉醒", "十万个冷笑话2", "大卫贝肯之倒霉特工熊", "父子雄兵", "傲娇与偏见", "决战食神", "鲛珠传", "降临", "极盗车神", "十八洞村", "追捕", "东北往事之破马张飞", "七十七天", "赛尔号大电影6：圣者无敌", "游戏规则", "绝世高手", "冈仁波齐", "绑架者", "降魔传", "大护法", "银魂 真人版", "密战", "烟花", "银翼杀手2049", "摆渡人", "原谅他77次", "血战钢锯岭", "血战湘江", "反转人生", "狂兽", "欢乐喜剧人", "至爱梵高·星空之谜", "龙之战", "荡寇风云", "闪光少女", "破·局", "疯岳撬佳人", "明月几时有", "合约男女", "亚瑟王：斗兽争霸", "我的爸爸是森林之王", "巨额来电", "这就是命", "刀剑神域：序列之争", "昆塔：反转星球", "引爆者", "地球：神奇的一天", "常在你左右", "喵星人", "声之形", "魔弦传说", "冰雪大作战", "大耳朵图图之美食狂想曲", "猪猪侠之英雄猪少年", "乐高蝙蝠侠大电影", "钢铁飞龙之再见奥特曼", "李雷和韩梅梅——昨日重现", "毒。诫", "了不起的菲丽西", "鲨海", "有完没完", "至暗时刻", "黑白迷宫", "重返·狼群", "英雄本色", "麻烦家族", "玩偶奇兵", "青禾男高", "阿唐奇遇", "超凡战队", "烽火芳菲", "最终幻想15：王者之剑", "\"吃吃\"的爱", "暴雪将至", "二次初恋", "精灵宝可梦：波尔凯尼恩与机巧的玛机雅娜", "忠爱无言", "冰雪女王2：冬日魔咒", "血狼犬", "三只小猪2", "天生不对", "嘉年华", "托马斯大电影之了不起的比赛", "恐袭波士顿", "守护者：世纪战元", "相爱相亲", "相声大电影之我要幸福", "美好的意外", "极致追击", "天空之眼", "雄狮", "缉枪", "抢红", "健忘村", "豆福传", "我的爸爸是国王", "请把你的窗户打开", "神秘家族", "天才捕手", "当怪物来敲门", "维京:王者之战", "深夜食堂2", "提着心，吊着胆", "上海王", "情遇曼哈顿", "与君相恋100次", "玩命直播", "临时演员", "那年夏天你去了哪里", "笨贼别跑", "碟仙诡谭2", "海洋奇缘", "麦兜响当当", "潜艇总动员之时光宝盒", "兄弟，别闹！", "六年，六天", "灵狼传奇", "怨灵2", "你若安好", "你的名字。", "捍卫者", "推理笔记", "中国推销员", "异兽来袭", "美容针", "冒牌卧底", "仙球大战", "回到火星", "一念无明", "夏天19岁的肖像", "绿野仙踪之奥兹国奇幻之旅", "勇往直前", "我是马布里", "那一场呼啸而过的青春", "以爱为名", "时间去哪儿了", "完美有多美", "海边的曼彻斯特", "萤火奇兵", "秘果", "我是医生", "不成问题的问题", "我不做大哥好多年", "罗曼蒂克消亡史", "会痛的十七岁", "你好，疯子！", "玛格丽特的春天", "不期而遇", "迷失Z城", "一路绽放", "小猫巴克里", "失业生", "咕噜咕噜美人鱼2", "惊魂绣花鞋", "笔仙咒怨", "和田玉传奇", "单身日记：好孕来袭", "假如王子睡着了", "李三娘", "恐怖理发店", "疯狂特警队", "20:16", "圣诞奇妙公司", "怪物岛", "借眼", "通灵姐妹", "胡杨的夏天", "S的秘密", "指甲刀人魔", "窦娥奇冤", "八月", "垫底联盟", "刺杀盖世太保", "回马亭", "惊天解密", "守信少年", "夜色撩人", "诡域新娘", "圣诞大赢家", "一万公里的约定", "点五步", "咕噜咕噜美人鱼", "深宫怨灵", "青春逗", "夺金四贱客", "大象林旺之一炮成名", "蝴蝶公墓", "皮绳上的魂", "双面劫匪", "碟仙前传", "少年巴比伦", "碟仙之毕业照", "超能龙骑侠", "花腰恋歌", "七月半3：灵触第七感", "一路逆风", "小情书", "怨灵宿舍之白纸女生", "恐怖电影院2", "银河守卫队", "神奇动物在哪里", "恐怖毕业照2", "煎饼侠", "火力全开", "撞邪31号", "理查大冒险", "午夜惊魂路", "六人晚餐", "纯洁心灵·逐梦演艺圈", "箭士柳白猿", "真假森林王", "因为爱情", "乡关何处", "初恋日记", "夜半凶铃", "心惊胆战", "你在哪", "老兽", "天梯：蔡国强的艺术", "冒牌监护人之寻宝闹翻天", "辛巴达与美人鱼公主", "麦兜当当伴我心"]
i=1
while (i<len(filmName)):
    print(filmName[i])
    i+=20
# print(len(filmName))