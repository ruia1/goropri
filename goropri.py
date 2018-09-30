import csv
from random import randint
gcsv = "goro.csv"
goros = []

from random import randint
from math import sqrt
def milpri(n):
    if type(n) != int or n < 2: return False
    if n == 2: return True
    if n & 1 == 0: return False
    if n < 5000:
        for i in range(3,int(sqrt(n))+1,2):
            if n%i == 0: return False
        return True
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for i in range(100):
        a = randint(1,n-1)
        t = d
        y = pow(a, t, n)
        while t !=n - 1 and y != 1 and y != n -1:
            y = (y * y) % n
            t <<= 1
        if y != n - 1 and t & 1 == 0: return False
    return True

class goro:
    count = 0
    def __init__(self,num,gint,gchar,gilen=0,gclen=0):
        goro.count = int(num)
        self.num = int(num)
        self.gint = int(gint)
        self.gchar = gchar
        if gilen == 0:
            self.gilen = len(str(gint))
        else:
            self.gilen = int(gilen)
        if gclen == 0:
            self.gclen = len(gchar)
        else:
            self.gclen = int(gclen)
    def getgint(self):
        return self.gint
    def seqence(self):
        return [self.num,self.gint,self.gchar,self.gilen,self.gclen]
    def seqencenonum(self):
        return [self.gint,self.gchar,self.gilen,self.gclen]
    
