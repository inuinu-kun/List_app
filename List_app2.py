import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ページのタイトル 以下は入力フォーム
st.title('表出力アプリ')
st.write('csvファイル専用の表出力WEBアプリです 左端がＸ軸 それ以降の右の数値がＹ軸になります。数字のみのファイルなら表題やラベル、凡例を付けられます。')

ward=st.text_input('表題', placeholder='表題を入れてください', max_chars=20,key=1)#keyは識別子

ygraph=st.text_input('Y軸の名前', placeholder='Y軸の名前を入れてください', max_chars=20,key=2)


ylimm=st.text_input('データ1の名前',placeholder='データ1の名前を入力してください',key=3)
ylimm2=st.text_input('データ2の名前',placeholder='データ2を使う場合は入力してください',key=4)

xgraph=st.text_input('X軸の名前', placeholder='X軸の名前を入れてください', max_chars=20,key=5)


# ファイルアップローダーの準備
uploaded_file = st.file_uploader("CSVファイルのアップロード 折れ線グラフの作成", type="csv",key=6)

# uploadファイルが存在するときだけ、csvファイルの読み込みがされる。
if uploaded_file is not None:
    # CSVファイルからデータを抽出
    xmoth,ymoth = np.loadtxt(uploaded_file, comments='#', delimiter=',', usecols=None, unpack=True)
    st.balloons()#アップロードされると風船を飛ばす
    

    # matplotlibで図を用意する
    fig = plt.figure()
    plt.plot(xmoth,ymoth,marker='.', markersize=10,label=ylimm)#xmoth,ymothはファイルの数値を受ける引数、labelは凡例
    plt.xlim()
    plt.ylim()
    plt.title(ward, fontsize=15,fontname='MS Mincho')
    plt.xlabel(xgraph, fontsize=10,fontname='MS Mincho')
    plt.ylabel(ygraph, fontsize=10,fontname='MS Mincho',labelpad=15,rotation=360)
    plt.legend(prop = {'family' : 'MS Gothic'})#凡例を表示
   
    # streamlit plot
    st.pyplot(fig)


uploaded_file = st.file_uploader("CSVファイルのアップロード 二つの折れ線グラフの作成", type="csv",key=7)

# uploadファイルが存在するときだけ、csvファイルの読み込みがされる。
if uploaded_file is not None:
    # CSVファイルからデータを抽出
    xmoth,ymoth,ymoth2 = np.loadtxt(uploaded_file, comments='#', delimiter=',', usecols=None, unpack=True)
    st.balloons()

    # matplotlibで図を用意する
    fig = plt.figure()
    plt.plot(xmoth,ymoth,marker='.', markersize=10,label=ylimm)#1つ目の折れ線グラフ
    plt.plot(xmoth,ymoth2,marker='.',markersize=10,label=ylimm2)#2つ目の折れ線グラフ
    plt.xlim()
    plt.ylim()
    plt.title(ward, fontsize=15,fontname='MS Mincho')
    plt.xlabel(xgraph, fontsize=10,fontname='MS Mincho')
    plt.ylabel(ygraph, fontsize=10,fontname='MS Mincho',labelpad=15,rotation=360)
    plt.legend(prop = {'family' : 'MS Gothic'})
    
    # streamlit plot
    st.pyplot(fig)
    
uploaded_file = st.file_uploader("CSVファイルのアップロード 棒グラフの作成", type="csv",key=8)#棒グラフの作成

if uploaded_file is not None:
    # CSVファイルからデータを抽出
    xmoth,ymoth = np.loadtxt(uploaded_file, comments='#', delimiter=',', usecols=None, unpack=True)
    st.balloons()

    # matplotlibで図を用意する
    fig = plt.figure()
    plt.bar(xmoth, ymoth,label=ylimm)
    plt.xlim()
    plt.ylim()
    plt.title(ward, fontsize=15,fontname='MS Mincho')
    plt.xlabel(xgraph, fontsize=10,fontname='MS Mincho')
    plt.ylabel(ygraph, fontsize=10,fontname='MS Mincho',labelpad=15,rotation=360)
    # legendで凡例表示
    plt.legend(prop = {'family' : 'MS Gothic'})

    # streamlit plot
    st.pyplot(fig)

uploaded_file = st.file_uploader("CSVファイルのアップロード 二本の棒グラフの作成", type="csv",key=9)

if uploaded_file is not None:
    # CSVファイルからデータを抽出
    xmoth,ymoth,ymoth2 = np.loadtxt(uploaded_file, comments='#', delimiter=',', usecols=None, unpack=True)
    st.balloons()


    # matplotlibで図を用意する
    fig = plt.figure()
    # 棒グラフをずらして表示
    plt.bar(np.array(xmoth)-0.15, ymoth,color="skyblue" ,width=0.3, label=ylimm)
    
    plt.bar(np.array(xmoth)+0.15, ymoth2,color="red" ,width=0.3, label=ylimm2)
    
    plt.xlim()
    plt.ylim()
    plt.title(ward, fontsize=15,fontname='MS Mincho')
    plt.xlabel(xgraph, fontsize=10,fontname='MS Mincho')
    plt.ylabel(ygraph, fontsize=10,fontname='MS Mincho',labelpad=15,rotation=360)
    plt.legend(prop = {'family' : 'MS Gothic'})

    # streamlit plot
    st.pyplot(fig)