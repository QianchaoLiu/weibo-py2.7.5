# -*- coding:utf-8 -*-

__author__ = 'liuqianchao'
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import gensim






import logging
import os.path
import sys
import multiprocessing

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    input, outp1, outp2 = sys.argv[1:4]

    model = Word2Vec(LineSentence(input), size=300, window=5, min_count=5,workers=multiprocessing.cpu_count())

    # trim unneeded model memory = use(much) less RAM
    #model.init_sims(replace=True)
    model.save(outp1)
    model.save_word2vec_format(outp2, binary=False)
'''
'''
import jieba
import sys
import logging
reload(sys)
sys.setdefaultencoding('utf-8')

f=open('/Users/liuqianchao/PycharmProjects/weibo-py2.7.5/wiki.zh.text.jian.text')
file=f.read()
print '开始分词'
seg_list =jieba.cut(file, cut_all=False)
newf=" ".join(seg_list)
wt=open('new.text','w')
wt.write(newf)

'''
model = gensim.models.Word2Vec.load("wiki.zh.text.model")
result = model.most_similar(positive=(u'天气',u'不好'))
#result = model.most_similar(u'父亲')
#print model.similarity(u'狗',u'猫')
#print model[u'新华网']
#word2vec长度为400
for e in result:
    print e[0], e[1]
'''