# Generated from c:\Users\EmChes\OneDrive - wtpvf\Documents\GitHub\CO3005_PPL_HK222\Assignement1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01c6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\7\61\u013a\n\61\f\61\16\61\u013d\13\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\7\62\u0145\n\62\f\62\16\62")
        buf.write("\u0148\13\62\3\62\3\62\3\62\3\62\3\62\3\63\6\63\u0150")
        buf.write("\n\63\r\63\16\63\u0151\3\63\3\63\3\64\3\64\3\64\7\64\u0159")
        buf.write("\n\64\f\64\16\64\u015c\13\64\3\64\3\64\3\64\7\64\u0161")
        buf.write("\n\64\f\64\16\64\u0164\13\64\5\64\u0166\n\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\5\65\u016d\n\65\3\65\5\65\u0170\n\65\3")
        buf.write("\65\3\65\3\65\5\65\u0175\n\65\3\65\3\65\3\66\3\66\5\66")
        buf.write("\u017b\n\66\3\66\3\66\3\66\3\66\3\67\3\67\6\67\u0183\n")
        buf.write("\67\r\67\16\67\u0184\38\38\38\39\39\79\u018c\n9\f9\16")
        buf.write("9\u018f\139\3:\3:\5:\u0193\n:\3:\6:\u0196\n:\r:\16:\u0197")
        buf.write("\3;\3;\7;\u019c\n;\f;\16;\u019f\13;\3<\3<\7<\u01a3\n<")
        buf.write("\f<\16<\u01a6\13<\3<\5<\u01a9\n<\3<\3<\3=\3=\7=\u01af")
        buf.write("\n=\f=\16=\u01b2\13=\3=\3=\3=\3=\3=\3>\3>\3>\3?\3?\3?")
        buf.write("\3?\7?\u01c0\n?\f?\16?\u01c3\13?\3?\3?\4\u0146\u01c1\2")
        buf.write("@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2")
        buf.write("s\2u8w9y:{;}<\3\2\f\4\2\f\f\17\17\5\2\13\f\17\17\"\"\3")
        buf.write("\2\63;\3\2\62;\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\4")
        buf.write("\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\2\u01d6\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2\5\u0084\3\2\2")
        buf.write("\2\7\u008a\3\2\2\2\t\u0092\3\2\2\2\13\u0095\3\2\2\2\r")
        buf.write("\u009a\3\2\2\2\17\u00a0\3\2\2\2\21\u00a6\3\2\2\2\23\u00aa")
        buf.write("\3\2\2\2\25\u00b3\3\2\2\2\27\u00b6\3\2\2\2\31\u00be\3")
        buf.write("\2\2\2\33\u00c5\3\2\2\2\35\u00cc\3\2\2\2\37\u00d1\3\2")
        buf.write("\2\2!\u00d7\3\2\2\2#\u00dc\3\2\2\2%\u00e0\3\2\2\2\'\u00e9")
        buf.write("\3\2\2\2)\u00ec\3\2\2\2+\u00f4\3\2\2\2-\u00fa\3\2\2\2")
        buf.write("/\u00fc\3\2\2\2\61\u00fe\3\2\2\2\63\u0100\3\2\2\2\65\u0102")
        buf.write("\3\2\2\2\67\u0104\3\2\2\29\u0106\3\2\2\2;\u0109\3\2\2")
        buf.write("\2=\u010c\3\2\2\2?\u010f\3\2\2\2A\u0112\3\2\2\2C\u0114")
        buf.write("\3\2\2\2E\u0117\3\2\2\2G\u0119\3\2\2\2I\u011c\3\2\2\2")
        buf.write("K\u011f\3\2\2\2M\u0121\3\2\2\2O\u0123\3\2\2\2Q\u0125\3")
        buf.write("\2\2\2S\u0127\3\2\2\2U\u0129\3\2\2\2W\u012b\3\2\2\2Y\u012d")
        buf.write("\3\2\2\2[\u012f\3\2\2\2]\u0131\3\2\2\2_\u0133\3\2\2\2")
        buf.write("a\u0135\3\2\2\2c\u0140\3\2\2\2e\u014f\3\2\2\2g\u0165\3")
        buf.write("\2\2\2i\u0174\3\2\2\2k\u0178\3\2\2\2m\u0182\3\2\2\2o\u0186")
        buf.write("\3\2\2\2q\u0189\3\2\2\2s\u0190\3\2\2\2u\u0199\3\2\2\2")
        buf.write("w\u01a0\3\2\2\2y\u01ac\3\2\2\2{\u01b8\3\2\2\2}\u01bb\3")
        buf.write("\2\2\2\177\u0080\7c\2\2\u0080\u0081\7w\2\2\u0081\u0082")
        buf.write("\7v\2\2\u0082\u0083\7q\2\2\u0083\4\3\2\2\2\u0084\u0085")
        buf.write("\7d\2\2\u0085\u0086\7t\2\2\u0086\u0087\7g\2\2\u0087\u0088")
        buf.write("\7c\2\2\u0088\u0089\7m\2\2\u0089\6\3\2\2\2\u008a\u008b")
        buf.write("\7d\2\2\u008b\u008c\7q\2\2\u008c\u008d\7q\2\2\u008d\u008e")
        buf.write("\7n\2\2\u008e\u008f\7g\2\2\u008f\u0090\7c\2\2\u0090\u0091")
        buf.write("\7p\2\2\u0091\b\3\2\2\2\u0092\u0093\7f\2\2\u0093\u0094")
        buf.write("\7q\2\2\u0094\n\3\2\2\2\u0095\u0096\7g\2\2\u0096\u0097")
        buf.write("\7n\2\2\u0097\u0098\7u\2\2\u0098\u0099\7g\2\2\u0099\f")
        buf.write("\3\2\2\2\u009a\u009b\7h\2\2\u009b\u009c\7c\2\2\u009c\u009d")
        buf.write("\7n\2\2\u009d\u009e\7u\2\2\u009e\u009f\7g\2\2\u009f\16")
        buf.write("\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3")
        buf.write("\7q\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5\7v\2\2\u00a5\20")
        buf.write("\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9")
        buf.write("\7t\2\2\u00a9\22\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac")
        buf.write("\7w\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\24\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7h\2\2\u00b5\26\3\2\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8")
        buf.write("\7p\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7i\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7t\2\2\u00bd\30")
        buf.write("\3\2\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\32\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7i\2\2\u00cb\34\3\2\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\36\3\2\2\2\u00d1\u00d2\7y\2\2\u00d2\u00d3")
        buf.write("\7j\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6 \3\2\2\2\u00d7\u00d8\7x\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7f\2\2\u00db\"")
        buf.write("\3\2\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7w\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df$\3\2\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5")
        buf.write("\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8&\3\2\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb")
        buf.write("\7h\2\2\u00eb(\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7j\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7v\2\2\u00f3*\3")
        buf.write("\2\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7{\2\2\u00f9,\3")
        buf.write("\2\2\2\u00fa\u00fb\7-\2\2\u00fb.\3\2\2\2\u00fc\u00fd\7")
        buf.write("/\2\2\u00fd\60\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff\62\3\2")
        buf.write("\2\2\u0100\u0101\7\61\2\2\u0101\64\3\2\2\2\u0102\u0103")
        buf.write("\7\'\2\2\u0103\66\3\2\2\2\u0104\u0105\7#\2\2\u01058\3")
        buf.write("\2\2\2\u0106\u0107\7(\2\2\u0107\u0108\7(\2\2\u0108:\3")
        buf.write("\2\2\2\u0109\u010a\7~\2\2\u010a\u010b\7~\2\2\u010b<\3")
        buf.write("\2\2\2\u010c\u010d\7?\2\2\u010d\u010e\7?\2\2\u010e>\3")
        buf.write("\2\2\2\u010f\u0110\7#\2\2\u0110\u0111\7?\2\2\u0111@\3")
        buf.write("\2\2\2\u0112\u0113\7>\2\2\u0113B\3\2\2\2\u0114\u0115\7")
        buf.write(">\2\2\u0115\u0116\7?\2\2\u0116D\3\2\2\2\u0117\u0118\7")
        buf.write("@\2\2\u0118F\3\2\2\2\u0119\u011a\7@\2\2\u011a\u011b\7")
        buf.write("?\2\2\u011bH\3\2\2\2\u011c\u011d\7<\2\2\u011d\u011e\7")
        buf.write("<\2\2\u011eJ\3\2\2\2\u011f\u0120\7*\2\2\u0120L\3\2\2\2")
        buf.write("\u0121\u0122\7+\2\2\u0122N\3\2\2\2\u0123\u0124\7]\2\2")
        buf.write("\u0124P\3\2\2\2\u0125\u0126\7_\2\2\u0126R\3\2\2\2\u0127")
        buf.write("\u0128\7\60\2\2\u0128T\3\2\2\2\u0129\u012a\7.\2\2\u012a")
        buf.write("V\3\2\2\2\u012b\u012c\7=\2\2\u012cX\3\2\2\2\u012d\u012e")
        buf.write("\7<\2\2\u012eZ\3\2\2\2\u012f\u0130\7}\2\2\u0130\\\3\2")
        buf.write("\2\2\u0131\u0132\7\177\2\2\u0132^\3\2\2\2\u0133\u0134")
        buf.write("\7?\2\2\u0134`\3\2\2\2\u0135\u0136\7\61\2\2\u0136\u0137")
        buf.write("\7\61\2\2\u0137\u013b\3\2\2\2\u0138\u013a\n\2\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u013f\b\61\2\2\u013fb\3\2\2\2\u0140\u0141")
        buf.write("\7\61\2\2\u0141\u0142\7,\2\2\u0142\u0146\3\2\2\2\u0143")
        buf.write("\u0145\13\2\2\2\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2")
        buf.write("\2\u0146\u0147\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0149")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\7,\2\2\u014a")
        buf.write("\u014b\7\61\2\2\u014b\u014c\3\2\2\2\u014c\u014d\b\62\2")
        buf.write("\2\u014dd\3\2\2\2\u014e\u0150\t\3\2\2\u014f\u014e\3\2")
        buf.write("\2\2\u0150\u0151\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\b\63\2\2\u0154")
        buf.write("f\3\2\2\2\u0155\u0166\7\62\2\2\u0156\u015a\t\4\2\2\u0157")
        buf.write("\u0159\t\5\2\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0162\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7a\2\2\u015e\u0161")
        buf.write("\t\5\2\2\u015f\u0161\t\5\2\2\u0160\u015d\3\2\2\2\u0160")
        buf.write("\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0165\u0155\3\2\2\2\u0165\u0156\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u0168\b\64\3\2\u0168h\3\2\2\2\u0169\u016f")
        buf.write("\5g\64\2\u016a\u0170\5q9\2\u016b\u016d\5q9\2\u016c\u016b")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u0170\5s:\2\u016f\u016a\3\2\2\2\u016f\u016c\3\2\2\2\u0170")
        buf.write("\u0175\3\2\2\2\u0171\u0172\5q9\2\u0172\u0173\5s:\2\u0173")
        buf.write("\u0175\3\2\2\2\u0174\u0169\3\2\2\2\u0174\u0171\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176\u0177\b\65\4\2\u0177j\3\2\2")
        buf.write("\2\u0178\u017a\7$\2\2\u0179\u017b\5m\67\2\u017a\u0179")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017d\7$\2\2\u017d\u017e\3\2\2\2\u017e\u017f\b\66\5\2")
        buf.write("\u017fl\3\2\2\2\u0180\u0183\n\6\2\2\u0181\u0183\5o8\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185n")
        buf.write("\3\2\2\2\u0186\u0187\7^\2\2\u0187\u0188\t\7\2\2\u0188")
        buf.write("p\3\2\2\2\u0189\u018d\7\60\2\2\u018a\u018c\t\5\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018er\3\2\2\2\u018f\u018d\3\2\2")
        buf.write("\2\u0190\u0192\t\b\2\2\u0191\u0193\t\t\2\2\u0192\u0191")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194")
        buf.write("\u0196\t\5\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198t\3\2\2")
        buf.write("\2\u0199\u019d\t\n\2\2\u019a\u019c\t\13\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019ev\3\2\2\2\u019f\u019d\3\2\2\2\u01a0")
        buf.write("\u01a4\7$\2\2\u01a1\u01a3\5m\67\2\u01a2\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3")
        buf.write("\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a9")
        buf.write("\7\2\2\3\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ab\b<\6\2\u01abx\3\2\2\2\u01ac")
        buf.write("\u01b0\7$\2\2\u01ad\u01af\5m\67\2\u01ae\u01ad\3\2\2\2")
        buf.write("\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3")
        buf.write("\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4")
        buf.write("\7^\2\2\u01b4\u01b5\n\7\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b7\b=\7\2\u01b7z\3\2\2\2\u01b8\u01b9\13\2\2\2\u01b9")
        buf.write("\u01ba\b>\b\2\u01ba|\3\2\2\2\u01bb\u01bc\7\61\2\2\u01bc")
        buf.write("\u01bd\7,\2\2\u01bd\u01c1\3\2\2\2\u01be\u01c0\13\2\2\2")
        buf.write("\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01c2\3")
        buf.write("\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c4\u01c5\b?\t\2\u01c5~\3\2\2\2\30\2\u013b")
        buf.write("\u0146\u0151\u015a\u0160\u0162\u0165\u016c\u016f\u0174")
        buf.write("\u017a\u0182\u0184\u018d\u0192\u0197\u019d\u01a4\u01a8")
        buf.write("\u01b0\u01c1\n\b\2\2\3\64\2\3\65\3\3\66\4\3<\5\3=\6\3")
        buf.write(">\7\3?\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQUAL = 30
    NEQUAL = 31
    LT = 32
    LTE = 33
    GT = 34
    GTE = 35
    CONCAT = 36
    LB = 37
    RB = 38
    LSB = 39
    RSB = 40
    DOT = 41
    COMMA = 42
    SM = 43
    COLON = 44
    LCB = 45
    RCB = 46
    ASS = 47
    LINE_CMT = 48
    BLOCK_CMT = 49
    WS = 50
    INTEGERLIT = 51
    FLOATLIT = 52
    STRINGLIT = 53
    ID = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57
    UNTERMINATED_COMMENT = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "NEQUAL", "LT", "LTE", "GT", "GTE", "CONCAT", "LB", "RB", "LSB", 
            "RSB", "DOT", "COMMA", "SM", "COLON", "LCB", "RCB", "ASS", "LINE_CMT", 
            "BLOCK_CMT", "WS", "INTEGERLIT", "FLOATLIT", "STRINGLIT", "ID", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", "CONCAT", 
                  "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SM", "COLON", 
                  "LCB", "RCB", "ASS", "LINE_CMT", "BLOCK_CMT", "WS", "INTEGERLIT", 
                  "FLOATLIT", "STRINGLIT", "StrCha", "Esc", "Deci", "Expo", 
                  "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", 
                  "UNTERMINATED_COMMENT" ]

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
            actions[50] = self.INTEGERLIT_action 
            actions[51] = self.FLOATLIT_action 
            actions[52] = self.STRINGLIT_action 
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[61] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGERLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	y = str(self.text)
            	raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	y = str(self.text)
            	raise IllegalEscape(y[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise ErrorToken(self.text)

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	y = str(self.text)
            	raise UnterminatedComment(y[0:])

     


