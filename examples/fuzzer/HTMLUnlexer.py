# Generated by Grammarinator 17.5r

from itertools import chain
from grammarinator.runtime import *

charset_0 = list(chain(*multirange_diff(printable_unicode_ranges, [(60, 61)])))
charset_1 = list(chain(range(32, 33), range(9, 10), range(13, 14), range(10, 11)))
charset_2 = list(chain(range(97, 103), range(65, 71), range(48, 58)))
charset_3 = list(chain(range(48, 58)))
charset_4 = list(chain(range(58, 59), range(97, 123), range(65, 91)))
charset_5 = list(chain(range(32, 33)))
charset_6 = list(chain(range(48, 58), range(97, 123), range(65, 91)))
charset_7 = list(chain(range(48, 58), range(97, 103), range(65, 71)))
charset_8 = list(chain(range(48, 58)))
charset_9 = list(chain(*multirange_diff(printable_unicode_ranges, [(34, 35),(60, 61)])))
charset_10 = list(chain(*multirange_diff(printable_unicode_ranges, [(39, 40),(60, 61)])))


class HTMLUnlexer(Grammarinator):

    def __init__(self):
        super(HTMLUnlexer, self).__init__()
        self.lexer = self
        self.set_options()

    def EOF(self, *args, **kwargs):
        pass

    
    def style_sheet(self, *args, **kwargs):
        return UnlexerRule(src='')
    
    def HTML_COMMENT(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='HTML_COMMENT'))
        current += self.create_node(UnlexerRule(src='<!--'))
        if max_depth >= self.min_depths['quant_0']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='-->'))
        return current

    def HTML_CONDITIONAL_COMMENT(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='HTML_CONDITIONAL_COMMENT'))
        current += self.create_node(UnlexerRule(src='<!['))
        if max_depth >= self.min_depths['quant_1']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src=']>'))
        return current

    def XML_DECLARATION(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='XML_DECLARATION'))
        current += self.create_node(UnlexerRule(src='<?xml'))
        if max_depth >= self.min_depths['quant_2']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='>'))
        return current

    def CDATA(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='CDATA'))
        current += self.create_node(UnlexerRule(src='<![CDATA['))
        if max_depth >= self.min_depths['quant_3']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src=']]>'))
        return current

    def DTD(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='DTD'))
        current += self.create_node(UnlexerRule(src='<!'))
        if max_depth >= self.min_depths['quant_4']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='>'))
        return current

    def SCRIPTLET(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='SCRIPTLET'))
        weights = self.depth_limited_weights([1, 1], self.min_depths['alt_0'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.create_node(UnlexerRule(src='<?'))
            if max_depth >= self.min_depths['quant_5']:
                for _ in self.zero_or_more(max_depth=max_depth):
                    current += UnlexerRule(src=self.any_char())

            current += self.create_node(UnlexerRule(src='?>'))
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='<%'))
            if max_depth >= self.min_depths['quant_6']:
                for _ in self.zero_or_more(max_depth=max_depth):
                    current += UnlexerRule(src=self.any_char())

            current += self.create_node(UnlexerRule(src='%>'))
        return current

    def SEA_WS(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='SEA_WS'))
        if max_depth >= 0:
            for _ in self.one_or_more(max_depth=max_depth):
                weights = self.depth_limited_weights([1, 1, 1], self.min_depths['alt_1'], max_depth)
                choice = self.choice(weights)
                if choice == 0:
                    current += self.create_node(UnlexerRule(src=' '))
                elif choice == 1:
                    current += self.create_node(UnlexerRule(src='\t'))
                elif choice == 2:
                    if max_depth >= self.min_depths['quant_7']:
                        for _ in self.zero_or_one(max_depth=max_depth):
                            current += self.create_node(UnlexerRule(src='\r'))

                    current += self.create_node(UnlexerRule(src='\n'))

        return current

    def SCRIPT_OPEN(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='SCRIPT_OPEN'))
        current += self.create_node(UnlexerRule(src='<script'))
        if max_depth >= self.min_depths['quant_8']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='>'))
        return current

    def STYLE_OPEN(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='STYLE_OPEN'))
        current += self.create_node(UnlexerRule(src='<style'))
        if max_depth >= self.min_depths['quant_9']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='>'))
        return current

    def TAG_OPEN(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_OPEN'))
        current += self.create_node(UnlexerRule(src='<'))
        return current

    def HTML_TEXT(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='HTML_TEXT'))
        if max_depth >= 0:
            for _ in self.one_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.char_from_list(charset_0))

        return current

    def TAG_CLOSE(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_CLOSE'))
        current += self.create_node(UnlexerRule(src='>'))
        return current

    def TAG_SLASH_CLOSE(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_SLASH_CLOSE'))
        current += self.create_node(UnlexerRule(src='/>'))
        return current

    def TAG_SLASH(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_SLASH'))
        current += self.create_node(UnlexerRule(src='/'))
        return current

    def TAG_EQUALS(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_EQUALS'))
        current += self.create_node(UnlexerRule(src='='))
        return current

    def TAG_NAME(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_NAME'))
        current += self.lexer.TAG_NameStartChar(max_depth=max_depth - 1)
        if max_depth >= self.min_depths['quant_10']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += self.lexer.TAG_NameChar(max_depth=max_depth - 1)

        return current

    def TAG_WHITESPACE(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_WHITESPACE'))
        current += self.create_node(UnlexerRule(src=self.char_from_list(charset_1)))
        return current

    def HEXDIGIT(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='HEXDIGIT'))
        current += self.create_node(UnlexerRule(src=self.char_from_list(charset_2)))
        return current

    def DIGIT(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='DIGIT'))
        current += self.create_node(UnlexerRule(src=self.char_from_list(charset_3)))
        return current

    def TAG_NameChar(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_NameChar'))
        weights = self.depth_limited_weights([1, 1, 1, 1, 1, 1, 1, 1], self.min_depths['alt_2'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.lexer.TAG_NameStartChar(max_depth=max_depth - 1)
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='-'))
        elif choice == 2:
            current += self.create_node(UnlexerRule(src='_'))
        elif choice == 3:
            current += self.create_node(UnlexerRule(src='.'))
        elif choice == 4:
            current += self.lexer.DIGIT(max_depth=max_depth - 1)
        elif choice == 5:
            current += self.create_node(UnlexerRule(src='\u00B7'))
        elif choice == 6:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(768, 879))))
        elif choice == 7:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(8255, 8256))))
        return current

    def TAG_NameStartChar(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='TAG_NameStartChar'))
        weights = self.depth_limited_weights([1, 1, 1, 1, 1, 1], self.min_depths['alt_3'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.create_node(UnlexerRule(src=self.char_from_list(charset_4)))
        elif choice == 1:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(8304, 8591))))
        elif choice == 2:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(11264, 12271))))
        elif choice == 3:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(12289, 55295))))
        elif choice == 4:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(63744, 64975))))
        elif choice == 5:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(65008, 65533))))
        return current

    def SCRIPT_BODY(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='SCRIPT_BODY'))
        if max_depth >= self.min_depths['quant_11']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='</script>'))
        return current

    def SCRIPT_SHORT_BODY(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='SCRIPT_SHORT_BODY'))
        if max_depth >= self.min_depths['quant_12']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='</>'))
        return current

    def STYLE_BODY(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='STYLE_BODY'))
        current += self.style_sheet()
        current += self.create_node(UnlexerRule(src='</style>'))
        return current

    def STYLE_SHORT_BODY(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='STYLE_SHORT_BODY'))
        current += self.style_sheet()
        current += self.create_node(UnlexerRule(src='</>'))
        return current

    def ATTVALUE_VALUE(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='ATTVALUE_VALUE'))
        if max_depth >= self.min_depths['quant_13']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += self.create_node(UnlexerRule(src=self.char_from_list(charset_5)))

        current += self.lexer.ATTRIBUTE(max_depth=max_depth - 1)
        return current

    def ATTRIBUTE(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='ATTRIBUTE'))
        weights = self.depth_limited_weights([1, 1, 1, 1, 1], self.min_depths['alt_4'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.lexer.DOUBLE_QUOTE_STRING(max_depth=max_depth - 1)
        elif choice == 1:
            current += self.lexer.SINGLE_QUOTE_STRING(max_depth=max_depth - 1)
        elif choice == 2:
            current += self.lexer.ATTCHARS(max_depth=max_depth - 1)
        elif choice == 3:
            current += self.lexer.HEXCHARS(max_depth=max_depth - 1)
        elif choice == 4:
            current += self.lexer.DECCHARS(max_depth=max_depth - 1)
        return current

    def ATTCHAR(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='ATTCHAR'))
        weights = self.depth_limited_weights([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], self.min_depths['alt_5'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.create_node(UnlexerRule(src='-'))
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='_'))
        elif choice == 2:
            current += self.create_node(UnlexerRule(src='.'))
        elif choice == 3:
            current += self.create_node(UnlexerRule(src='/'))
        elif choice == 4:
            current += self.create_node(UnlexerRule(src='+'))
        elif choice == 5:
            current += self.create_node(UnlexerRule(src=','))
        elif choice == 6:
            current += self.create_node(UnlexerRule(src='?'))
        elif choice == 7:
            current += self.create_node(UnlexerRule(src='='))
        elif choice == 8:
            current += self.create_node(UnlexerRule(src=':'))
        elif choice == 9:
            current += self.create_node(UnlexerRule(src=';'))
        elif choice == 10:
            current += self.create_node(UnlexerRule(src='#'))
        elif choice == 11:
            current += self.create_node(UnlexerRule(src=self.char_from_list(charset_6)))
        return current

    def ATTCHARS(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='ATTCHARS'))
        if max_depth >= 0:
            for _ in self.one_or_more(max_depth=max_depth):
                current += self.lexer.ATTCHAR(max_depth=max_depth - 1)

        if max_depth >= self.min_depths['quant_14']:
            for _ in self.zero_or_one(max_depth=max_depth):
                current += self.create_node(UnlexerRule(src=' '))

        return current

    def HEXCHARS(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='HEXCHARS'))
        current += self.create_node(UnlexerRule(src='#'))
        if max_depth >= 0:
            for _ in self.one_or_more(max_depth=max_depth):
                current += self.create_node(UnlexerRule(src=self.char_from_list(charset_7)))

        return current

    def DECCHARS(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='DECCHARS'))
        if max_depth >= 0:
            for _ in self.one_or_more(max_depth=max_depth):
                current += self.create_node(UnlexerRule(src=self.char_from_list(charset_8)))

        if max_depth >= self.min_depths['quant_15']:
            for _ in self.zero_or_one(max_depth=max_depth):
                current += self.create_node(UnlexerRule(src='%'))

        return current

    def DOUBLE_QUOTE_STRING(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='DOUBLE_QUOTE_STRING'))
        current += self.create_node(UnlexerRule(src='"'))
        if max_depth >= self.min_depths['quant_16']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.char_from_list(charset_9))

        current += self.create_node(UnlexerRule(src='"'))
        return current

    def SINGLE_QUOTE_STRING(self, *, max_depth=float('inf')):
        current = self.create_node(UnlexerRule(name='SINGLE_QUOTE_STRING'))
        current += self.create_node(UnlexerRule(src='\''))
        if max_depth >= self.min_depths['quant_17']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += UnlexerRule(src=self.char_from_list(charset_10))

        current += self.create_node(UnlexerRule(src='\''))
        return current

    def set_options(self):
        self.options = dict(tokenVocab="HTMLLexer", dot="any_unicode_char")

    min_depths = {'TAG_EQUALS': 0, 'SCRIPT_OPEN': 0, 'alt_0': [0, 0], 'DIGIT': 0, 'SINGLE_QUOTE_STRING': 0, 'ATTVALUE_VALUE': 2, 'quant_0': 0, 'TAG_SLASH': 0, 'quant_11': 0, 'alt_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'DTD': 0, 'HEXCHARS': 0, 'alt_2': [1, 0, 0, 0, 1, 0, 0, 0], 'TAG_NameChar': 0, 'TAG_OPEN': 0, 'ATTCHAR': 0, 'quant_6': 0, 'quant_1': 0, 'XML_DECLARATION': 0, 'quant_13': 0, 'quant_5': 0, 'quant_15': 0, 'quant_14': 0, 'quant_4': 0, 'TAG_WHITESPACE': 0, 'HTML_TEXT': 0, 'quant_10': 1, 'STYLE_OPEN': 0, 'HTML_COMMENT': 0, 'quant_12': 0, 'SEA_WS': 0, 'alt_1': [0, 0, 0], 'DOUBLE_QUOTE_STRING': 0, 'HEXDIGIT': 0, 'quant_7': 0, 'TAG_SLASH_CLOSE': 0, 'CDATA': 0, 'quant_3': 0, 'quant_2': 0, 'ATTCHARS': 1, 'alt_4': [1, 1, 2, 1, 1], 'alt_3': [0, 0, 0, 0, 0, 0], 'STYLE_BODY': 0, 'TAG_NameStartChar': 0, 'quant_16': 0, 'SCRIPT_BODY': 0, 'quant_8': 0, 'SCRIPTLET': 0, 'HTML_CONDITIONAL_COMMENT': 0, 'TAG_CLOSE': 0, 'SCRIPT_SHORT_BODY': 0, 'ATTRIBUTE': 1, 'TAG_NAME': 1, 'quant_17': 0, 'STYLE_SHORT_BODY': 0, 'DECCHARS': 0, 'quant_9': 0}

