import re

def reformat():

    p = re.compile('>.*<')

    corpcode_path = './CORPCODE.xml'
    with open(corpcode_path, 'r', encoding='utf8') as f:
        res = ''
        cnt = 0
        for line in f:
            m = p.search(line)
            if m:
                s = m.group()[1:-1]
                res += s
                if cnt < 3:
                    res += ', '
                    cnt += 1
                else:
                    res += '\n'
                    cnt = 0
        
        with open('./CORPCODE.txt', mode='w', encoding='utf8') as f:
            f.write(res)
