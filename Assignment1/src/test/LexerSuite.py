import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_LS1(self):
        self.assertTrue(TestLexer.test("ABC", "ABC,<EOF>", 101))

    def test_LS2(self):
        self.assertTrue(TestLexer.test("12234", "12234,<EOF>", 102))

    def test_LS3(self):
        self.assertTrue(TestLexer.test("2131234_12342134_1", "2131234_12342134_1,<EOF>", 103))

    def test_LS4(self):
        self.assertTrue(TestLexer.test("bruh bruh lmeo", "bruh,bruh,lmeo,<EOF>", 104))

    def test_LS5(self):
        self.assertTrue(TestLexer.test("asdfsdafasdfdsfasdf", "asdfsdafasdfdsfasdf,<EOF>", 105))

    def test_LS6(self):
        self.assertTrue(TestLexer.test("ab_sdfsd_sdfc_", "ab_sdfsd_sdfc_,<EOF>", 106))

    def test_LS7(self):
        self.assertTrue(TestLexer.test("test_LS 8 asdasdq123 DSF dsfsdq213ASF 2saf2kalutyIUOY","test_LS,8,asdasdq123,DSF,dsfsdq213ASF,2,saf2kalutyIUOY,<EOF>",107))

    def test_LS8(self):
        self.assertTrue(TestLexer.test("abc dasd 98asd  JKUG gjhg12 [sad] sadukjh]", "abc,dasd,98,asd,JKUG,gjhg12,[,sad,],sadukjh,],<EOF>", 108))

    def test_LS9(self):
        self.assertTrue(TestLexer.test("1+1=3", "1,+,1,=,3,<EOF>", 109))

    def test_LS10(self):
        self.assertTrue(TestLexer.test("asdf +f dshj+sa g-sadw21 hga*", "asdf,+,f,dshj,+,sa,g,-,sadw21,hga,*,<EOF>", 110))

    def test_LS11(self):
        self.assertTrue(TestLexer.test("i<3u", "i,<,3,u,<EOF>", 111))

    def test_LS12(self):
        self.assertTrue(TestLexer.test("ewrw<wq.QWE>eqw", "ewrw,<,wq,.,QWE,>,eqw,<EOF>", 112))

    def test_LS13(self):
        self.assertTrue(TestLexer.test("1_234_128765e+1632", "1_234_128765e+1632,<EOF>", 113))

    def test_LS14(self):
        self.assertTrue(TestLexer.test(":a:ghje34:,dsfeiewqo.", ":,a,:,ghje34,:,,,dsfeiewqo,.,<EOF>", 114))

    def test_LS15(self):
        self.assertTrue(TestLexer.test("{please give me the bezt score}", "{,please,give,me,the,bezt,score,},<EOF>", 115))

    def test_LS16(self):
        self.assertTrue(TestLexer.test(""" 13.987235e123 """, """13.987235e123,<EOF>""", 116))

    def test_LS17(self):
        self.assertTrue(TestLexer.test(""" "abc" """, """"abc",<EOF>""", 117))

    def test_LS18(self):
        self.assertTrue(TestLexer.test(""" "abc\t" """, """"abc\t",<EOF>""", 118))

    def test_LS19(self):
        input = """ "hjhasdfasdk\n" """
        expect = """Unclosed String: "hjhasdfasdk"""
        self.assertTrue(TestLexer.test(input,expect,119))

    def test_LS20(self):
        self.assertTrue(TestLexer.test(""" "hi jghadsf qwyu3iter" """, """"hi jghadsf qwyu3iter",<EOF>""", 120))

    def test_LS21(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 121))

    def test_LS22(self):
        self.assertTrue(TestLexer.test("+-*/", "+,-,*,/,<EOF>", 122))

    def test_LS23(self):
        self.assertTrue(TestLexer.test("auto break do else", "auto,break,do,else,<EOF>", 123))

    def test_LS24(self):
        self.assertTrue(TestLexer.test(""" abc \" def """, """abc,Unclosed String: " def """, 124))

    def test_LS25(self):
        self.assertTrue(TestLexer.test("abc + -", "abc,+,-,<EOF>", 125))

    def test_LS26(self):
        self.assertTrue(TestLexer.test("! == ^ & != && * % $ ... ","!,==,Error Token ^",126))

    def test_LS27(self):
         self.assertTrue(TestLexer.test(""" % erty == ! @ ksmdk ""","""%,erty,==,!,Error Token @""",127))
    
    def test_LS28(self):
         self.assertTrue(TestLexer.test("! == & != && * % $ ... ","!,==,Error Token &",128)) # today
    
    def test_LS29(self):
        self.assertTrue(TestLexer.test(""" 12+3>9-3x \"**asndabc+\\^ def\" ""","""12,+,3,>,9,-,3,x,Illegal Escape In String: "**asndabc+\^""",129))
    
    def test_LS30(self):
        self.assertTrue(TestLexer.test("""  \"\\!LScna\" ""","""Illegal Escape In String: "\!""",130))
    
    def test_LS31(self):
        self.assertTrue(TestLexer.test("!a%5&&b||c+*", "!,a,%,5,&&,b,||,c,+,*,<EOF>", 131))

    def test_LS32(self):
        self.assertTrue(TestLexer.test("a==b==01234!=43210<3>4", "a,==,b,==,01234,!=,43210,<,3,>,4,<EOF>", 132))

    def test_LS33(self):
        self.assertTrue(TestLexer.test("*and<=>mod<\\<=", "*,and,<=,>,mod,<,\\,<=,<EOF>", 133))

    def test_LS34(self):
        self.assertTrue(TestLexer.test("/*this is a cmt*/", "<EOF>", 134))

    def test_LS35(self):
        self.assertTrue(TestLexer.test("#hjhjhuhu/*youare live */", "<EOF>", 135))

    def test_LS36(self):
        self.assertTrue(TestLexer.test("#hello my friend \n asda", "asda,<EOF>", 136))

    def test_LS37(self):
        self.assertTrue(TestLexer.test("/*hello my friend \n nothinghjhj \n love */ ntp", "ntp,<EOF>", 137))

    def test_LS38(self):
        self.assertTrue(TestLexer.test("asf aso Dowoad ", "asf,aso,Dowoad,<EOF>", 138))

    def test_LS39(self):
        self.assertTrue(TestLexer.test("tuoitre chuwa trai su doi", "tuoitre,chuwa,trai,su,doi,<EOF>", 139))

    def test_LS40(self):
        self.assertTrue(TestLexer.test("imposter lol ", "imposter,lol,<EOF>", 140))

    def test_LS41(self):
        self.assertTrue(TestLexer.test("01 10 001 100", "01,10,001,100,<EOF>", 141))

    def test_LS42(self):
        self.assertTrue(TestLexer.test("01. 10.3e+9 0.3e5","01.,10.3e+9,0.3e5,<EOF>", 142))

    def test_LS43(self):
        self.assertTrue(TestLexer.test("5.e5 6. 5.e-8","5.e5,6.,5.e-8,<EOF>", 143))

    def test_LS44(self):
        self.assertTrue(TestLexer.test("anD then false", "anD,then,false,<EOF>", 144))

    def test_LS45(self):
        self.assertTrue(TestLexer.test("sTRIng False", "sTRIng,False,<EOF>", 145))

    def test_LS46(self):
        self.assertTrue(TestLexer.test(""" ",dls\\F12" """, """Illegal Escape In String: ",dls\\F""", 146))

    def test_LS147(self):
        input = "a88jdjij + a2x - 40 > 12"
        expect = "a88jdjij,+,a2x,-,40,>,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_LS148(self):
        input = "as<.>iooi"
        expect = "as,<,.,>,iooi,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_LS149(self):
        input = "[;]12kkkasijiasdijANXNMXMM\t"
        expect = "[,;,],12,kkkasijiasdijANXNMXMM,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_LS150(self):
        input = ":a:sxassa:,irejgioj0990hiju."
        expect = ":,a,:,sxassa,:,,,irejgioj0990hiju,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_LS151(self):
        input = "class a extends B {}"
        expect = "class,a,extends,B,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_LS152(self):
        input = "class ABC }"
        expect = "class,ABC,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test_LS153(self):
        input = "class ABC { }"
        expect = "class,ABC,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_LS154(self):
        input = "class ABC extends { }"
        expect = "class,ABC,extends,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_LS155(self):
        input = "class { }"
        expect = "class,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test_LS156(self):
        input = "int main(){}"
        expect = "int,main,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test_LS157(self):
        input = "a.x() this.x.a().a"
        expect = "a,.,x,(,),this,.,x,.,a,(,),.,a,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test_LS158(self):
        input = "static int getNumOfShape() {return numOfShape;}"
        expect = "static,int,getNumOfShape,(,),{,return,numOfShape,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))

    def test_LS159(self):
        input = """s := new A();
                    a.a().a := 12;
                    this.a := 12;
                    io.writeFloatLn(s.getArea());"""
        expect = "s,:=,new,A,(,),;,a,.,a,(,),.,a,:=,12,;,this,.,a,:=,12,;,io,.,writeFloatLn,(,s,.,getArea,(,),),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))

    def test_LS160(self):
        input = "ox128 + 1258.e8"
        expect = "ox128,+,1258.e8,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))

    def test_LS161(self):
        input = "a := true, b = false"
        expect = "a,:=,true,,,b,=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))

    def test_LS162(self):
        input = """ "abc\\e def" """
        expect = """Illegal Escape In String: "abc\\e"""
        self.assertTrue(TestLexer.test(input, expect, 162))
    
    def test_LS163(self):
        input = """ "ab'c\\n def" """
        expect = """"ab'c\\n def",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test_LS164(self):
        input = """~!^^^^!"""
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 164))

    def test_LS165(self):
        input = "!@^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 165))

    def test_LS166(self):
        input = """a= "He said: " Im Super'Man "s" testtt; __world = 5; imple = 8;"""
        expect = """a,=,"He said: ",Im,Super,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 166))

    def test_LS167(self):
        input = """a= "He said: " Hello " \n ";"""
        expect = """a,=,"He said: ",Hello,Unclosed String: " """
        self.assertTrue(TestLexer.test(input, expect, 167))

    def test_LS168(self):
        input = """a = "Hello \n world !";"""
        expect = """a,=,Unclosed String: "Hello """
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test_LS169(self):
        input = "{1,2,3}"
        expect = "{,1,,,2,,,3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test_LS170(self):
        input = "{2.3, 4.2, 102e3}"
        expect = "{,2.3,,,4.2,,,102e3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_LS171(self):
        input = "a[4] = {1, 2,  3, 4}"
        expect = "a,[,4,],=,{,1,,,2,,,3,,,4,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test_LS172(self):
        input = "==!=!&&||+-/"
        expect = "==,!=,!,&&,||,+,-,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test_LS173(self):
        input = "int[5] a;"
        expect = "int,[,5,],a,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test_LS174(self):
        input = "a[3 + x.foo(2)] := a[b[2]] + 3;"
        expect = "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test_LS175(self):
        input = "s:=r*r*this.myPI;"
        expect = "s,:=,r,*,r,*,this,.,myPI,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

    def test_LS176(self):
        input = "1/2"
        expect = "1,/,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

    def test_LS177(self):
        input = """ " \\h " """
        expect = """Illegal Escape In String: " \h"""
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test_LS178(self):
        input = """ " \\naaa\\t" """
        expect = """" \\naaa\\t",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test_LS179(self):
        input = "{}"
        expect = "{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))

    def test_LS180(self):
        input = """{"}"""
        expect = """{,Unclosed String: "}"""
        self.assertTrue(TestLexer.test(input, expect, 180))

    def test_LS181(self):
        input = "{False,}"
        expect = "{,False,,,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test_LS182(self):
        input = "#{\"}"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_LS183(self):
        input = "/* abcxyz #{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_LS184(self):
        input = "# this is a line comment /*"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))
    
    def test_LS185(self):
        input = "{/* this is a line comment */ 180, 20}"
        expect = "{,180,,,20,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test_LS186(self):
        input = """ "\\"aadadddldld\\"" """
        expect = """"\\"aadadddldld\\"",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 186))

    def test_LS187(self):
        input = """ "dshf"""
        expect = """Unclosed String: "dshf"""
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_LS188(self):
        input = """ {/*"*****/*"}*/*"""
        expect = """{,*,Unclosed String: "}*/*"""
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_LS189(self):
        input = """sb0345"-a)
                    " """
        expect = """sb0345,Unclosed String: "-a)"""
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_LS190(self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: "abc\\x"""
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_LS191(self):
        input = """ "\\t\\ " """
        expect = """Illegal Escape In String: "\\t\\ """
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_LS192(self):
        input = """ "        " """
        expect = """"        ",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_LS193(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_LS194(self):
        input = "Var"
        expect = "Var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_LS195(self):
        input = "ab?svn"
        expect = "ab,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_LS196(self):
        input = "Var x;"
        expect = "Var,x,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_LS197(self):
        input = """{         "1" ,      "2"     ,      "3"       }"""
        expect = """{,"1",,,"2",,,"3",},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))
    
    def test_LS198(self):
        input = "12.000e3"
        expect = "12.000e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))
    
    def test_LS199(self):
        input = "12.e-3"
        expect = "12.e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))
    
    def test_LS200(self):
        self.assertTrue(TestLexer.test(""" "abvc\bcd" """, """"abvc\bcd",<EOF>""", 200))
    