#!python3
import MeCab

mecab = MeCab.Tagger()

# バグ回避
# mecab 0.996で、Python3からMeCabのparseToNode関数を使うと、最初のsurfaceが表示されないというバグがある
# その回避のため、parseToNode関数を呼び出す前に、parse関数を呼び出しておく
mecab.parse('')

text = input('>')

node = mecab.parseToNode(text)
while node:
    print(node.surface, node.feature)
    node = node.next