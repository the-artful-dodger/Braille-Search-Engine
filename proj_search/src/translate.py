# -*- coding: utf-8 -*-

ENG_TO_BRAILLE = {"a":1, "b":12, "c":14, "d":145,
                  "e":15, "f":124, "g":1245, "h":125,
                  "i":24, "j":245, "k":13, "l":123,
                  "m":134, "n":1345, "o":135, "p":1234,
                  "q":12345, "r":1235, "s":234, "t":2345,
                  "u":136, "v":1236, "w":2456, "x":1346,
                  "y":13456, "z":1356, "#":3456}

DOT_PATTERN_TO_BRAILLE = {0:"⠀",1:"⠁",2:"⠂",12:"⠃",3:"⠄",13:"⠅",23:"⠆",123:"⠇",4:"⠈",14:"⠉",24:"⠊",
                         124:"⠋",34:"⠌",134:"⠍",234:"⠎",1234:"⠏",5:"⠐",15:"⠑",25:"⠒",125:"⠓",35:"⠔",
                         135:"⠕",235:"⠖",1235:"⠗",45:"⠘",145:"⠙",245:"⠚",1245:"⠛",345:"⠜",1345:"⠝",
                         2345:"⠞",12345:"⠟",6:"⠠",16:"⠡",26:"⠢",126:"⠣",36:"⠤",136:"⠥",236:"⠦",1236:"⠧",
                         46:"⠨",146:"⠩",246:"⠪",1246:"⠫",346:"⠬",1346:"⠭",2346:"⠮",12346:"⠯",56:"⠰",
                         156:"⠱",256:"⠲",1256:"⠳",356:"⠴",1356:"⠵",2356:"⠶",12356:"⠷",456:"⠸",1456:"⠹",
                         2456:"⠺",12456:"⠻",3456:"⠼",13456:"⠽",23456:"⠾",123456:"⠿",7:"⡀",17:"⡁",27:"⡂",
                         127:"⡃",37:"⡄",137:"⡅",237:"⡆",1237:"⡇",47:"⡈",147:"⡉",247:"⡊",1247:"⡋",347:"⡌",
                         1347:"⡍",2347:"⡎",12347:"⡏",57:"⡐",157:"⡑",257:"⡒",1257:"⡓",357:"⡔",1357:"⡕",
                         2357:"⡖",12357:"⡗",457:"⡘",1457:"⡙",2457:"⡚",12457:"⡛",3457:"⡜",13457:"⡝",
                         23457:"⡞",123457:"⡟",67:"⡠",167:"⡡",267:"⡢",1267:"⡣",367:"⡤",1367:"⡥",2367:"⡦",
                         12367:"⡧",467:"⡨",1467:"⡩",2467:"⡪",12467:"⡫",3467:"⡬",13467:"⡭",23467:"⡮",
                         123467:"⡯",567:"⡰",1567:"⡱",2567:"⡲",12567:"⡳",3567:"⡴",13567:"⡵",23567:"⡶",
                         123567:"⡷",4567:"⡸",14567:"⡹",24567:"⡺",124567:"⡻",34567:"⡼",134567:"⡽",234567:"⡾",
                         1234567:"⡿",8:"⢀",18:"⢁",28:"⢂",128:"⢃",38:"⢄",138:"⢅",238:"⢆",1238:"⢇",48:"⢈",
                         148:"⢉",248:"⢊",1248:"⢋",348:"⢌",1348:"⢍",2348:"⢎",12348:"⢏",58:"⢐",158:"⢑",
                         258:"⢒",1258:"⢓",358:"⢔",1358:"⢕",2358:"⢖",12358:"⢗",458:"⢘",1458:"⢙",2458:"⢚",
                         12458:"⢛",3458:"⢜",13458:"⢝",23458:"⢞",123458:"⢟",68:"⢠",168:"⢡",268:"⢢",1268:"⢣",
                         368:"⢤",1368:"⢥",2368:"⢦",12368:"⢧",468:"⢨",1468:"⢩",2468:"⢪",12468:"⢫",3468:"⢬",
                         13468:"⢭",23468:"⢮",123468:"⢯",568:"⢰",1568:"⢱",2568:"⢲",12568:"⢳",3568:"⢴",13568:"⢵",
                         23568:"⢶",123568:"⢷",4568:"⢸",14568:"⢹",24568:"⢺",124568:"⢻",34568:"⢼",134568:"⢽",
                         234568:"⢾",1234568:"⢿",78:"⣀",178:"⣁",278:"⣂",1278:"⣃",378:"⣄",1378:"⣅",2378:"⣆",
                         12378:"⣇",478:"⣈",1478:"⣉",2478:"⣊",12478:"⣋",3478:"⣌",13478:"⣍",23478:"⣎",123478:"⣏",
                         578:"⣐",1578:"⣑",2578:"⣒",12578:"⣓",3578:"⣔",13578:"⣕",23578:"⣖",123578:"⣗",4578:"⣘",
                         14578:"⣙",24578:"⣚",124578:"⣛",34578:"⣜",134578:"⣝",234578:"⣞",1234578:"⣟",678:"⣠",
                         1678:"⣡",2678:"⣢",12678:"⣣",3678:"⣤",13678:"⣥",23678:"⣦",123678:"⣧",4678:"⣨",
                         14678:"⣩",24678:"⣪",124678:"⣫",34678:"⣬",134678:"⣭",234678:"⣮",1234678:"⣯",5678:"⣰",
                         15678:"⣱",25678:"⣲",125678:"⣳",35678:"⣴",135678:"⣵",235678:"⣶",1235678:"⣷",45678:"⣸",
                         145678:"⣹",245678:"⣺",1245678:"⣻",345678:"⣼",1345678:"⣽",2345678:"⣾",12345678:"⣿"}


def convert(sentence):
    l_s = list(sentence.lower())
    for id, k in enumerate(l_s):
        if k in ENG_TO_BRAILLE:
            l_s[id] = ENG_TO_BRAILLE[k]
        else:
            l_s[id] = 0

    res = []

    for k in l_s:
        res.append(DOT_PATTERN_TO_BRAILLE[k])

    return res

print convert('hello')