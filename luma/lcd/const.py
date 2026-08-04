# -*- coding: utf-8 -*-
# Copyright (c) 2013-20 Richard Hull and contributors
# See LICENSE.rst for details.


class st7567(object):
    DISPLAYON = 0xAF
    DISPLAYOFF = 0xAE


class st7565(object):
    DISPLAYON = 0xAF
    DISPLAYOFF = 0xAE


class pcd8544(object):
    DISPLAYON = 0x0C
    DISPLAYOFF = 0x08


class st7735(object):
    DISPLAYON = 0x29
    DISPLAYOFF = 0x28


class ili9341(object):
    DISPLAYON = 0x29
    DISPLAYOFF = 0x28


class ili9486(object):
    DISPLAYON = 0x29
    DISPLAYOFF = 0x28


class ili9488(object):
    DISPLAYON = 0x29
    DISPLAYOFF = 0x28


class ht1621(object):
    DISPLAYON = 0x06
    DISPLAYOFF = 0x04


class uc1701x(object):
    DISPLAYON = 0xAF
    DISPLAYOFF = 0xAE


class st7789(object):
    DISPLAYON = 0x29
    DISPLAYOFF = 0x28


class hd44780(object):
    """
    Values to be used by the hd44780 class during initialization of the display.
    Contains FONTDATA to enable the hd44780 class to embed the same fonts that
    are contained within any display that uses a hd44780 style controller

    .. versionadded:: 2.5.0
    """
    CLEAR = 0x01
    HOME = 0x02
    ENTRY = 0x06
    DISPLAYOFF = 0x08
    DISPLAYON = 0x0C
    FUNCTIONSET = 0x20
    DL8 = 0x10
    DL4 = 0x00
    LINES2 = 0x08
    LINES1 = 0x00
    CHAR5x8 = 0x00
    CHAR5x10 = 0x04
    DL8 = 0x10
    DL4 = 0x00
    DDRAMADDR = 0x80
    CGRAMADDR = 0x40
    LINES = [00, 0x40, 0x14, 0x54]
    CUSTOMCHARS = 8
    FONTDATA = {
        'metrics': [
            # A00 ENGLISH_JAPANESE 5x8 METRICS
            {
                'name': 'A00',
                'index': range(16, 256),
                'xwidth': 5,
                'cell_size': (5, 10),
                'glyph_size': (5, 8),
                'table_size': (800, 20)
            },
            # A02 ENGLISH_EUROPEAN 5x8 METRICS
            {
                'name': 'A02',
                'index': range(16, 256),
                'xwidth': 5,
                'cell_size': (5, 10),
                'glyph_size': (5, 8),
                'table_size': (800, 20)
            },
            # AiP31068L-002 EUROPEAN_RUSSIAN 5x8 METRICS
            {
                'name': 'AiP-002',
                'index': range(16, 256),
                'xwidth': 5,
                'cell_size': (5, 10),
                'glyph_size': (5, 8),
                'table_size': (800, 20)
            },
            # AiP31068L-003 WESTERN EUROPEAN 5x8 METRICS
            {
                'name': 'AiP-003',
                'index': range(16, 256),
                'xwidth': 5,
                'cell_size': (5, 10),
                'glyph_size': (5, 8),
                'table_size': (800, 20)
            },
            # 901 FRENCH, POLISH AND SILESIAN ACCENTED CHARACTERS 5x8 METRICS
            {
                'name': '901',
                'index': range(160, 192),
                'xwidth': 5,
                'cell_size': (5, 10),
                'glyph_size': (5, 8),
                'table_size': (80, 20)
            }
        ],
        # TODO: Complete (and verify) FONT Mappings (Issue #112)
        'mappings': [
            {   # A00 ENGLISH_JAPANESE CHARACTER FONT
                # Missing maps for
                # a1, e2, e5, e6, e7, e9, ea, f0, f1, f4, f5, f8, f9, fa, fb, fc
                0x0410:   0x41,  # А CYRILLIC CAPITAL LETTER A
                0x0412:   0x42,  # В CYRILLIC CAPITAL LETTER VE
                0x0421:   0x43,  # С CYRILLIC CAPITAL LETTER ES
                0x0415:   0x45,  # Е CYRILLIC CAPITAL LETTER IE
                0x041d:   0x48,  # Н CYRILLIC CAPITAL LETTER EN
                0x041a:   0x4b,  # К CYRILLIC CAPITAL LETTER KA
                0x041c:   0x4d,  # М CYRILLIC CAPITAL LETTER EM
                0x041e:   0x4f,  # О CYRILLIC CAPITAL LETTER O
                0x0420:   0x50,  # Р CYRILLIC CAPITAL LETTER ER
                0x0422:   0x54,  # Т CYRILLIC CAPITAL LETTER TE
                0x0425:   0x58,  # Х CYRILLIC CAPITAL LETTER HA
                0x00a5:   0x5c,  # ¥ YEN SIGN
                0x042c:   0x62,  # Ь CYRILLIC CAPITAL LETTER SOFT SIGN
                0x2192:   0x7e,  # → RIGHTWARDS ARROW
                0x2190:   0x7f,  # ← LEFTWARDS ARROW
                0x300c:   0xa2,  # 「 LEFT CORNER BRACKET
                0x300d:   0xa3,  # 」 RIGHT CORNER BRACKET
                0x30fd:   0xa4,  # ヽ KATAKANA ITERATION MARK
                0x30fb:   0xa5,  # ・ KATAKANA MIDDLE DOT
                0x30f2:   0xa6,  # ヲ KATAKANA LETTER WO
                0x30a1:   0xa7,  # ァ KATAKANA LETTER SMALL A
                0x30a3:   0xa8,  # ィ KATAKANA LETTER SMALL I
                0x30a5:   0xa9,  # ゥ KATAKANA LETTER SMALL U
                0x30a7:   0xaa,  # ェ KATAKANA LETTER SMALL E
                0x30a9:   0xab,  # ォ KATAKANA LETTER SMALL O
                0x30e3:   0xac,  # ャ KATAKANA LETTER SMALL YA
                0x30e5:   0xad,  # ュ KATAKANA LETTER SMALL YU
                0x30e7:   0xae,  # ョ KATAKANA LETTER SMALL YO
                0x30c3:   0xaf,  # ッ KATAKANA LETTER SMALL TU
                0x30fc:   0xb0,  # ー KATAKANA-HIRAGANA PROLONGED SOUND MARK
                0x30a2:   0xb1,  # ア KATAKANA LETTER A
                0x30a4:   0xb2,  # イ KATAKANA LETTER I
                0x30a6:   0xb3,  # ウ KATAKANA LETTER U
                0x30a8:   0xb4,  # エ KATAKANA LETTER E
                0x30aa:   0xb5,  # オ KATAKANA LETTER O
                0x30ab:   0xb6,  # カ KATAKANA LETTER KA
                0x30ad:   0xb7,  # キ KATAKANA LETTER KI
                0x30af:   0xb8,  # ク KATAKANA LETTER KU
                0x30b1:   0xb9,  # ケ KATAKANA LETTER KE
                0x30b3:   0xba,  # コ KATAKANA LETTER KO
                0x30b5:   0xbb,  # サ KATAKANA LETTER SA
                0x30b7:   0xbc,  # シ KATAKANA LETTER SI
                0x30b9:   0xbd,  # ス KATAKANA LETTER SU
                0x30bb:   0xbe,  # セ KATAKANA LETTER SE
                0x30bd:   0xbf,  # ソ KATAKANA LETTER SO
                0x30bf:   0xc0,  # タ KATAKANA LETTER TA
                0x30c1:   0xc1,  # チ KATAKANA LETTER TI
                0x30c4:   0xc2,  # ツ KATAKANA LETTER TU
                0x30c6:   0xc3,  # テ KATAKANA LETTER TE
                0x30c8:   0xc4,  # ト KATAKANA LETTER TO
                0x30ca:   0xc5,  # ナ KATAKANA LETTER NA
                0x30cb:   0xc6,  # ニ KATAKANA LETTER NI
                0x30cc:   0xc7,  # ヌ KATAKANA LETTER NU
                0x30cd:   0xc8,  # ネ KATAKANA LETTER NE
                0x30ce:   0xc9,  # ノ KATAKANA LETTER NO
                0x30cf:   0xca,  # ハ KATAKANA LETTER HA
                0x30d2:   0xcb,  # ヒ KATAKANA LETTER HI
                0x30d5:   0xcc,  # フ KATAKANA LETTER HU
                0x30d8:   0xcd,  # ヘ KATAKANA LETTER HE
                0x30db:   0xce,  # ホ KATAKANA LETTER HO
                0x30de:   0xcf,  # マ KATAKANA LETTER MA
                0x30df:   0xd0,  # ミ KATAKANA LETTER MI
                0x30e0:   0xd1,  # ム KATAKANA LETTER MU
                0x30e1:   0xd2,  # メ KATAKANA LETTER ME
                0x30e2:   0xd3,  # モ KATAKANA LETTER MO
                0x30e4:   0xd4,  # ヤ KATAKANA LETTER YA
                0x30e6:   0xd5,  # ユ KATAKANA LETTER YU
                0x30e8:   0xd6,  # ヨ KATAKANA LETTER YO
                0x30e9:   0xd7,  # ラ KATAKANA LETTER RA
                0x30ea:   0xd8,  # リ KATAKANA LETTER RI
                0x30eb:   0xd9,  # ル KATAKANA LETTER RU
                0x30ec:   0xda,  # レ KATAKANA LETTER RE
                0x30ed:   0xdb,  # ロ KATAKANA LETTER RO
                0x30ef:   0xdc,  # ワ KATAKANA LETTER WA
                0x30f3:   0xdd,  # ン KATAKANA LETTER N
                0x309b:   0xde,  # ゛ KATAKANA-HIRAGANA VOICED SOUND MARK
                0x309c:   0xdf,  # ゜ KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK
                0x03b1:   0xe0,  # α GREEK SMALL LETTER ALPHA
                0x00e4:   0xe1,  # ä LATIN SMALL LETTER A WITH DIAERESIS
                0x03b2:   0xe2,  # β GREEK SMALL LETTER BETA (5x10)
                0x03b5:   0xe3,  # ε GREEK SMALL LETTER EPSILON
                0x00b5:   0xe4,  # µ MICRO SIGN (5x10)
                0x03bc:   0xe4,  # μ GREEK SMALL LETTER MU (5x10)
                0x03c3:   0xe5,  # σ GREEK SMALL LETTER SIGMA
                0x03c1:   0xe6,  # ρ GREEK SMALL LETTER RHO (5x10)
                0x221a:   0xe8,  # √ SQUARE ROOT
                0x02e3:   0xeb,  # ˣ MODIFIER LETTER SMALL X
                0x00a2:   0xec,  # ¢ CENT SIGN
                0x2c60:   0xed,  # Ⱡ LATIN CAPITAL LETTER L WITH DOUBLE BAR
                0x00f6:   0xef,  # ö LATIN SMALL LETTER O WITH DIAERESIS
                0x0398:   0xf2,  # Θ GREEK CAPITAL LETTER THETA
                0x03f4:   0xf2,  # ϴ GREEK CAPITAL THETA SYMBOL
                0x221e:   0xf3,  # ∞ INFINITY
                0x03a9:   0xf4,  # Ω GREEK CAPITAL LETTER OMEGA
                0x00fc:   0xf5,  # ü LATIN SMALL LETTER U WITH DIAERESIS (5x10)
                0x03a3:   0xf6,  # Σ GREEK CAPITAL LETTER SIGMA
                0x03c0:   0xf7,  # π GREEK SMALL LETTER PI
                0xa68b:   0xfb,  # ꚋ CYRILLIC SMALL LETTER TE WITH MIDDLE HOOK
                0x00f7:   0xfd,  # ÷ DIVISION SIGN
                0x25ae:   0xff,  # ▮ BLACK VERTICAL RECTANGLE
            },
            {   # A02 ENGLISH_EUROPEAN CHARACTER FONT
                # Note: Contains no 5x10 fonts
                0x25b6:   0x10,  # ▶ BLACK RIGHT-POINTING TRIANGLE
                0x25c0:   0x11,  # ◀ BLACK LEFT-POINTING TRIANGLE
                0x201c:   0x12,  # “ LEFT DOUBLE QUOTATION MARK
                0x201d:   0x13,  # ” RIGHT DOUBLE QUOTATION MARK
                0x23eb:   0x14,  # ⏫ BLACK UP-POINTING DOUBLE TRIANGLE
                0x23ec:   0x15,  # ⏬ BLACK DOWN-POINTING DOUBLE TRIANGLE
                0x25cf:   0x16,  # ● BLACK CIRCLE
                0x21b2:   0x17,  # ↲ DOWNWARDS ARROW WITH TIP LEFTWARDS
                0x2191:   0x18,  # ↑ UPWARDS ARROW
                0x2193:   0x19,  # ↓ DOWNWARDS ARROW
                0x2192:   0x1a,  # → RIGHTWARDS ARROW
                0x2190:   0x1b,  # ← LEFTWARDS ARROW
                0x2264:   0x1c,  # ≤ LESS-THAN OR EQUAL TO
                0x2265:   0x1d,  # ≥ GREATER-THAN OR EQUAL TO
                0x25b2:   0x1e,  # ▲ BLACK UP-POINTING TRIANGLE
                0x25bc:   0x1f,  # ▼ BLACK DOWN-POINTING TRIANGLE
                0x2019:   0x27,  # ’ RIGHT SINGLE QUOTATION MARK
                0x0410:   0x41,  # А CYRILLIC CAPITAL LETTER A
                0x0412:   0x42,  # В CYRILLIC CAPITAL LETTER VE
                0x0421:   0x43,  # С CYRILLIC CAPITAL LETTER ES
                0x0415:   0x45,  # Е CYRILLIC CAPITAL LETTER IE
                0x041d:   0x48,  # Н CYRILLIC CAPITAL LETTER EN
                0x041a:   0x4b,  # К CYRILLIC CAPITAL LETTER KA
                0x041c:   0x4d,  # М CYRILLIC CAPITAL LETTER EM
                0x041e:   0x4f,  # О CYRILLIC CAPITAL LETTER O
                0x0420:   0x50,  # Р CYRILLIC CAPITAL LETTER ER
                0x0422:   0x54,  # Т CYRILLIC CAPITAL LETTER TE
                0x0425:   0x58,  # Х CYRILLIC CAPITAL LETTER HA
                0x042c:   0x62,  # Ь CYRILLIC CAPITAL LETTER SOFT SIGN
                0x2302:   0x7f,  # ⌂ HOUSE
                0x0411:   0x80,  # Б CYRILLIC CAPITAL LETTER BE
                0x0414:   0x81,  # Д CYRILLIC CAPITAL LETTER DE
                0x0416:   0x82,  # Ж CYRILLIC CAPITAL LETTER ZHE
                0x0417:   0x83,  # З CYRILLIC CAPITAL LETTER ZE
                0x0418:   0x84,  # И CYRILLIC CAPITAL LETTER I
                0x0419:   0x85,  # Й CYRILLIC CAPITAL LETTER SHORT I
                0x041b:   0x86,  # Л CYRILLIC CAPITAL LETTER EL
                0x041f:   0x87,  # П CYRILLIC CAPITAL LETTER PE
                0x0423:   0x88,  # У CYRILLIC CAPITAL LETTER U
                0x0426:   0x89,  # Ц CYRILLIC CAPITAL LETTER TSE
                0x0427:   0x8a,  # Ч CYRILLIC CAPITAL LETTER CHE
                0x0428:   0x8b,  # Ш CYRILLIC CAPITAL LETTER SHA
                0x0429:   0x8c,  # Щ CYRILLIC CAPITAL LETTER SHCHA
                0x042a:   0x8d,  # Ъ CYRILLIC CAPITAL LETTER HARD SIGN
                0x042b:   0x8e,  # Ы CYRILLIC CAPITAL LETTER YERU
                0x042d:   0x8f,  # Э CYRILLIC CAPITAL LETTER E
                0x03b1:   0x90,  # α GREEK SMALL LETTER ALPHA
                0x266a:   0x91,  # ♪ EIGHTH NOTE
                0x0393:   0x92,  # Γ GREEK CAPITAL LETTER GAMMA
                0x0413:   0x92,  # Г CYRILLIC CAPITAL LETTER GHE
                0x03c0:   0x93,  # π GREEK SMALL LETTER PI
                0x03a3:   0x94,  # Σ GREEK CAPITAL LETTER SIGMA
                0x03c3:   0x95,  # σ GREEK SMALL LETTER SIGMA
                0x266c:   0x96,  # ♬ BEAMED SIXTEENTH NOTES
                0x03c4:   0x97,  # τ GREEK SMALL LETTER TAU
                0x1f514:  0x98,  # 🔔 BELL
                0x0398:   0x99,  # Θ GREEK CAPITAL LETTER THETA
                0x03a9:   0x9a,  # Ω GREEK CAPITAL LETTER OMEGA
                0x03b4:   0x9b,  # δ GREEK SMALL LETTER DELTA
                0x221e:   0x9c,  # ∞ INFINITY
                0x2665:   0x9d,  # ♥ BLACK HEART SUIT
                0x03b5:   0x9e,  # ε GREEK SMALL LETTER EPSILON
                0x2229:   0x9f,  # ∩ INTERSECTION
                0x23f8:   0xa0,  # ⏸ DOUBLE VERTICAL BAR
                0x00a1:   0xa1,  # ¡ INVERTED EXCLAMATION MARK
                0x00a2:   0xa2,  # ¢ CENT SIGN
                0x00a3:   0xa3,  # £ POUND SIGN
                0x00a4:   0xa4,  # ¤ CURRENCY SIGN
                0x00a5:   0xa5,  # ¥ YEN SIGN
                0x00a6:   0xa6,  # ¦ BROKEN BAR
                0x00a7:   0xa7,  # § SECTION SIGN
                0x0192:   0xa8,  # ƒ LATIN SMALL LETTER F WITH HOOK
                0x00a9:   0xa9,  # © COPYRIGHT SIGN
                0x00aa:   0xaa,  # ª FEMININE ORDINAL INDICATOR
                0x00ab:   0xab,  # « LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
                0x042e:   0xac,  # Ю CYRILLIC CAPITAL LETTER YU
                0x042f:   0xad,  # Я CYRILLIC CAPITAL LETTER YA
                0x00ae:   0xae,  # ® REGISTERED SIGN
                0x2018:   0xaf,  # ‘ LEFT SINGLE QUOTATION MARK
                0x00b0:   0xb0,  # ° DEGREE SIGN
                0x00b1:   0xb1,  # ± PLUS-MINUS SIGN
                0x00b2:   0xb2,  # ² SUPERSCRIPT TWO
                0x00b3:   0xb3,  # ³ SUPERSCRIPT THREE
                0x20a7:   0xb4,  # ₧ PESETA SIGN
                0x00b5:   0xb5,  # µ MICRO SIGN
                0x00b6:   0xb6,  # ¶ PILCROW SIGN
                0x00b7:   0xb7,  # · MIDDLE DOT
                0x03c9:   0xb8,  # ω GREEK SMALL LETTER OMEGA
                0x00b9:   0xb9,  # ¹ SUPERSCRIPT ONE
                0x00ba:   0xba,  # º MASCULINE ORDINAL INDICATOR
                0x00bb:   0xbb,  # » RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
                0x00bc:   0xbc,  # ¼ VULGAR FRACTION ONE QUARTER
                0x00bd:   0xbd,  # ½ VULGAR FRACTION ONE HALF
                0x00be:   0xbe,  # ¾ VULGAR FRACTION THREE QUARTERS
                0x00bf:   0xbf,  # ¿ INVERTED QUESTION MARK
                0x00c0:   0xc0,  # À LATIN CAPITAL LETTER A WITH GRAVE
                0x00c1:   0xc1,  # Á LATIN CAPITAL LETTER A WITH ACUTE
                0x00c2:   0xc2,  # Â LATIN CAPITAL LETTER A WITH CIRCUMFLEX
                0x00c3:   0xc3,  # Ã LATIN CAPITAL LETTER A WITH TILDE
                0x00c4:   0xc4,  # Ä LATIN CAPITAL LETTER A WITH DIAERESIS
                0x00c5:   0xc5,  # Å LATIN CAPITAL LETTER A WITH RING ABOVE
                0x00c6:   0xc6,  # Æ LATIN CAPITAL LETTER AE
                0x00c7:   0xc7,  # Ç LATIN CAPITAL LETTER C WITH CEDILLA
                0x00c8:   0xc8,  # È LATIN CAPITAL LETTER E WITH GRAVE
                0x00c9:   0xc9,  # É LATIN CAPITAL LETTER E WITH ACUTE
                0x00ca:   0xca,  # Ê LATIN CAPITAL LETTER E WITH CIRCUMFLEX
                0x00cb:   0xcb,  # Ë LATIN CAPITAL LETTER E WITH DIAERESIS
                0x00cc:   0xcc,  # Ì LATIN CAPITAL LETTER I WITH GRAVE
                0x00cd:   0xcd,  # Í LATIN CAPITAL LETTER I WITH ACUTE
                0x00ce:   0xce,  # Î LATIN CAPITAL LETTER I WITH CIRCUMFLEX
                0x00cf:   0xcf,  # Ï LATIN CAPITAL LETTER I WITH DIAERESIS
                0x00d0:   0xd0,  # Ð LATIN CAPITAL LETTER ETH
                0x00d1:   0xd1,  # Ñ LATIN CAPITAL LETTER N WITH TILDE
                0x00d2:   0xd2,  # Ò LATIN CAPITAL LETTER O WITH GRAVE
                0x00d3:   0xd3,  # Ó LATIN CAPITAL LETTER O WITH ACUTE
                0x00d4:   0xd4,  # Ô LATIN CAPITAL LETTER O WITH CIRCUMFLEX
                0x00d5:   0xd5,  # Õ LATIN CAPITAL LETTER O WITH TILDE
                0x00d6:   0xd6,  # Ö LATIN CAPITAL LETTER O WITH DIAERESIS
                0x00d7:   0xd7,  # × MULTIPLICATION SIGN
                0x00d8:   0xd8,  # Ø LATIN CAPITAL LETTER O WITH STROKE
                0x0424:   0xd8,  # Ф CYRILLIC CAPITAL LETTER EF
                0x00d9:   0xd9,  # Ù LATIN CAPITAL LETTER U WITH GRAVE
                0x00da:   0xda,  # Ú LATIN CAPITAL LETTER U WITH ACUTE
                0x00db:   0xdb,  # Û LATIN CAPITAL LETTER U WITH CIRCUMFLEX
                0x00dc:   0xdc,  # Ü LATIN CAPITAL LETTER U WITH DIAERESIS
                0x00dd:   0xdd,  # Ý LATIN CAPITAL LETTER Y WITH ACUTE
                0x00de:   0xde,  # Þ LATIN CAPITAL LETTER THORN
                0x00df:   0xdf,  # ß LATIN SMALL LETTER SHARP S
                0x00e0:   0xe0,  # à LATIN SMALL LETTER A WITH GRAVE
                0x00e1:   0xe1,  # á LATIN SMALL LETTER A WITH ACUTE
                0x00e2:   0xe2,  # â LATIN SMALL LETTER A WITH CIRCUMFLEX
                0x00e3:   0xe3,  # ã LATIN SMALL LETTER A WITH TILDE
                0x00e4:   0xe4,  # ä LATIN SMALL LETTER A WITH DIAERESIS
                0x00e5:   0xe5,  # å LATIN SMALL LETTER A WITH RING ABOVE
                0x00e6:   0xe6,  # æ LATIN SMALL LETTER AE
                0x00e7:   0xe7,  # ç LATIN SMALL LETTER C WITH CEDILLA
                0x00e8:   0xe8,  # è LATIN SMALL LETTER E WITH GRAVE
                0x00e9:   0xe9,  # é LATIN SMALL LETTER E WITH ACUTE
                0x00ea:   0xea,  # ê LATIN SMALL LETTER E WITH CIRCUMFLEX
                0x00eb:   0xeb,  # ë LATIN SMALL LETTER E WITH DIAERESIS
                0x00ec:   0xec,  # ì LATIN SMALL LETTER I WITH GRAVE
                0x00ed:   0xed,  # í LATIN SMALL LETTER I WITH ACUTE
                0x00ee:   0xee,  # î LATIN SMALL LETTER I WITH CIRCUMFLEX
                0x00ef:   0xef,  # ï LATIN SMALL LETTER I WITH DIAERESIS
                0x00f0:   0xf0,  # ð LATIN SMALL LETTER ETH
                0x00f1:   0xf1,  # ñ LATIN SMALL LETTER N WITH TILDE
                0x00f2:   0xf2,  # ò LATIN SMALL LETTER O WITH GRAVE
                0x00f3:   0xf3,  # ó LATIN SMALL LETTER O WITH ACUTE
                0x00f4:   0xf4,  # ô LATIN SMALL LETTER O WITH CIRCUMFLEX
                0x00f5:   0xf5,  # õ LATIN SMALL LETTER O WITH TILDE
                0x00f6:   0xf6,  # ö LATIN SMALL LETTER O WITH DIAERESIS
                0x00f7:   0xf7,  # ÷ DIVISION SIGN
                0x00f8:   0xf8,  # ø LATIN SMALL LETTER O WITH STROKE
                0x00f9:   0xf9,  # ù LATIN SMALL LETTER U WITH GRAVE
                0x00fa:   0xfa,  # ú LATIN SMALL LETTER U WITH ACUTE
                0x00fb:   0xfb,  # û LATIN SMALL LETTER U WITH CIRCUMFLEX
                0x00fc:   0xfc,  # ü LATIN SMALL LETTER U WITH DIAERESIS
                0x00fd:   0xfd,  # ý LATIN SMALL LETTER Y WITH ACUTE
                0x00fe:   0xfe,  # þ LATIN SMALL LETTER THORN
                0x00ff:   0xff,  # ÿ LATIN SMALL LETTER Y WITH DIAERESIS
            },
            {   # AiP31068L-002 EUROPEAN_RUSSIAN CHARACTER FONT
                # Missing maps for
                # 7f, cc, d0, d1, d2, d3, d4, d5, d6, dd, de, df, e3, e4, e5, e6, e7, e8, e9, ec, f5, f6, f7, f8, f9, fa, fb, fc
                0x0410:   0x41,  # А CYRILLIC CAPITAL LETTER A
                0x0412:   0x42,  # В CYRILLIC CAPITAL LETTER VE
                0x0421:   0x43,  # С CYRILLIC CAPITAL LETTER ES
                0x0415:   0x45,  # Е CYRILLIC CAPITAL LETTER IE
                0x041d:   0x48,  # Н CYRILLIC CAPITAL LETTER EN
                0x041a:   0x4b,  # К CYRILLIC CAPITAL LETTER KA
                0x041c:   0x4d,  # М CYRILLIC CAPITAL LETTER EM
                0x041e:   0x4f,  # О CYRILLIC CAPITAL LETTER O
                0x0420:   0x50,  # Р CYRILLIC CAPITAL LETTER ER
                0x0422:   0x54,  # Т CYRILLIC CAPITAL LETTER TE
                0x0425:   0x58,  # Х CYRILLIC CAPITAL LETTER HA
                0x00a2:   0x5c,  # ¢ CENT SIGN
                0x042c:   0x62,  # Ь CYRILLIC CAPITAL LETTER SOFT SIGN
                0x21b5:   0x7e,  # ↵ RIGHTWARDS ARROW
                #         0x7f,  # ???
                0x0411:   0xa0,  # Б CYRILLIC CAPITAL LETTER BE
                0x0413:   0xa1,  # Г CYRILLIC CAPITAL LETTER GHE
                0x0401:   0xa2,  # Ё CYRILLIC CAPITAL LETTER IO
                0x0416:   0xa3,  # Ж CYRILLIC CAPITAL LETTER ZHE
                0x0417:   0xa4,  # З CYRILLIC CAPITAL LETTER ZE
                0x0418:   0xa5,  # И CYRILLIC CAPITAL LETTER I
                0x0419:   0xa6,  # Й CYRILLIC CAPITAL LETTER SHORT I
                0x041b:   0xa7,  # Л CYRILLIC CAPITAL LETTER EL
                0x041f:   0xa8,  # П CYRILLIC CAPITAL LETTER PE
                0x0423:   0xa9,  # У CYRILLIC CAPITAL LETTER U
                0x0424:   0xaa,  # Ф CYRILLIC CAPITAL LETTER EF
                0x0427:   0xab,  # Ч CYRILLIC CAPITAL LETTER CHE
                0x0428:   0xac,  # Ш CYRILLIC CAPITAL LETTER SHA
                0x042a:   0xad,  # Ъ CYRILLIC CAPITAL LETTER HARD SIGN
                0x042b:   0xae,  # Ы CYRILLIC CAPITAL LETTER YERU
                0x042d:   0xaf,  # Э CYRILLIC CAPITAL LETTER E
                0x042e:   0xb0,  # Ю CYRILLIC CAPITAL LETTER YU
                0x042f:   0xb1,  # Я CYRILLIC CAPITAL LETTER YA
                0x0431:   0xb2,  # б CYRILLIC SMALL LETTER BE
                0x0432:   0xb3,  # в CYRILLIC SMALL LETTER VE
                0x0433:   0xb4,  # г CYRILLIC SMALL LETTER GHE
                0x0451:   0xb5,  # ё CYRILLIC SMALL LETTER IO
                0x0436:   0xb6,  # ж CYRILLIC SMALL LETTER ZHE
                0x0437:   0xb7,  # з CYRILLIC SMALL LETTER ZE
                0x0438:   0xb8,  # и CYRILLIC SMALL LETTER I
                0x0439:   0xb9,  # й CYRILLIC SMALL LETTER SHORT I
                0x043a:   0xba,  # к CYRILLIC SMALL LETTER KA
                0x043b:   0xbb,  # л CYRILLIC SMALL LETTER EL
                0x043c:   0xbc,  # м CYRILLIC SMALL LETTER EM
                0x043d:   0xbd,  # н CYRILLIC SMALL LETTER EN
                0x043f:   0xbe,  # п CYRILLIC SMALL LETTER PE
                0x0442:   0xbf,  # т CYRILLIC SMALL LETTER TE
                0x0447:   0xc0,  # ч CYRILLIC SMALL LETTER CHE
                0x0448:   0xc1,  # ш CYRILLIC SMALL LETTER SHA
                0x044a:   0xc2,  # ъ CYRILLIC SMALL LETTER HARD SIGN
                0x044b:   0xc3,  # ы CYRILLIC SMALL LETTER YERU
                0x044c:   0xc4,  # ь CYRILLIC SMALL LETTER SOFT SIGN
                0x044d:   0xc5,  # э CYRILLIC SMALL LETTER E
                0x044e:   0xc6,  # ю CYRILLIC SMALL LETTER YU
                0x044f:   0xc7,  # я CYRILLIC SMALL LETTER YA
                0x00ab:   0xc8,  # « LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
                0x00bb:   0xc9,  # » RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
                0x201c:   0xca,  # “ LEFT DOUBLE QUOTATION MARK
                0x201d:   0xcb,  # ” RIGHT DOUBLE QUOTATION MARK
                #         0xcc,  # ???
                0x00bf:   0xcd,  # ¿ INVERTED QUESTION MARK
                0x2a0d:   0xce,  # ⨍ FINITE PART INTEGRAL
                0x00a3:   0xcf,  # £ POUND SIGN
                #         0xd0,  # ???
                #         0xd1,  # ???
                #         0xd2,  # ???
                #         0xd3,  # ???
                #         0xd4,  # ???
                #         0xd5,  # ???
                #         0xd6,  # ???
                0x2160:   0xd7,  # Ⅰ ROMAN NUMERAL ONE
                0x2161:   0xd8,  # Ⅱ ROMAN NUMERAL TWO
                0x2191:   0xd9,  # ↑ UPWARDS ARROW
                0x2193:   0xda,  # ↓ DOWNWARDS ARROW
                0x21e4:   0xdb,  # ⇤ LEFTWARDS ARROW TO BAR
                0x21e5:   0xdc,  # ⇥ RIGHTWARDS ARROW TO BAR
                #         0xdd,  # ???
                #         0xde,  # ???
                #         0xdf,  # ???
                0x0414:   0xe0,  # Д CYRILLIC CAPITAL LETTER DE
                0x0426:   0xe1,  # Ц CYRILLIC CAPITAL LETTER TSE
                0x0429:   0xe2,  # Щ CYRILLIC CAPITAL LETTER SHCHA
                #         0xe3,  # ???
                #         0xe4,  # ???
                #         0xe5,  # ???
                #         0xe6,  # ???
                #         0xe7,  # ???
                #         0xe8,  # ???
                #         0xe9,  # ???
                0x00e9:   0xea,  # é LATIN SMALL LETTER E WITH ACUTE
                0x00e7:   0xeb,  # ç LATIN SMALL LETTER C WITH CEDILLA
                #         0xec,  # ???
                0x1f514:  0xed,  # 🔔 BELL
                0x25cc:   0xee,  # ◌ DOTTED CIRCLE
                0x25cb:   0xef,  # ○ WHITE CIRCLE
                0x00bc:   0xf0,  # ¼ VULGAR FRACTION ONE QUARTER
                0x2153:   0xf1,  # ⅓ VULGAR FRACTION ONE THIRD
                0x00bd:   0xf2,  # ½ VULGAR FRACTION ONE HALF
                0x00be:   0xf3,  # ¾ VULGAR FRACTION THREE QUARTERS
                0x2338:   0xf4,  # ⌸ APL FUNCTIONAL SYMBOL QUAD EQUAL
                #         0xf5,  # ???
                #         0xf6,  # ???
                #         0xf7,  # ???
                #         0xf8,  # ???
                #         0xf9,  # ???
                #         0xfa,  # ???
                #         0xfb,  # ???
                #         0xfc,  # ???
                0x00a7:   0xfd,  # § SECTION SIGN
                0x00b6:   0xfe,  # ¶ PILCROW SIGN
                0x25ae:   0xff,  # ▮ BLACK VERTICAL RECTANGLE
            },
            {   # AiP31068L-003 WESTERN EUROPEAN CHARACTER FONT
                # Missing maps for
                # 12, 13, 14, 15, 16, 17, 18, 19, 9d, 9e, c0, c1
                0x00b1:   0x10,  # ± PLUS-MINUS SIGN
                0x2261:   0x11,  # ≡ IDENTICAL TO
                #         0x12,  # ???
                #         0x13,  # ???
                #         0x14,  # ???
                #         0x15,  # ???
                #         0x16,  # ???
                #         0x17,  # ???
                #         0x18,  # ???
                #         0x19,  # ???
                0x2248:   0x20,  # ≈ ALMOST EQUAL TO
                0x222b:   0x21,  # ∫ INTEGRAL
                0xfe66:   0x22,  # ﹦ SMALL EQUALS SIGN
                0x223f:   0x23,  # ∿ SINE WAVE
                0x00b2:   0x24,  # ² SUPERSCRIPT TWO
                0x00b3:   0x25,  # ³ SUPERSCRIPT THREE
                0x0410:   0x41,  # А CYRILLIC CAPITAL LETTER A
                0x0412:   0x42,  # В CYRILLIC CAPITAL LETTER VE
                0x0421:   0x43,  # С CYRILLIC CAPITAL LETTER ES
                0x0415:   0x45,  # Е CYRILLIC CAPITAL LETTER IE
                0x041d:   0x48,  # Н CYRILLIC CAPITAL LETTER EN
                0x041a:   0x4b,  # К CYRILLIC CAPITAL LETTER KA
                0x041c:   0x4d,  # М CYRILLIC CAPITAL LETTER EM
                0x041e:   0x4f,  # О CYRILLIC CAPITAL LETTER O
                0x0420:   0x50,  # Р CYRILLIC CAPITAL LETTER ER
                0x0422:   0x54,  # Т CYRILLIC CAPITAL LETTER TE
                0x0425:   0x58,  # Х CYRILLIC CAPITAL LETTER HA
                0x042c:   0x62,  # Ь CYRILLIC CAPITAL LETTER SOFT SIGN
                0x0394:   0x7f,  # Δ GREEK CAPITAL LETTER DELTA
                0x00c7:   0x80,  # Ç LATIN CAPITAL LETTER C WITH CEDILLA
                0x00fc:   0x81,  # ü LATIN SMALL LETTER U WITH DIAERESIS
                0x00e9:   0x82,  # é LATIN SMALL LETTER E WITH ACUTE
                0x00e2:   0x83,  # â LATIN SMALL LETTER A WITH CIRCUMFLEX
                0x00e4:   0x84,  # ä LATIN SMALL LETTER A WITH DIAERESIS
                0x00e0:   0x85,  # à LATIN SMALL LETTER A WITH GRAVE
                0x0227:   0x86,  # ȧ LATIN SMALL LETTER A WITH DOT ABOVE
                0x00e7:   0x87,  # ç LATIN SMALL LETTER C WITH CEDILLA
                0x00ea:   0x88,  # ê LATIN SMALL LETTER E WITH CIRCUMFLEX
                0x00eb:   0x89,  # ë LATIN SMALL LETTER E WITH DIAERESIS
                0x00e8:   0x8a,  # è LATIN SMALL LETTER E WITH GRAVE
                0x00ef:   0x8b,  # ï LATIN SMALL LETTER I WITH DIAERESIS
                0x00ee:   0x8c,  # î LATIN SMALL LETTER I WITH CIRCUMFLEX
                0x00ec:   0x8d,  # ì LATIN SMALL LETTER I WITH GRAVE
                0x00c4:   0x8e,  # Ä LATIN CAPITAL LETTER A WITH DIAERESIS
                0x00c2:   0x8f,  # Â LATIN CAPITAL LETTER A WITH CIRCUMFLEX
                0x00c9:   0x90,  # É LATIN CAPITAL LETTER E WITH ACUTE
                0x00e6:   0x91,  # æ LATIN SMALL LETTER AE
                0x00c6:   0x92,  # Æ LATIN CAPITAL LETTER AE
                0x00f4:   0x93,  # ô LATIN SMALL LETTER O WITH CIRCUMFLEX
                0x00d4:   0x93,  # Ô LATIN CAPITAL LETTER O WITH CIRCUMFLEX
                0x00f6:   0x94,  # ö LATIN SMALL LETTER O WITH DIAERESIS
                0x00f2:   0x95,  # ò LATIN SMALL LETTER O WITH GRAVE
                0x00fb:   0x96,  # û LATIN SMALL LETTER U WITH CIRCUMFLEX
                0x00f9:   0x97,  # ù LATIN SMALL LETTER U WITH GRAVE
                0x00ff:   0x98,  # ÿ LATIN SMALL LETTER Y WITH DIAERESIS
                0x014e:   0x99,  # Ŏ LATIN CAPITAL LETTER O WITH BREVE
                0x00dc:   0x9a,  # Ü LATIN CAPITAL LETTER U WITH DIAERESIS
                0x00f1:   0x9b,  # ñ LATIN SMALL LETTER N WITH TILDE
                0x00d1:   0x9c,  # Ñ LATIN CAPITAL LETTER N WITH TILDE
                #         0x9d,  # ???
                #         0x9e,  # ???
                0x00bf:   0x9f,  # ¿ INVERTED QUESTION MARK
                0x00e1:   0xa0,  # á LATIN SMALL LETTER A WITH ACUTE
                0x00ed:   0xa1,  # í LATIN SMALL LETTER I WITH ACUTE
                0x00f3:   0xa2,  # ó LATIN SMALL LETTER O WITH ACUTE
                0x00fa:   0xa3,  # ú LATIN SMALL LETTER U WITH ACUTE
                0x00a2:   0xa4,  # ¢ CENT SIGN
                0x00a3:   0xa5,  # £ POUND SIGN
                0x00a5:   0xa6,  # ¥ YEN SIGN
                0x20bd:   0xa7,  # ₽ RUBLE SIGN
                0x2a0d:   0xa8,  # ⨍ FINITE PART INTEGRAL
                0x00a1:   0xa9,  # ¡ INVERTED EXCLAMATION MARK
                0x00c3:   0xaa,  # Ã LATIN CAPITAL LETTER A WITH TILDE
                0x00e3:   0xab,  # ã LATIN SMALL LETTER A WITH TILDE
                0x00d5:   0xac,  # Õ LATIN CAPITAL LETTER O WITH TILDE
                0x00f5:   0xad,  # õ LATIN SMALL LETTER O WITH TILDE
                0x00d8:   0xae,  # Ø LATIN CAPITAL LETTER O WITH STROKE
                0x00f8:   0xaf,  # ø LATIN SMALL LETTER O WITH STROKE
                0x00a8:   0xb1,  # ¨ DIAERESIS
                0x00b0:   0xb2,  # ° DEGREE SIGN
                0x0060:   0xb3,  # ` GRAVE ACCENT
                0x00b4:   0xb4,  # ´ ACUTE ACCENT
                0x00bd:   0xb5,  # ½ VULGAR FRACTION ONE HALF
                0x00bc:   0xb6,  # ¼ VULGAR FRACTION ONE QUARTER
                0x00d7:   0xb7,  # × MULTIPLICATION SIGN
                0x00f7:   0xb8,  # ÷ DIVISION SIGN
                0x2264:   0xb9,  # ≤ LESS-THAN OR EQUAL TO
                0x2265:   0xba,  # ≥ GREATER-THAN OR EQUAL TO
                0x00ab:   0xbb,  # « LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
                0x00bb:   0xbc,  # » RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
                0x2260:   0xbd,  # ≠ NOT EQUAL TO
                0x221a:   0xbe,  # √ SQUARE ROOT
                0x203e:   0xbf,  # ‾ OVERLINE
                #         0xc0,  # ???
                #         0xc1,  # ???
                0x221e:   0xc2,  # ∞ INFINITY
                0x25f8:   0xc3,  # ◸ UPPER LEFT TRIANGLE
                0x21b5:   0xc4,  # ↵ RIGHTWARDS ARROW
                0x2191:   0xc5,  # ↑ UPWARDS ARROW
                0x2193:   0xc6,  # ↓ DOWNWARDS ARROW
                0x2192:   0xc7,  # → RIGHTWARDS ARROW
                0x2190:   0xc8,  # ← LEFTWARDS ARROW
                0x250c:   0xc9,  # ┌ BOX DRAWINGS LIGHT DOWN AND RIGHT
                0x2510:   0xca,  # ┐ BOX DRAWINGS LIGHT DOWN AND LEFT
                0x2514:   0xcb,  # └ BOX DRAWINGS LIGHT UP AND RIGHT
                0x2518:   0xcc,  # ┘ BOX DRAWINGS LIGHT UP AND LEFT
                0x22c5:   0xcd,  # ․ ONE DOT LEADER
                0x00ae:   0xce,  # ® REGISTERED SIGN
                0x00a9:   0xcf,  # © COPYRIGHT SIGN
                0x2122:   0xd0,  # ™ TRADE MARK SIGN
                0x03ee:   0xd1,  # ✝ COPTIC CAPITAL LETTER DEI
                0x00a7:   0xd2,  # § SECTION SIGN
                0x00b6:   0xd3,  # ¶ PILCROW SIGN
                0x0393:   0xd4,  # Γ GREEK CAPITAL LETTER GAMMA
                0x25ff:   0xd5,  # ◿ LOWER RIGHT TRIANGLE
                0x03f4:   0xd6,  # ϴ GREEK CAPITAL THETA SYMBOL
                0x039b:   0xd7,  # Λ GREEK CAPITAL LETTER LAMDA
                0x039e:   0xd8,  # Ξ GREEK CAPITAL LETTER XI
                0x03a0:   0xd9,  # Π GREEK CAPITAL LETTER PI
                0x03a3:   0xda,  # Σ GREEK CAPITAL LETTER SIGMA
                0x0372:   0xdb,  # Ͳ GREEK CAPITAL LETTER ARCHAIC SAMPI
                0x03a6:   0xdc,  # Φ GREEK CAPITAL LETTER PHI
                0x03a8:   0xdd,  # Ψ GREEK CAPITAL LETTER PSI
                0x03a9:   0xde,  # Ω GREEK CAPITAL LETTER OMEGA
                0x03b1:   0xdf,  # α GREEK SMALL LETTER ALPHA
                0x03b2:   0xe0,  # β GREEK SMALL LETTER BETA
                0x03b3:   0xe1,  # γ GREEK SMALL LETTER GAMMA
                0x03b4:   0xe2,  # δ GREEK SMALL LETTER DELTA
                0x03b5:   0xe3,  # ε GREEK SMALL LETTER EPSILON
                0x03b6:   0xe4,  # ζ GREEK SMALL LETTER ZETA
                0x03b7:   0xe5,  # η GREEK SMALL LETTER ETA
                0x03b8:   0xe6,  # θ GREEK SMALL LETTER THETA
                0x03b9:   0xe7,  # ι GREEK SMALL LETTER IOTA
                0x03ba:   0xe8,  # κ GREEK SMALL LETTER KAPPA
                0x03bb:   0xe9,  # λ GREEK SMALL LETTER LAMDA
                0x03bc:   0xea,  # μ GREEK SMALL LETTER MU
                0x03bd:   0xeb,  # ν GREEK SMALL LETTER NU
                0x03be:   0xec,  # ξ GREEK SMALL LETTER XI
                0x03c0:   0xed,  # π GREEK SMALL LETTER PI
                0x03c1:   0xee,  # ρ GREEK SMALL LETTER RHO
                0x03c3:   0xef,  # σ GREEK SMALL LETTER SIGMA
                0x03c4:   0xf0,  # τ GREEK SMALL LETTER TAU
                0x03c5:   0xf1,  # υ GREEK SMALL LETTER UPSILON
                0x03c7:   0xf2,  # χ GREEK SMALL LETTER CHI
                0x03c8:   0xf3,  # ψ GREEK SMALL LETTER PSI
                0x03c9:   0xf4,  # ω GREEK SMALL LETTER OMEGA
                0x25bc:   0xf5,  # ▼ BLACK DOWN-POINTING TRIANGLE
                0x25b6:   0xf6,  # ▶ BLACK RIGHT-POINTING TRIANGLE
                0x25c0:   0xf7,  # ◀ BLACK LEFT-POINTING TRIANGLE
                0x1d5e5:  0xf8,  # 𝗥 MATHEMATICAL SANS-SERIF BOLD CAPITAL R
                0x21a4:   0xf9,  # ↤ LEFTWARDS ARROW FROM BAR
                0x1d5d9:  0xfa,  # 𝗙 MATHEMATICAL SANS-SERIF BOLD CAPITAL F
                0x21a6:   0xfb,  # ↦ RIGHTWARDS ARROW FROM BAR
                0x25af:   0xfc,  # ▯ WHITE VERTICAL RECTANGLE
                0x25ac:   0xfd,  # ▬ BLACK RECTANGLE
                0x1f182:  0xfe,  # 🆂 NEGATIVE SQUARED LATIN CAPITAL LETTER S
                0x1f17f:  0xff,  # 🅿 NEGATIVE SQUARED LATIN CAPITAL LETTER P
            },
            {   # 901 FRENCH, POLISH AND SILESIAN ACCENTED CHARACTERS
                0x00c0:   0xa0,  # À LATIN CAPITAL LETTER A WITH GRAVE
                0x00c1:   0xa1,  # Á LATIN CAPITAL LETTER A WITH ACUTE
                0x00c8:   0xa2,  # È LATIN CAPITAL LETTER E WITH GRAVE
                0x00ca:   0xa3,  # Ê LATIN CAPITAL LETTER E WITH CIRCUMFLEX
                0x00cb:   0xa4,  # Ë LATIN CAPITAL LETTER E WITH DIAERESIS
                0x00ce:   0xa5,  # Î LATIN CAPITAL LETTER I WITH CIRCUMFLEX
                0x00cf:   0xa6,  # Ï LATIN CAPITAL LETTER I WITH DIAERESIS
                0x0152:   0xa7,  # Œ LATIN CAPITAL LIGATURE OE
                0x0153:   0xa8,  # œ LATIN SMALL LIGATURE OE
                0x00d9:   0xa9,  # Ù LATIN CAPITAL LETTER U WITH GRAVE
                0x00db:   0xaa,  # Û LATIN CAPITAL LETTER U WITH CIRCUMFLEX
                0x0178:   0xab,  # Ÿ LATIN CAPITAL LETTER Y WITH DIAERESIS
                0x014c:   0xac,  # Ō LATIN CAPITAL LETTER O WITH MACRON
                0x014d:   0xad,  # ō LATIN SMALL LETTER O WITH MACRON
                0x014f:   0xae,  # ŏ LATIN SMALL LETTER O WITH BREVE
                0x0104:   0xb0,  # Ą LATIN CAPITAL LETTER A WITH OGONEK
                0x0106:   0xb1,  # Ć LATIN CAPITAL LETTER C WITH ACUTE
                0x0118:   0xb2,  # Ę LATIN CAPITAL LETTER E WITH OGONEK
                0x0141:   0xb3,  # Ł LATIN CAPITAL LETTER L WITH STROKE
                0x0143:   0xb4,  # Ń LATIN CAPITAL LETTER N WITH ACUTE
                0x00d3:   0xb5,  # Ó LATIN CAPITAL LETTER O WITH ACUTE
                0x015a:   0xb6,  # Ś LATIN CAPITAL LETTER S WITH ACUTE
                0x015b:   0xb6,  # ś LATIN SMALL LETTER S WITH ACUTE
                0x0179:   0xb7,  # Ź LATIN CAPITAL LETTER Z WITH ACUTE
                0x017a:   0xb7,  # ź LATIN SMALL LETTER Z WITH ACUTE
                0x017b:   0xb8,  # Ż LATIN CAPITAL LETTER Z WITH DOT ABOVE
                0x017c:   0xb8,  # ż LATIN SMALL LETTER Z WITH DOT ABOVE
                0x0105:   0xb9,  # ą LATIN SMALL LETTER A WITH OGONEK
                0x0107:   0xba,  # ć LATIN SMALL LETTER C WITH ACUTE
                0x0119:   0xbb,  # ę LATIN SMALL LETTER E WITH OGONEK
                0x0142:   0xbc,  # ł LATIN SMALL LETTER L WITH STROKE
                0x0144:   0xbd,  # ń LATIN SMALL LETTER N WITH ACUTE
                0x016e:   0xbe,  # Ů LATIN CAPITAL LETTER U WITH RING ABOVE
                0x016f:   0xbf,  # ů LATIN SMALL LETTER U WITH RING ABOVE

            }
        ],
        'fonts': [
            # A00 ENGLISH_JAPANESE CHARACTER FONT (aka AiP31068L-001)
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x14\xa2a\x8c\x12\x00\x00\x00\x00q\x1d\xf1|\xdfs\x80\x01\x01\x0es\xbc\xee\x7f\xee\x8b\x8f\x18F.\xf3\xbc\xff\xc61\x8c\x7f\xc8\xb8\x80@ \x00\x80\xc0\x81\x05\x06\x00\x00\x00\x00\x04\x00\x00\x00\x00" \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x14\xa7\xe6D!\x08@\x00\x01\x8b"#A\x11\x8cX\xc2\x00\x91\x8cc\x19B\x11\x89\x05(n1\x8cc\x02F1\x8cC\x05\t@  \x00\x81/\x80\x01\x02\x00\x00\x00\x00\x04\x00\x00\x00\x00B\x10\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x03\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x15\xfa\n\x88@\xaa@\x00\x02\x99\x02Ez\x01\x8cX\xc4|A\x0cc\x08\xc2\x10\x89\x05HW1\x8cc\x02F1TE\x0f\x8a \x13\xac\xe6\xb9\x11\xb3\r"j\xce\xf3l\xeeF1\x8c~B\x10H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00?\x11>$\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xa7\x11\x00@\x9d\xf0|\x04\xa9\x04)\x07\xc2s\xc0\x08\x00"l}\x08\xfb\xd7\xf9\x05\x88V\xb1\xf4|\xe2F5"\x89\x02\x08\x00\x00s\t\xc7\x91\xc9\x05BW1\x8c\xf3\x04F5TD\x82\x0b\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08@3\xe1\'\xc9\xff\xb8U\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf2\xa2\xa0@\xaaF\x00\x08\xc9\x08\x1f\x86$\x88X\xc4|D\xaf\xe3\x08\xc2\x11\x89\x05HFq\x85h\x12F5Q\x11\x0f\x88\x00\x03\xe3\x08\xfd\x0f\x89\x05\x82V1\xf3\xe0\xe4F5#\xc8B\x10H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00H0&dHd\x8b\xd5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xafN@!\x08B\x01\x90\x89\x11\x11F$\x88\x98B\x00\x80\xacc\x19B\x11\x89%(F1\x84\xa4\x12EU\x89!\x02\x08\x00\x04c\x18\xc1\x01\x89%BF1\x80`\x14\xcdUPPB\x10\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00D\x00D\xa0H\xa5\x08A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xa2\r\xa0\x12\x00\x04\x01\x80s\xbe\xe19\xc4s\x00\x81\x01\x04t|\xee~\x0f\x8b\x99\x1f\xc6.\x83c\xe28\x8a\x89?\xc28\x1f\x03\xfc\xe7\xb9\x0e\x8b\x99\'F.\x80a\xe34\x8a\x8b\xbe" \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x01\xc2\x00\x88!\xbf$\x7f\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xc2@\t\x04\x02\x00\xa0\x01\x00\x00\x80\xe4\x10\x00 \x81\x00\x00\x80\x00\x00\x04\x00\x0e\x90\x00\x00\x00\x9c\x02\x80\x00\x00\x00\x00\x04\x00!\xca\x00\x00\x00+\xe0\xf8\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00E\xff\xff\xff{\xff\xfc\x7f\xf1\x7f*\x04\x11\xdf\xf8\x89\x0f\xa3\xffq\x03\xf4;\xe0\x91!\xff\xe2T\x00\x00\x00\x00\x00\x00\x81B \x00\x00\x1c\x00\x02\x00\x00\x02\x00\x10\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01I\x12\t$L\x82\xa0\x851I+\xf4|\x01\x10\x85\xf0\xd0\x81\x02\x02\x8f\x88?\x95!\x18\x81\x1cK\x9c\xe8\xbc\xcf>\x8c\x87r\xce\xb3b\x07E\x1f\x8c}\xff\x80\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf9\x99\x12\x19?\x88\x82\xac\x89I\xaf\xeaF\x10\n \xa3\x00\x88\x81t\x15\xf4\x8b\xe1\x95#\x18\x84\x00\xa8c\x08\xd11 \x85J#1\xcc\xfe\xb8\xc4\x8aTH\x8a\xfc\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01(\x12)$\x08\x82 \x91\x01\x19\x02E\x10\x04p\xa3\x00\x86\xaa\x04H\x85\x08!\x15e\x10\x84\x00\x93\xfc\xc8\xca1 \x04\n\xf21\x8ccX\xc5\n$~\xff\x80\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x08"I$\x10\x82A)\x02\x11\x04D \n\xa9#\x01\x06\xa4w\xd4\x84\x08"%i\x11\x08\x00\x94c\x19\xc61\xa0\x04\x07"1\x8cc\xa5F\nTH\x98\x90\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x08O\x8aDa>\x8eD\xecb\x08\x84C\xf0""\xf6\x00\x82\x08`t\x7f\xe4E\xb1\xf2p\x00k\xfc\xee\xbb\xcf@\x04\x02>.\xf3\xdc\r\xcf\xf3\x8b\xc9\x18\x80\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x08\x02\x01\x00\x04\x00\x00\x00\x80@\x004\x00\x00@\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x08\x02\x01\x00$\x00\x00\x00\x80@\x00\x00\x00\x00@\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x08\x02\x0e\x00\x18\x00\x00\x00\x80@\x00\x00\x00\x03\x80\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',

            # A02 WESTERN EUROPEAN CHARACTER FONT
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x93\xb2|\x01!\x00\x01 \x00\x01\x14\xa2a\x8c\x12\x00\x00\x00\x00q\x1d\xf1|\xdfs\x80\x01\x01\x0eq<\xee\x7f\xee\x8b\x8f\x18F.\xf3\xbc\xef\xc61\x8c~\xe08\x80@ \x00\x80\xc0\x81\x05\x06\x00\x00\x00\x00\x04\x00\x00\x00\x00" \x04\xf9k\xe8\x91\xff\x8cb\n\xe2.\x01>\x0f\x80\xa0#\x80`\x00\x0e\xd9\x08`D\x86\x17\xdc\t?\xe4a\xa4\x979\xc1q\x08B\x10\x9f\x01\x14\xa7\xe6D!\x08@\x00\x01\x8b"#A\x11\x8cX\xc2\x00\x91\x8a\xa3\x19B\x11\x89\x05(n1\x8cc\x12F1\x8cB\x88\t@  \x00\x81 \x80\x01\x02\x00\x00\x00\x00\x04\x00\x00\x00\x00B\x10\n\x89j\x18\xc4\xb1\x8ccZ\xa21\x01\xa2\x08\x00\xe1t\\\x90(\x11\xd8\x1c\x88\xa8\x89,BZ\xc6(s\xb7/\x93\xe5\xa9\x04\x84\x08\x8e\x01\x15\xfa\n\x88@\xaa@\x00\x02\x99\x02Ez\x01\x8cX\xc4|A\x0cc\x08\xc2\x10\x89\x05HW1\x8cc\x02F1TD\x84\n \x13\xac\xe6\xb9\x0f\xb1\r"j\xce\xf3l\xeeF1\x8c~B\x10\x11\x82j\x19\xc4\xb1\x8ccZ\xa2%Ia\xf4<\xaetbE\xfd\xd1\xd8(\x87|\x84%^\xaa\xc6\xac\x7f\x80\x00\x03\xe9!?\xf2\x11\xce\x01\x00\xa7\x11\x00@\x9d\xf0|\x04\xa9\x04)\x07\xc2s\xc0\x08\x00"l}\x08\xfb\xd7\xf9\x05\x88V\xb1\xf4|\xe2F5"\x88\x82\x08\x00\x00s\t\xc7\x91\xcb\x05BW1\x8c\xf3\x04F1TD\x82\t\xb1\xf4\\j\xcc\xb1T_Z\xbb+\xa9`\xa2H\xb4w\xe2\xaa\xfe\x11\xd9)\xc5\x10\n\xfd\xe3N\xbe s\x80\x02\x7f\xff%D\x81!\xc4\x00\x01\xf2\xa2\xa0@\xaaF\x00\x08\xc9\x08\x1f\x86$\x88X\xc4|D\xaf\xe3\x08\xc2\x11\x89\x05HFq\x85h\x12F5Q\x10\x81\x08\x00\x03\xe3\x08\xfd\x0f\x89\x05\x82V1\xf3\xe0\xe4F5#\xc8B\x12Q\x8f\xea\x1c\xd4\xb1$CZ\xa6\xa1\x91 \xa4K\xa4\xfcc\x1d}\x91\xd9*\x87|\x84%^\xaa\x96`a\x80\x079\xc8#\x88@\x03\xe4\x00\x00\xafN@!\x08B\x01\x90\x89\x11\x11F$\x88\x98B\x00\x80\xacc\x19B\x11\x89%(F1\x84\xa5\x12EU\x89 \x80\x88\x00\x04c\x18\xc1\x01\x89%BV1\x80`\x14\xcdUPPB\x10\x1f\x8cj\x18\xe6\xb1G\xc3_\xa6\xb1\x97 \xa8Kd$U\x10:1\xd9\x1c\x98\x90\x92\xa4@Z\xa6\xa0@\x80\x0f\x90\x04!\x00\x0f\xfc\x00\x01\x00\xa2\r\xa0\x12\x00\x04\x01\x80s\xbe\xe19\xc4s\x00\x81\x01\x04t|\xee~\x0f\x8b\x99\x1f\xc6.\x83b\xe28\x8a\x89>\xe08\x1f\x03\xfc\xe7\xb9\x0e\x8b\x99\'V.\x80a\xe34\x8a\x8b\xbe" \x00\xf4k\xe8\xc51\x80C\xf0\xbb.o!?\xb0b\x03\xb6\xe0\x11\xd1\xd9\t`\x10\x8cG\xfe\tG\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x19\xce\x00\x00\x02\x00\x08\xc7\x00@\x88\xd5\x10\x0e@\x88\x04\x08\x80\x03P"5@\x02\x04E\x0b\x00@\x88\xd0\x10\x00@\x88\x04\x08\x80\x03P \x00\x00\x02\x04@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x91$)E\xe0\x06\x1c\tI\x04!\x15 (\xf1!\x14\xa2\x11Jt\x88EH\x00q\x08\xa0\x11\x06!\x15%(\x00!\x14\xa2\x11J\xa4\x88B5@\x11\x08\xa5\t\x8a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x91\x08\xceF`\x02#JS\x00!\x00\x02\x11\x90\x00\x00\x00\x00\x00H\x1c\xe0\x01\xd1$b\x08\xc5\xc9\x00\x00\x00\x13N\x00\x00\x00\x00\x00@\x00\x05H\x04 \x00\x00\x10\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x97\xd0(F`R"\xa5)$R\x9c\xe5:\x90\xff\xff\xf79\xceLc\x17:*tc\x18\xa9)s\x9c\xe78\xb0s\x9c\xe2\x10\x84\xa5\x9c\xe0\x01\xc0tc\x18\xc4\xd1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00a=\xc9M\xec\x8f"[Wh\x8cc\x18\xc6\xf1\x84!\x02\x10\x84\xeec\x18\xc6$\xacc\x18\x91.\x08B\x10\x85\xf1\x8cc\x161\x8c\x16c\x17:?\xacc\x18\xc4\xb1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0b\xf4l\xa8\x1c\xa5\x04\xb0\xff\xff\xff\xff\x8e\xf7\xbd\xe2\x10\x84Mc\x18\xc6*tc\x18\x91\xc9{\xde\xf7\xbe\x8e\xff\xff\xf2\x10\x84|c\x18\xc6 tc\x18\xbc\xcf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t@`\xa8\x01G\x88\xf1\x8cc\x18\xc6\x82\x84!\x02\x10\x84L\xe3\x18\xc61$c\x18\x91\t\x8cc\x18\xc6\xa4\x84!\x02\x10\x84\x8cc\x18\xc6$$\xe79\x84\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xc0\x01\xc0`P>\x01\x1c.\x8cc\x18\xc6\xe6\xff\xff\xf79\xcet\\\xe79\xc0s\x9c\xe7\x13\x96{\xde\xf7\xbdLs\x9c\xe79\xcet\\\xe79\xc0CZ\xd6\xb9\xce\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',

            # AiP31068L-002 EUROPEAN_RUSSIAN CHARACTER FONT
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x14\xa2a\x8c\x12\x00\x00\x00\x00q\x1d\xf1|\xdfs\x80\x01\x01\x0es\xbc\xee\x7f\xee\x8b\x8f\x18F.\xf3\xbc\xff\xc61\x8c\x7f\xc08\x80@ \x00\x80\xc0\x81\x05\x06\x00\x00\x00\x00\x04\x00\x00\x00\x01{\xdc \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xd5_EO\xfcI\x1a\xe2.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x14\xa7\xe6D!\x08@\x00\x01\x8b"#A\x11\x8cX\xc2\x00\x91\x8cc\x19B\x11\x89\x05(n1\x8cc\x02F1\x8cC\x02\t@  \x00\x81/\x80\x01\x02\x00\x00\x00\x00\x04\x00\x00\x00\x01X\xd0\xa7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8cAP\xc4\x85\x8c]\x1a\xa21\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x15\xfa\n\x88@\xaa@\x00\x02\x99\x02Ez\x01\x8cX\xc4|A\x0cc\x08\xc2\x10\x89\x05HW1\x8cc\x02F1TE\x07\n \x03\xac\xe6\xb9\x11\xb3\r"j\xce\xf3l\xeeF1\x8c\x7f[\xdd.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84=P\xce%\x8ck\x1a\xa2!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xa7\x11\x00@\x9d\xf0|\x04\xa9\x04)\x07\xc2s\xc0\x08\x00"l}\x08\xfb\xd7\xf9\x05\x88V\xb1\xf4|\xe2F5"\x89\n\x08\x00\x00s\t\xc7\x91\xc9\x05BW1\x8c\xf3\x04F5TEZG\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4 \xe7Ve\x8a\xaa\xfa\xbb\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf2\xa2\xa0@\xaaF\x00\x08\xc9\x08\x1f\x86$\x88X\xc4|D\xaf\xe3\x08\xc2\x11\x89\x05HFq\x85h\x12F5Q\x11\n\x88\x00\x03\xe3\x08\xfd\x0f\x89\x05\x82V1\xf3\xe0\xe4F5#\xc9{\xdd\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8c9P\xe6\xa5\x89*\x1a\xa6\xa1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xafN@!\x08B\x01\x90\x89\x11\x11F$\x88\x98B\x00\x80\xacc\x19B\x11\x89%(F1\x84\xa4\x12EU\x89!\x07\x08\x00\x04c\x18\xc1\x01\x89%BF1\x80`\x14\xcdUPP\x00\x00\x9e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8c!P\xc75\x8a\x1c\x1a\xa6\xb1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xa2\r\xa0\x12\x00\x04\x01\x80s\xbe\xe19\xc4s\x00\x81\x01\x04t|\xee~\x0f\x8b\x99\x1f\xc6.\x83c\xe28\x8a\x89?\xc28\x1f\x03\xfc\xe7\xb9\x0e\x8b\x99\'F.\x80a\xe34\x8a\x8b\xbe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4=_F)\x8c\x08\x1f\xbb.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x93\xc6\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xb9\x10d\x00\x00\n\x02\x8e\xf9\t\x00\xc2\x00|j\x00\x00\x02RD\x05\x10\x00\x8cc\x88\xe1\x08 \x04A\x19\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xacX\x00\x00\x00\x02\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9d\x00\x8a\x00\x00\x00m\x04S\x89$\xc7\x80,j\x02\x00\x04\x05\x88\x009N\x94\xa4\x8f\x82\x8es\\\xe9&\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xaca\xcf\xba\xbe\x89$\xf8\xc7\xff\x8dq\x18:O!\x01+\x10\x88\x00\x00\x0e\xba\xa4UIf\xd6&,j\xf2F\xa0\x00\x1c\xe58\x11\xad\xef\x88\x8f\x88 \x04E\x12\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xeb\xfd(\xc6\xa1\x9ch]\xc6$\x8dQ\x18F\xb1L\x80\t!\xde\x00\x14\xa1\x10DQ\t\xff\xfcF,jWF\xa0\x00#\x05:1ZR\x9f\x82\xaf\xff}\xf3)\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa9c\xc8}\xc6\xac\xf0Z\xfe$}]\x9e\x1f\xaf\x92R\x03\xc0\x88\x01\x14\xa28\x84Q+f\xd4\x80Lj\x9a\xc6\xa0\x00?\x15|\x11\xbc\xe7\xb8\xb0( \x04E(\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xaac(B\xa1\xcdiX\xc6$\rSYF\xa5L\xa4\x02\xc4\x88!\x00\x04m\x04Q\x1d$\xc5\x00\x8ck\x1a\xc6\xa0\x00 \xe1\x11N\x08H\x7f\x80\xaes\\\xe9\x10\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x94]\xc8:\xbe\x8ed\x98\xc6$\x0f\xdd\x9e:I!6\x03\xbb\x0f!\x1c\xa8\x02\x0e\xf9\t\x00\xc2\x00\xff\xff\xf7\x7f\xe0\x00\x1cF\x00\x00\x01\xce\x18\x81\xe8 \x84AH\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88C\x12\x04 \x00\x00\xc0\x00\x00\x00\x00\x10\x00\x9cq\xce\x03\xb0\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',

            # AiP31068L-003 WESTERN EUROPEAN CHARACTER FONT
            b' > \x92\x04\x0c\x000\x03\x9c\x01\x14\xa2a\x8c\x12\x08\x00\x00\x00q\x1d\xf1|\xdfs\x80\x01\x01\x0eq<\xee\x7f\xee\x8b\x9f\x18F.\xf3\xbc\xef\xc61\x8c\x7f\xc08\x800 \x00\x80`\x81\x04\x86\x00\x00\x00\x00\x02\x00\x00\x00\x002a\x00x\x04E \x80"\x90\xa2!D\x10\x1e@ \x88TT\xd6\xb9\xc4\x10\x84"\x1a<\x11\x1a\xd6\xb4 \'\xe2A\x11\x04\x12\x14P\x00\x84\x01\x14\xa7\xe6D!*@\x00\x01\x8b"#A\x11\x8cX\xc2\x00\x91\x8a\xa3\x19B\x11\x89\x05(n1\x8cc\x12F1\x8cC\x08\t@  \x00\x80\x80\x80\x00\x82\x00\x00\x00\x00\x02\x00\x00\x00\x00B\x12\xa4\x82\x88\xa0\x10\x00P\x08\x05\x10\n (\xa5\x11D\x03\x81)\x06 !\x08G\xa5R(%)I\xc2\xf8"A\x11\x04!(@#\x9c\x01\x15\xfa\n\x88@\x9c@\x00\x02\x99\x02Ez\x01\x8cX\xc4|A\xbcc\x08\xc2\x10\x89\x05HW1\x8cc\x02F1R\x85\x04\n \x13\xbc\xf7\xb8\x8f\xb3\x0c\x92j\xce\xf3\xd6\xef\xc61\x8c~B\x10D\x80\x1c\xe79\xces\x9c\xc0\x00\x84\xfe\xa8\x00\x00\x00\x8cb\x00>$p\x00\n#\xfc \x00g\x02n\'\xd2B\x10\x84!\x00O\xd6\x04\x01\x00\xa7\x11\x00@\x89\xf0|\x04\xa9\x04)\x07\xc2s\xc0\x08\x00"\xac}\x08\xfb\xd7\xf9\x05\x88V\xb1\xf4|\xe2F5!\t\x02\x08\x00\x00c\x08\xc7\xf1\xc9\x04\xa2W1\x8cY\x02F1TD\x82\x08\n\x84b\x10\x840\x8cbF1N\x81~\xe7:1\x8ccl\xc6(\x0b\x1d\x1ax\x92q\x1c\x18\xba\xb5 \x10\x82\x10\x84!\x14@W\x9c\x00\x01\xf2\xa2\xa0@\x9cF\x00\x08\xc9\x08\x1f\x86$\x88X\xc4|D\xbf\xe3\x08\xc2\x11\x89\x05HFq\x85h\x12F5Q\x11\x01\x08\x00\x03\xe3\x08\xfc\x8f\x89\x04\xc2V1\xf3\xd0\xe2F5#\xc8B\x10\n|~\xf7\xbd\xf0\xff\xfeB\x121\xf3\xe9\x18\xc61|c\x9a\xbd\xd0y#\x1a#\xf7!"\xf8\xc75\x07\xd0\x82\x10\x84!(O\x88\x00\x00\x00\xafN@!*B\x01\x90\x89\x11\x11F$\x88\x98B\x00\x80\x84c\x19B\x11\x89%(F1\x84\xa5\x12EU\x89!\x00\x88\x00\x04c\x08\xc0\x81\x89$\xa2F1\x80P\x12MUPPB\x10\x11\x14\xe1\x18\xc6/\x84 B\x13\xff\x85)\x18\xc6s\x0cc\x19\x80\x11\x89#7\xa0\x92\xa1?\x18\xc5\xce\xf8\x08\x92\x10\x84!\x00@\x00\x00\x01\x00\xa2\r\xa0\x12\x08\x04\x01\x80s\xbe\xe19\xc4s\x00\x81\x01\x04t|\xee~\x0f\x8b\x99\x1f\xc6.\x83b\xe28\x8a\x89?\xc08\x1f\x03\xfc\xf7\xb8\x8e\x8b\x98\x97F.\x80Q\xe1\xb4\x8a\x8b\xbe2`\x1fs\\\xf7\xbd\xe2s\x9c\xe7:1\xfb\xee\xe79\xads\x9d\x18\xff\xee{\x9c\xd2|\x93A"\xf7:\x08\x00\t\x12\x08\x88!\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x12\x08\x88@\x81@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xf2\x04\x90\x80A\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"\x88\x81B\x00\x00\x90\x00\x08\xff\x11\x01\xf0\x90\x80\x07\xff\x00\x81\xce\xf9\x1c\xff\x81\xc4\xff\xfe\xa7U\xc0`\x0c\x0f\x81\x80\x03\x00\x0f\x80\x00\x00\x00\x00\x00\x00\xf0~\x1f\x83\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14BJ\x91!\x08Z\x08\x80)\x01\x10\xb8\x84$\x03\x00\x82{!!\xd8\x86$\x8a\x91RV \x90\x12\x01\x02@\x01\x00\x02\x00\x00\x00\x00\x00~\x01\xf9~X\x831\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00V\xaa\x02\x04\xa5|\x80!\x15"\xd4\x82D\x03\x00\x82\xb5\'\xdd\xd8\x0e*\x02\x89WV-\x94H\xf2ZDI%4}\xcf\xfc\xb2E\x7f\x87\xdap8\x82\xf5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa4\xf9\tB\x90\x80!+D\x90\x9f\xfc\x03\x00\xb2w\x89\x02\xd8\x17\xear\x84J\xd62\xb2\x9d\x04\'\xc4Q%\x13\xaa2$KX\xbb\xff\xff\xfd\xf8\xfe1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xea\x00\x90\xa5~\x80!+\x8f\x92\xa2D\x03\x00\xb2\xb5\xd9\x1cX&1\x02\x88J\xb9R\x8a\xa3\xe8&Db\xa5$*2$MX\xbb\x87\xf2|8\xff\xb7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c1 \x00Z!\x80%\x15\x04\x11\xc4$\x03\xff\x82\xbb\xa9"XF1\x8a\x90G\x11R\x89#\x08&DR\xa5H*2,\x8dZ\x92\x01\xd9pX\x82w\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xfe\x00 \x80"\x00\x02\x10\x80\x00\x00\x00\x01\xce\x89\x1cX}\xd1\xfa\xbeB\x13m\xb1\x1c\xf7%\x83Lz\x88O\xcc\x13\x18\xe5\x10\x00\xd8p\x1f\x83\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x82\x00\x00\x84\x00\x00 \x07\x02\x00\x00\x18@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x82\x00\x00\x84\x00\x00 \x00\x82\x00\x00(@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x01\x00\x00\x00&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',

            # 901 FRENCH, POLISH AND SILESIAN ACCENTED CHARACTERS
            # Horizontally-aligned to A00, AiP-002 & AiP-003
            # Intended to be combined with existing fonts
            b'@\x90E\x10\x0f\x02\x08\xa7\x01@!\x08\xa0)T\x01\x14\x008\x80\x00?\xff\x80\x14TA\x17\x00\x00s\xa1\x089\xd6\xacc\x18\xb9\xc0\x8c}\xef\x10\x94\xbcb\xa8\xc6 \xff\xe1\x08\x10\x94\xa4bH\xc6 \x8c\x7f\xff\xb9\xcf{\x9cG9\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p~\x81\x08B \x04\x06\x08\x84\x88\xa0\x82\x10\x84\x00\x08\x02\x11J\x8b\xe0\xa8\xb9\xdf\xfb\x9c\xe2X\x84\x8c<\xcc\xc6\x02\x10a\x13f1\xfc!\x8a\xc5\xc4#\xe1\xf6F1\x8c$\x89\xc4(Dc\x02F3\xab\xfe\xf8\xbb\xdf\xfb\xdc\xe7E\xcd\x10\x04\x00\x00\x00\x00\x80@\x00\x00\x08\x02\x00\x00\x00\x00@ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        ]
    }
    # Replicate A00 data to support making 5x10 version
    FONTDATA['mappings'].append(FONTDATA['mappings'][0])
    FONTDATA['fonts'].append(FONTDATA['fonts'][0])
    FONTDATA['metrics'].append(dict(FONTDATA['metrics'][0]))
    FONTDATA['metrics'][5]['name'] = 'A00_5x10'
    FONTDATA['metrics'][5]['glyph_size'] = (5, 10)

    # Replicate A02 data to support making 5x10 version
    FONTDATA['mappings'].append(FONTDATA['mappings'][1])
    FONTDATA['fonts'].append(FONTDATA['fonts'][1])
    FONTDATA['metrics'].append(dict(FONTDATA['metrics'][1]))
    FONTDATA['metrics'][6]['name'] = 'A02_5x10'
    FONTDATA['metrics'][6]['glyph_size'] = (5, 10)

    # Replicate AiP31068L-002 data to support making 5x10 version
    FONTDATA['mappings'].append(FONTDATA['mappings'][2])
    FONTDATA['fonts'].append(FONTDATA['fonts'][2])
    FONTDATA['metrics'].append(dict(FONTDATA['metrics'][2]))
    FONTDATA['metrics'][7]['name'] = 'AiP-002_5x10'
    FONTDATA['metrics'][7]['glyph_size'] = (5, 10)

    # Replicate AiP31068L-003 data to support making 5x10 version
    FONTDATA['mappings'].append(FONTDATA['mappings'][3])
    FONTDATA['fonts'].append(FONTDATA['fonts'][3])
    FONTDATA['metrics'].append(dict(FONTDATA['metrics'][3]))
    FONTDATA['metrics'][8]['name'] = 'AiP-003_5x10'
    FONTDATA['metrics'][8]['glyph_size'] = (5, 10)

    # Replicate 901 data to support making 5x10 version
    FONTDATA['mappings'].append(FONTDATA['mappings'][4])
    FONTDATA['fonts'].append(FONTDATA['fonts'][4])
    FONTDATA['metrics'].append(dict(FONTDATA['metrics'][4]))
    FONTDATA['metrics'][9]['name'] = '901_5x10'
    FONTDATA['metrics'][9]['glyph_size'] = (5, 10)