class finds:
    def __init__(self,fgoro = 0,fmax = 0,fmin = 0,fmany = 5,printcount = 0,fvalue = 0,flis = [],lenflis = 1):
        self.fgoro = fgoro
        self.fmax = fmax
        self.fmin = fmin
        self.fmany = fmany
        self.printcount = printcount
        self.fvalue = fvalue
        self.flis = flis
        self.lenflis = lenflis
        self.setupf()
    
    def setupf(self):
        del self.flis
        self.flis = []
        for gc in range(self.lenflis):
            self.flis.append(self.fvalue // (goro.count ** gc) % goro.count)

    def addf(self,increminal = 1):
        self.fvalue += increminal
        if self.fvalue != 0:
            i = self.fvalue
            self.lenflis = 0
            while i != 0:
                self.lenflis += 1
                i //= goro.count
        self.setupf()
        
    def orend(self):
        if self.fvalue > goro.count ** goro.count or self.orendsub():
            return True
        return False
    
    def orendsub(self):
        if self.printcount >= self.fmany:
            return True
        return False

def setupgoro():
    with open(gcsv,'r') as f:
        rd = csv.reader(f)
        global goros
        del goros
        goros = []
        for row in rd:
            try:
                new = goro(row[0],row[1],row[2],row[3],row[4])
                goros.append(new)
            except IndexError:
                pass
    return

def updategoro(goroup):
    with open(gcsv,'a') as f:
        w = csv.writer(f)
        w.writerow(goroup.seqence())

def standardsetup():
    setupgoro()
    for gr in [[523,"ごつみ"],[593,"コックさん"],[443,"しじみ"],[653,"婿さん"],[425,"四つ子"]]:
        k = True
        for row in goros:
            if gr[0] == row.gint or gr[1] == row.gchar:
                k = False
                break
        if k:
            updategoro(goro(goro.count+1,gr[0],gr[1]))
    
def goromake():
    orcontinue = 1
    setupgoro()
    if goro.count == 0:
        print("語呂が登録されていません。基本セットを登録しますか？"+
              "はい：１ いいえ：０ を入力してください。")
        stnup = input()
        print()
        if stnup in ["1","１"]:
            print("基本セットを登録しました。")
            standardsetup()
            print("続けて登録しますか？　はい：１ いいえ：０ を入力してください。")
            orcontinue = input()
            print()
            try:
                orcontinue = int(orcontinue)
            except ValueError:
                orcontinue = 0
    if orcontinue == 1:
        print("語呂を登録します。「end」を入力することでいつでも登録を終了できます。")
    while orcontinue == 1:
        print("語呂のパーツとなる数字を入力してください。")
        maknumber = input()
        print()
        if maknumber == "end":
            print("メニューに戻ります。\n")
            return
        try:
            maknumber = int(maknumber)
        except ValueError:
            print("正しい値を入力してください。登録に失敗しました。\n")
            continue
        print("数字の語呂を入力してください。")
        makgoro = input()
        if makgoro == "end":
            print("メニューに戻ります。\n")
            return
        print("\n数字：" + str(maknumber) + " 語呂：" + makgoro + " で登録します。よろしいですか？\n"+
              "はい：１ いいえ：０ を入力してください。")
        ok = input()
        print()
        if ok == "end":
            print("メニューに戻ります。\n")
            return
        if ok in ["1","１"]:
            setupgoro()
            ok2 = True
            for row in goros:
                if maknumber == row.gint or makgoro == row.gchar:
                    ok2 = False
                    break
            if ok2:
                updategoro(goro(goro.count+1,maknumber,makgoro))
                print("登録に成功しました。")
            else:
                print("既に登録されています。登録に失敗しました。")
        else:
            print("登録しませんでした。")
        print("登録を続けますか？　はい：１ いいえ：０ を入力してください。")
        try:
            orcontinue = int(input())
            print()
        except ValueError:
            orcontinue = 0
            print()
    print("メニューに戻ります。\n")
    
def goroprintlist():
    global goros
    setupgoro()
    print('{: <3}'.format("番号"),'{: <16}'.format("語呂の数"),"語呂")
    for row in goros:
        print('{: <5}'.format(str(row.num)),'{: <20}'.format(str(row.gint)),row.gchar)
    print("")

def delgoro():
    goro.count = 0
    setupgoro()
    if goro.count == 0:
        print("語呂が登録されていません。語呂を登録してください。\n")
        return
    while True:
        print("語呂を削除します。「end」を入力することでいつでも削除を終了できます。")
        goroprintlist()
        print("削除する語呂を、番号で選択してください。")
        delg = input()
        print()
        if delg == "end":
            print("メニューに戻ります。\n")
            return
        try:
            delg = int(delg)
        except ValueError:
            print("正しい値を入力してください。")
            continue
        if delg not in range(1,goro.count+1):
            print("正しい値を入力してください。")
            continue
        print(str(delg) + "番目の" + str(goros[delg-1].gint) + ":" + goros[delg-1].gchar + "を削除します。よろしいですか？\n"+
              "はい：１ いいえ：０ を入力してください。")
        ok = input()
        print()
        if ok == "end":
            print("メニューに戻ります。\n")
        with open(gcsv,'w') as f:
            count = 1
            w = csv.writer(f)
            for i in goros:
                if i.num != delg:
                    w.writerow([str(count)] + i.seqencenonum())
                    count += 1
        goro.count = 0
        setupgoro()
        if goro.count == 0:
            print("語呂が登録されていません。語呂を登録してください。\n")
            return
        print("削除を続けますか？　はい：１ いいえ：０ を入力してください。")
        if input() in ["1","１"]:
            continue
        else:
            print("メニューに戻ります。\n")
def arrayispri():
    global findp
    reti = "" #returnint
    retc = "" #returnchar
    relen = 0
    for i in findp.flis:
        reti += str(goros[i].getgint())
        retc += goros[i].gchar
        relen += goros[i].gilen
    try:
        re = int(reti)
        if ((findp.fgoro == 0 or ((findp.fgoro - 1) in findp.flis))
            and (findp.fmax == 0 or findp.fmax >= relen)
            and (findp.fmin == 0 or findp.fmin <= relen) and milpri(re)):
            print('{:<30}'.format(re),":",retc)
            findp.printcount += 1
    except ValueError:
        pass
    findp.addf()
    return

def findpri():
    global findp
    while not findp.orend():
        arrayispri()
    if not findp.orendsub():
        print(findp.fmany,"個は見つかりませんでした。")
        del findp
                   
def findprimenu():
    orcontinue = "1"
    global findp
    while orcontinue in ["1","１"]:
        setupgoro()
        if goro.count == 0:
            print("語呂が登録されていません。基本セットを登録しますか？"
                  +"はい：１ いいえ：０ を入力してください。")
            stnup = input()
            if stnup in ["1","１"]:
                standardsetup()
                print("続けて登録しますか？　はい：１ いいえ：０ を入力してください。")
                orcontinue = input()
                print()
                continue
            else:
                print("語呂を登録してください。\n")
                break
        findp = finds()
        print(goro.count,"個の語呂から、語呂素数を生成します。\n"
              ,"「end」を入力することでいつでも生成を終了できます。")
        goroprintlist()
        print("探索する素数に含まれる語呂を、データベースの番号で入力してください。\n"
                      +"すべての設定を指定しない場合、rを入力してください。\n"
                      +"指定しない場合は、0を入力してください。")
        fgoro = input()
        print()
        if fgoro == "end":
            print("メニューに戻ります。\n")
            return
        elif fgoro == "r":
            print("探索を開始します。")
            del findp
            findp = finds()
            findpri()
        else:
            try:
                findp.fgoro = int(fgoro)
            except ValueError:
                print("正しい値を入力してください。")
                continue
            print("探索する素数の、最大の桁数を入力してください。指定しない場合は、０を入力してください。最大値は３０です。")
            fmax = input()
            print()
            if fmax == "end":
                print("メニューに戻ります。\n")
                return
            else:
                try:
                    findp.fmax = int(fmax)
                except ValueError:
                    print("正しい値を入力してください。")
                    continue
                if findp.fmax != 0 and findp.fmax < 2:
                    print("正しい値を入力してください。")
                    continue
                print("探索する素数の、最小の桁数を入力してください。指定しない場合は、０を入力してください。")
                fmin = input()
                print()
                if fmin == "end":
                    print("メニューに戻ります。\n")
                    return
                try:
                    findp.fmin = int(fmin)
                except ValueError:
                    print("正しい値を入力してください。")
                    continue
                if findp.fmin < 0 or (findp.fmax != 0 and findp.fmax < findp.fmin):
                    print("正しい値を入力してください。")
                    continue
                else:
                    print("探索する素数の数を入力してください。指定しない場合は０を入力してください。規定値は５、最大値は５０です。")
                    fmany = input()
                    print()
                    if fmany == "end":
                        print("メニューに戻ります。\n")
                        return
                    try:
                        findp.fmany = int(fmany)
                    except ValueError:
                        print("正しい値を入力してください。")
                        continue
                    if findp.fmany < 0 or findp.fmany > 50:
                        print("正しい値を入力してください。")
                        continue
                    elif findp.fmany == 0:
                        findp.fmany = 5
                    print("探索を開始します。")
                    findpri()
        print("続けますか？ はい：１ いいえ：０ を入力してください。")
        orcontinue = input()
        print()
    print("メニューに戻ります。\n")
                     
def jump(jmode):
        if jmode == "find":
            findprimenu()
        elif jmode == "standard":
            standardsetup()
            print("基本セットを登録しました。")
        elif jmode == "g.entry":
            goromake()
        elif jmode == "g.list":
            goroprintlist()
        elif jmode == "g.del":
            delgoro()
        else:
            print("正しい値を入力してください。\n")
        return
            
def menu():
    while True:
        print("詳細メニューです。行いたい操作のコードを入力してください。\n"+
                      "ホーム：home 終了：end\n"+
                      "語呂素数生成：find 語呂登録：g.entry 語呂削除：g.del 登録された語呂一覧：g.list")
        mmode = input()
        if mmode == "end":
            print("終了します。\n")
            if '__main__'==__name__:
                input("終了するにはエンターを押してください...")
            return True
        elif mmode == "home":
            print("\nホームに戻ります。\n")
            return False
        else:
            print()
            jump(mmode)

def openg():
    try:
        f = open(gcsv,'x')
        f.close()
        print("語呂ファイルが存在しないため、新規作成しました。\n")
    except FileExistsError:
        print("語呂ファイルのオープンに成功しました。\n")
def gohome():
    openg()
    while True:
        print("語呂モードホームメニューです。行いたい操作のコードを入力してください。\n"+
              "語呂素数生成：find 語呂登録：g.entry 詳細メニュー：menu 終了：end\n")
        mode = input()
        if mode == "end":
            print("終了します。\n")
            if '__main__'==__name__:
                input("終了するにはエンターを押してください...")
            return
        elif mode == "menu":
            menureturn = menu()
            if menureturn:
                return
        else:
            jump(mode)
            
if '__main__'==__name__:
    gohome()
