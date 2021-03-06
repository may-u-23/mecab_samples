# mecab_samples

# 概要
- MeCabのサンプルスクリプト
- 入力された文章を形態素解析する

![mecab-python3_sample](https://user-images.githubusercontent.com/56919784/97726975-2b512980-1b13-11eb-8a0d-056da11da3f2.gif)

```
❯ ./mecab-python3_sample.py
>或る水族館の水槽で、ひさしい間、飢ゑた蛸が飼はれてゐた。
 BOS/EOS,*,*,*,*,*,*,*,*
或 連体詞,*,*,*,*,*,或,アル,アル
る 助動詞,*,*,*,文語・リ,体言接続,り,ル,ル
水族館 名詞,一般,*,*,*,*,水族館,スイゾクカン,スイゾクカン
の 助詞,連体化,*,*,*,*,の,ノ,ノ
水槽 名詞,一般,*,*,*,*,水槽,スイソウ,スイソー
で 助詞,格助詞,一般,*,*,*,で,デ,デ
、 記号,読点,*,*,*,*,、,、,、
ひさしい 形容詞,自立,*,*,形容詞・イ段,基本形,ひさしい,ヒサシイ,ヒサシイ
間 名詞,一般,*,*,*,*,間,マ,マ
、 記号,読点,*,*,*,*,、,、,、
飢 名詞,一般,*,*,*,*,*
ゑた 名詞,一般,*,*,*,*,*
蛸 名詞,一般,*,*,*,*,蛸,タコ,タコ
が 助詞,格助詞,一般,*,*,*,が,ガ,ガ
飼 名詞,一般,*,*,*,*,*
はれ 動詞,自立,*,*,一段,連用形,はれる,ハレ,ハレ
て 助詞,接続助詞,*,*,*,*,て,テ,テ
ゐ 動詞,自立,*,*,一段,連用形,ゐる,ヰ,イ
た 助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
。 記号,句点,*,*,*,*,。,。,。
 BOS/EOS,*,*,*,*,*,*,*,*
```

# 動作確認環境
```
ProductName:	Mac OS X
ProductVersion:	10.15.6
BuildVersion:	19G73

mecab: stable 0.996 (bottled)
mecab-ipadic: stable 2.7.0-20070801 (bottled)
mecab-python3: 1.0.2
```

# 事前作業
## Mecabのインストール
```
❯ brew install mecab
❯ brew install mecab-ipadic
```

## mecab-python3のインストール
```
❯ pip3 install mecab-python3
```

# 実行方法
## 実行権限付与
```
chmod u+x mecab-python3_sample.py
```

## 実行
```
❯ ./mecab-python3_sample.py
```
