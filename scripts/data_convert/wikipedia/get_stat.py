#!/usr/bin/env python
# This is script that obtains statistics on # of tokens & sentences
# directly from the Wikipedia dump.
import sys
import numpy as np

sys.path.append('.')

from scripts.config import SPACY_MODEL, BERT_BASE_MODEL
from pytorch_pretrained_bert import BertTokenizer
from scripts.data_convert.text_proc import SpacyTextParser
from scripts.data_convert.convert_common import wikiExtractorFileIterator, \
    SimpleXmlRecIterator, procWikipediaRecord

if len(sys.argv) != 2:
    print('Usage: <dump root dir>')
    sys.exit(1)

stopWords = []  # Currently, the list of stop-words is empty
textProcessor = SpacyTextParser(SPACY_MODEL, stopWords, sentSplit=True, enablePOS=False)

sentQtys = []
tokQtys = []
bertPieceQtys = []

tokenizer = BertTokenizer.from_pretrained(BERT_BASE_MODEL, do_lower_case=True)

for fn in wikiExtractorFileIterator(sys.argv[1]):
    for wikiRec in SimpleXmlRecIterator(fn, 'doc'):
        pw = procWikipediaRecord(wikiRec)
        print(pw.id, pw.url, pw.title)
        wikiText = pw.content
        sentList = list(textProcessor(wikiText).sents)
        tQty = 0
        for s in sentList:
            tQty += len(s)  # This includes non-word tokens, but it's ok

        sentQtys.append(len(sentList))
        tokQtys.append(tQty)
        bertToks = tokenizer.tokenize(wikiText)
        bertPieceQtys.append(len(bertToks))

print('Sentence # distribution:  ', np.quantile(sentQtys, np.arange(1, 10) / 10.0))
print('Token # distribution:     ', np.quantile(tokQtys, np.arange(1, 10) / 10.0))
print('BERT token # distribution:', np.quantile(bertPieceQtys, np.arange(1, 10) / 10.0))
