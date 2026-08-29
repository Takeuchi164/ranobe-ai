
import streamlit as st
import openai
st.title("ラノベに詳しい書店員アプリ")
# AzureポータルからコピーしたAPIキーとエンドポイントを貼り付けます。
API_KEY = ""
ENDPOINT = ""
# OpenAI APIを呼び出すためのパラメタを設定します。
openai.api_type="azure"
openai.api_key = API_KEY
openai.api_base = ENDPOINT
openai.api_version = "2024-12-01-preview"
# ユーザーからの入力を受け付けます。
user_input = st.text_area("好きなマンガやアニメ、ゲームのタイトルを入力してください。")
if st.button("送信"):
# 送信ボタンが押されたら・・・
# Open AI にリクエストを送信して処理を実行させます。
    user_input = f"{user_input} が好きです。おすすめのライトノベルを教えてください。"
    response = openai.ChatCompletion.create(
    engine = "gpt-4o", 
    # 使用するモデルを指定
    messages=[{"role": "user", "content": user_input}]
    )
    # 戻ってきたレスポンスデータの中身を画面に表示します。
    st.write("AIの応答:", response["choices"][0]["message"]["content"])