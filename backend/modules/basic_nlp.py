# basic nlp module

# 形態素解析
# ストップワードの除去
# htmlタグの除去

import sys, pathlib
from pyknp import Jumanpp
import mojimoji
# midasi, yomi, genkei, hinsi, bunrui, katuyou1, katuyou2, imis, repname

class MorphAnalysis:
    def __init__(self):
        self.stop_path = str(pathlib.Path(__file__).resolve().parent) + '/data/stopwords_slothlib.txt'
        self.stopwords = []
        with open(self.stop_path, 'r') as f:
            self.stopwords = f.read().split()

        # 形態素解析
        self.jumanpp = Jumanpp()

    def to_wakati(self, text,
                  allow_word_class=['名詞', '指示詞', '動詞', '形容詞', '判定詞', '助動詞', '副詞',
                                    '助詞', '接続詞', '連体詞', '感動詞', '接頭辞', '特殊', '未定義語'],
                  remove_stopwords=False, genkei=False):
        wkt = ""
        text = mojimoji.han_to_zen(text)
        rst = self.jumanpp.analysis(text)
        for mrph in rst.mrph_list():
            if remove_stopwords and (mrph.genkei in self.stopwords):
                continue
            if mrph.hinsi in allow_word_class:
                if genkei:
                    wkt += mrph.genkei + ' '
                else:
                    wkt += mrph.midasi + ' '
        return wkt
