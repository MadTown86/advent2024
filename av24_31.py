import re as r

def main():
    res = 0
    with open("av24_3_input.txt", 'r') as file:
        blobbiekins = file.read()
    
    example = """*who():mul(420,173)what()*~why() select()how()-mul(448,672)mul(914,202){^{why()];<&;/mul(748,792)what(),$from()what()when()mul(399,982)<;)]]mul(347,549)@;*);mul(655,663) @select()~%,$#mul(535,284)*--@()]+~mul(2,513)why()mul(239,99)!<mul(2,988)@mul(971,404)?&from()mul(660,516)-;what();how()+!why()mul(612,994)'[mul(253,728)<-mul(208,621)>?}( #]mul(162,534)#+how()}<&what();mul(685,182)mul(146,549)mul(659,511)mul(283,734)*/don't()/mul(579,121)what()mul(790,893)where()@)-{#!who()((mul(985,741)when(),$where()>do()<~''-~-mul(961,154),]select()(select()@what()mul(840,357)] when()mul(47,948))]?what()+*;+mul(331,33)who();&~~mul(983,456)mul(660,500)who()mul(414,834)where()^({>mul(961,732)#^]how()'"""

    cutdown = """mul(420,173)mul(448,672)mul(914,202)mul(748,792)mul(399,982)mul(347,549)mul(655,663)mul(535,284)mul(2,513)mul(239,99)mul(2,988)mul(971,404)mul(660,516)mul(612,994)mul(253,728)mul(208,621)mul(162,534)mul(685,182)mul(146,549)mul(659,511)mul(283,734)mul(579,121)mul(790,893)mul(985,741)mul(961,154)mul(840,357)mul(47,948)mul(331,33)mul(983,456)mul(660,500)mul(414,834)mul(961,732)"""
    # Process matches with re module
    pattern = r'mul\((.*?)\)'
    matches = r.findall(pattern, blobbiekins)

    for match in matches:
        line = match.split(",")
        if len(line) == 2:
            x, y = line
            if x.isdigit() and y.isdigit():
                res += int(x) * int(y)
            else:
                continue
    

    return res

if __name__ == "__main__":
    # 158982546 - this was too low have to check the regex
    print(main())