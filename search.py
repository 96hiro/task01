### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

import csv

# -*- coding: utf-8 -*-

# CSVファイルを開く
csv_file = open('./input.csv', 'r')
#ファイルを読み込み、値を変数に格納する
# reader = [csv.reader(csv_file)]
reader = csv_file.readlines()
source = reader
#CSVファイルを閉じる   
csv_file.close()


### 検索ツール
def searchs():

    #入力値を変数へ格納する
    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    ### ここに検索ロジックを書く
    #入力値がリストの値と一致するか判定結果をフラグとして立てる(初期値を0に設定)
    flg = 0
    
    #文字列をカンマで区切り、Listに格納する
    ColumnList = source[0].split(",")
    #Listの値と入力値が一致するかを判定する
    for culumList in ColumnList:
        #改行コードを消す
        culum = culumList.replace("\n","")
        #入力値と一致した時の処理
        if culum == word:   
            #判定フラグに１を代入
            flg = 1            
            print("{}が見つかりした".format(word))
            #for文を抜ける
            break
    #入力値と不一致だった時の処理
    if flg == 0:
    
        print("{}は見つかりませんでした".format(word))
        #値を書き込むcsvファイルを指定し開く
        with open('./output.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator="\n")
            #改行コードがある場合は削除する
            mtSouce = source[0].replace('\n','')
            #読み込んだ値の最後尾に入力値を結合する
            mtSouce += ','+word
            #csvファイルへ書き込む
            writer.writerow(mtSouce.split(','))

if __name__ == "__main__":
    
    # searchs("")
    searchs()
