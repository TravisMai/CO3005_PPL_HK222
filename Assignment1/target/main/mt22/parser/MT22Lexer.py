# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01b5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\7\2\u0082\n\2")
        buf.write("\f\2\16\2\u0085\13\2\3\2\5\2\u0088\n\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\7\3\u0092\n\3\f\3\16\3\u0095\13\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u009e\n\4\f\4\16\4\u00a1")
        buf.write("\13\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\6\64\u015b")
        buf.write("\n\64\r\64\16\64\u015c\3\64\3\64\3\65\3\65\7\65\u0163")
        buf.write("\n\65\f\65\16\65\u0166\13\65\3\65\5\65\u0169\n\65\3\66")
        buf.write("\3\66\7\66\u016d\n\66\f\66\16\66\u0170\13\66\3\66\5\66")
        buf.write("\u0173\n\66\3\66\3\66\5\66\u0177\n\66\3\66\5\66\u017a")
        buf.write("\n\66\3\67\3\67\5\67\u017e\n\67\3\67\3\67\38\38\68\u0184")
        buf.write("\n8\r8\168\u0185\39\39\39\3:\3:\7:\u018d\n:\f:\16:\u0190")
        buf.write("\13:\3;\3;\5;\u0194\n;\3;\6;\u0197\n;\r;\16;\u0198\3<")
        buf.write("\3<\7<\u019d\n<\f<\16<\u01a0\13<\3<\5<\u01a3\n<\3<\3<")
        buf.write("\3=\3=\7=\u01a9\n=\f=\16=\u01ac\13=\3=\3=\3=\3=\3=\3>")
        buf.write("\3>\3>\3\u0093\2?\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o\2q\2s\2u\2w9y:{;\3\2\16\4\2\f\f\17\17\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\6\2\13\f\17\17\"\"aa\3\2\63;\4")
        buf.write("\2\62;aa\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\t\2$$^^ddhhppttvv\2\u01c4\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\3}\3\2\2\2\5\u008d\3\2\2\2\7\u009b\3\2\2\2\t")
        buf.write("\u00a2\3\2\2\2\13\u00a7\3\2\2\2\r\u00ad\3\2\2\2\17\u00b5")
        buf.write("\3\2\2\2\21\u00b8\3\2\2\2\23\u00bd\3\2\2\2\25\u00c3\3")
        buf.write("\2\2\2\27\u00c9\3\2\2\2\31\u00cd\3\2\2\2\33\u00d6\3\2")
        buf.write("\2\2\35\u00d9\3\2\2\2\37\u00e2\3\2\2\2!\u00e9\3\2\2\2")
        buf.write("#\u00f0\3\2\2\2%\u00f5\3\2\2\2\'\u00fb\3\2\2\2)\u0100")
        buf.write("\3\2\2\2+\u0104\3\2\2\2-\u010d\3\2\2\2/\u0110\3\2\2\2")
        buf.write("\61\u0118\3\2\2\2\63\u011e\3\2\2\2\65\u0120\3\2\2\2\67")
        buf.write("\u0122\3\2\2\29\u0124\3\2\2\2;\u0126\3\2\2\2=\u0128\3")
        buf.write("\2\2\2?\u012a\3\2\2\2A\u012d\3\2\2\2C\u0130\3\2\2\2E\u0133")
        buf.write("\3\2\2\2G\u0136\3\2\2\2I\u0138\3\2\2\2K\u013b\3\2\2\2")
        buf.write("M\u013d\3\2\2\2O\u0140\3\2\2\2Q\u0143\3\2\2\2S\u0145\3")
        buf.write("\2\2\2U\u0147\3\2\2\2W\u0149\3\2\2\2Y\u014b\3\2\2\2[\u014d")
        buf.write("\3\2\2\2]\u014f\3\2\2\2_\u0151\3\2\2\2a\u0153\3\2\2\2")
        buf.write("c\u0155\3\2\2\2e\u0157\3\2\2\2g\u015a\3\2\2\2i\u0168\3")
        buf.write("\2\2\2k\u0172\3\2\2\2m\u017b\3\2\2\2o\u0183\3\2\2\2q\u0187")
        buf.write("\3\2\2\2s\u018a\3\2\2\2u\u0191\3\2\2\2w\u019a\3\2\2\2")
        buf.write("y\u01a6\3\2\2\2{\u01b2\3\2\2\2}~\7\61\2\2~\177\7\61\2")
        buf.write("\2\177\u0083\3\2\2\2\u0080\u0082\n\2\2\2\u0081\u0080\3")
        buf.write("\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0086")
        buf.write("\u0088\7\17\2\2\u0087\u0086\3\2\2\2\u0087\u0088\3\2\2")
        buf.write("\2\u0088\u0089\3\2\2\2\u0089\u008a\7\f\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u008c\b\2\2\2\u008c\4\3\2\2\2\u008d\u008e")
        buf.write("\7\61\2\2\u008e\u008f\7,\2\2\u008f\u0093\3\2\2\2\u0090")
        buf.write("\u0092\13\2\2\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2")
        buf.write("\2\u0093\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0096")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\7,\2\2\u0097")
        buf.write("\u0098\7\61\2\2\u0098\u0099\3\2\2\2\u0099\u009a\b\3\2")
        buf.write("\2\u009a\6\3\2\2\2\u009b\u009f\t\3\2\2\u009c\u009e\t\4")
        buf.write("\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\b\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\u00a6\7q\2\2\u00a6\n\3\2\2\2\u00a7\u00a8")
        buf.write("\7d\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7c\2\2\u00ab\u00ac\7m\2\2\u00ac\f\3\2\2\2\u00ad\u00ae")
        buf.write("\7d\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1")
        buf.write("\7n\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\16\3\2\2\2\u00b5\u00b6\7f\2\2\u00b6\u00b7")
        buf.write("\7q\2\2\u00b7\20\3\2\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba")
        buf.write("\7n\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7g\2\2\u00bc\22")
        buf.write("\3\2\2\2\u00bd\u00be\7h\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0")
        buf.write("\7n\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7g\2\2\u00c2\24")
        buf.write("\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6")
        buf.write("\7q\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7v\2\2\u00c8\26")
        buf.write("\3\2\2\2\u00c9\u00ca\7h\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00cc\30\3\2\2\2\u00cd\u00ce\7h\2\2\u00ce\u00cf")
        buf.write("\7w\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7e\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\32\3\2\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7h\2\2\u00d8\34\3\2\2\2\u00d9\u00da\7k\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7i\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\36\3\2\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7\u00e8\7p\2\2\u00e8 \3\2\2\2\u00e9\u00ea")
        buf.write("\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7i\2\2\u00ef\"")
        buf.write("\3\2\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7w\2\2\u00f3\u00f4\7g\2\2\u00f4$\3\2\2\2\u00f5\u00f6")
        buf.write("\7y\2\2\u00f6\u00f7\7j\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7g\2\2\u00fa&\3\2\2\2\u00fb\u00fc")
        buf.write("\7x\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff")
        buf.write("\7f\2\2\u00ff(\3\2\2\2\u0100\u0101\7q\2\2\u0101\u0102")
        buf.write("\7w\2\2\u0102\u0103\7v\2\2\u0103*\3\2\2\2\u0104\u0105")
        buf.write("\7e\2\2\u0105\u0106\7q\2\2\u0106\u0107\7p\2\2\u0107\u0108")
        buf.write("\7v\2\2\u0108\u0109\7k\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7w\2\2\u010b\u010c\7g\2\2\u010c,\3\2\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u010f\7h\2\2\u010f.\3\2\2\2\u0110\u0111")
        buf.write("\7k\2\2\u0111\u0112\7p\2\2\u0112\u0113\7j\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\u0115\7t\2\2\u0115\u0116\7k\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117\60\3\2\2\2\u0118\u0119\7c\2\2\u0119\u011a")
        buf.write("\7t\2\2\u011a\u011b\7t\2\2\u011b\u011c\7c\2\2\u011c\u011d")
        buf.write("\7{\2\2\u011d\62\3\2\2\2\u011e\u011f\7-\2\2\u011f\64\3")
        buf.write("\2\2\2\u0120\u0121\7/\2\2\u0121\66\3\2\2\2\u0122\u0123")
        buf.write("\7,\2\2\u01238\3\2\2\2\u0124\u0125\7\61\2\2\u0125:\3\2")
        buf.write("\2\2\u0126\u0127\7\'\2\2\u0127<\3\2\2\2\u0128\u0129\7")
        buf.write("#\2\2\u0129>\3\2\2\2\u012a\u012b\7(\2\2\u012b\u012c\7")
        buf.write("(\2\2\u012c@\3\2\2\2\u012d\u012e\7~\2\2\u012e\u012f\7")
        buf.write("~\2\2\u012fB\3\2\2\2\u0130\u0131\7?\2\2\u0131\u0132\7")
        buf.write("?\2\2\u0132D\3\2\2\2\u0133\u0134\7#\2\2\u0134\u0135\7")
        buf.write("?\2\2\u0135F\3\2\2\2\u0136\u0137\7>\2\2\u0137H\3\2\2\2")
        buf.write("\u0138\u0139\7>\2\2\u0139\u013a\7?\2\2\u013aJ\3\2\2\2")
        buf.write("\u013b\u013c\7@\2\2\u013cL\3\2\2\2\u013d\u013e\7@\2\2")
        buf.write("\u013e\u013f\7?\2\2\u013fN\3\2\2\2\u0140\u0141\7<\2\2")
        buf.write("\u0141\u0142\7<\2\2\u0142P\3\2\2\2\u0143\u0144\7*\2\2")
        buf.write("\u0144R\3\2\2\2\u0145\u0146\7+\2\2\u0146T\3\2\2\2\u0147")
        buf.write("\u0148\7]\2\2\u0148V\3\2\2\2\u0149\u014a\7_\2\2\u014a")
        buf.write("X\3\2\2\2\u014b\u014c\7\60\2\2\u014cZ\3\2\2\2\u014d\u014e")
        buf.write("\7.\2\2\u014e\\\3\2\2\2\u014f\u0150\7=\2\2\u0150^\3\2")
        buf.write("\2\2\u0151\u0152\7<\2\2\u0152`\3\2\2\2\u0153\u0154\7}")
        buf.write("\2\2\u0154b\3\2\2\2\u0155\u0156\7\177\2\2\u0156d\3\2\2")
        buf.write("\2\u0157\u0158\7?\2\2\u0158f\3\2\2\2\u0159\u015b\t\5\2")
        buf.write("\2\u015a\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\b\64\2\2\u015fh\3\2\2\2\u0160\u0164\t\6\2\2\u0161")
        buf.write("\u0163\t\7\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0169\3")
        buf.write("\2\2\2\u0166\u0164\3\2\2\2\u0167\u0169\7\62\2\2\u0168")
        buf.write("\u0160\3\2\2\2\u0168\u0167\3\2\2\2\u0169j\3\2\2\2\u016a")
        buf.write("\u016e\t\6\2\2\u016b\u016d\t\7\2\2\u016c\u016b\3\2\2\2")
        buf.write("\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3")
        buf.write("\2\2\2\u016f\u0173\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173")
        buf.write("\7\62\2\2\u0172\u016a\3\2\2\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0179\3\2\2\2\u0174\u017a\5s:\2\u0175\u0177\5s:\2\u0176")
        buf.write("\u0175\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u017a\5u;\2\u0179\u0174\3\2\2\2\u0179\u0176\3\2")
        buf.write("\2\2\u017al\3\2\2\2\u017b\u017d\7$\2\2\u017c\u017e\5o")
        buf.write("8\2\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017f\u0180\7$\2\2\u0180n\3\2\2\2\u0181\u0184")
        buf.write("\n\b\2\2\u0182\u0184\5q9\2\u0183\u0181\3\2\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186p\3\2\2\2\u0187\u0188\7^\2\2\u0188")
        buf.write("\u0189\t\t\2\2\u0189r\3\2\2\2\u018a\u018e\7\60\2\2\u018b")
        buf.write("\u018d\t\n\2\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018ft\3\2\2")
        buf.write("\2\u0190\u018e\3\2\2\2\u0191\u0193\t\13\2\2\u0192\u0194")
        buf.write("\t\f\2\2\u0193\u0192\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0196\3\2\2\2\u0195\u0197\t\n\2\2\u0196\u0195\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3")
        buf.write("\2\2\2\u0199v\3\2\2\2\u019a\u019e\7$\2\2\u019b\u019d\5")
        buf.write("o8\2\u019c\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a1\u01a3\7\2\2\3\u01a2\u01a1\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\b")
        buf.write("<\3\2\u01a5x\3\2\2\2\u01a6\u01aa\7$\2\2\u01a7\u01a9\5")
        buf.write("o8\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ad\u01ae\7^\2\2\u01ae\u01af\n\r\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u01b1\b=\4\2\u01b1z\3\2\2\2")
        buf.write("\u01b2\u01b3\13\2\2\2\u01b3\u01b4\b>\5\2\u01b4|\3\2\2")
        buf.write("\2\27\2\u0083\u0087\u0093\u009f\u015c\u0164\u0168\u016e")
        buf.write("\u0172\u0176\u0179\u017d\u0183\u0185\u018e\u0193\u0198")
        buf.write("\u019e\u01a2\u01aa\6\b\2\2\3<\2\3=\3\3>\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_CMT = 1
    BLOCK_CMT = 2
    ID = 3
    AUTO = 4
    BREAK = 5
    BOOLEAN = 6
    DO = 7
    ELSE = 8
    FALSE = 9
    FLOAT = 10
    FOR = 11
    FUNCTION = 12
    IF = 13
    INTERGER = 14
    RETURN = 15
    STRING = 16
    TRUE = 17
    WHILE = 18
    VOID = 19
    OUT = 20
    CONTINUE = 21
    OF = 22
    INHERIT = 23
    ARRAY = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    MOD = 29
    NOT = 30
    AND = 31
    OR = 32
    EQUAL = 33
    NEQUAL = 34
    LT = 35
    LTE = 36
    GT = 37
    GTE = 38
    CONCAT = 39
    LB = 40
    RB = 41
    LSB = 42
    RSB = 43
    DOT = 44
    COMMA = 45
    SM = 46
    COLON = 47
    LP = 48
    RP = 49
    ASS = 50
    WS = 51
    INTERGERLIT = 52
    FLOATLIT = 53
    STRINGLIT = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'interger'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "LINE_CMT", "BLOCK_CMT", "ID", "AUTO", "BREAK", "BOOLEAN", "DO", 
            "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTERGER", 
            "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", 
            "CONCAT", "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SM", "COLON", 
            "LP", "RP", "ASS", "WS", "INTERGERLIT", "FLOATLIT", "STRINGLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LINE_CMT", "BLOCK_CMT", "ID", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTERGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NEQUAL", 
                  "LT", "LTE", "GT", "GTE", "CONCAT", "LB", "RB", "LSB", 
                  "RSB", "DOT", "COMMA", "SM", "COLON", "LP", "RP", "ASS", 
                  "WS", "INTERGERLIT", "FLOATLIT", "STRINGLIT", "StrCha", 
                  "Esc", "Deci", "Expo", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	y = str(self.text)
            	raise UncloseString(y[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	y = str(self.text)
            	raise IllegalEscape(y[0:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise ErrorToken(self.text)

     


