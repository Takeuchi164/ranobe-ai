# BookLog

「ranobe-ai」はユーザーが入力した好きなマンガやアニメなどのタイトルをもとに、**Azure OpenAI (GPT-4o)** を活用してぴったりのライトノベルを提案してくれる、Streamlit製のWebアプリケーションです。

# DEMO

好きな作品を伝えると、おすすめのライトノベルを教えてくれます。
<img width="606" height="326" alt="demo" src="https://github.com/user-attachments/assets/9e908eea-3cf8-4592-bc46-14e4fc001b0b" />


# Features

面倒な会話文を書く必要はなく、お気に入りのタイトルを伝えるだけで直感的にAIのレコメンドを受けられます。

# Requirement

* **streamlit**
* **openai**

# Installation

1. Gitからリポジトリをクローン（またはZIPをダウンロード）する
2. ライブラリをインストールする
```
pip install -r requirements.txt
```

3. アプリの起動
```
streamlit run main.py
```

# Usage

1. アプリを起動すると、ブラウザに「ラノベに詳しい書店員アプリ」の画面が表示されます。
2. テキストエリアに、**好きなマンガ、アニメ、ゲームのタイトル**を入力します。
   * *例: 「呪術廻戦」や「葬送のフリーレン」など*
3. **「送信」ボタン**をクリックすると、Azure OpenAI (GPT-4o) を通じてAI書店員がおすすめのライトノベルを考えて画面に表示してくれます

# Note

実行する前に、main.py 内の API_KEY と ENDPOINT にご自身のAzure OpenAI情報を設定してください。

# Author

* Takeuchi

# License

このプロジェクトは [MIT License](LICENSE) の下で公開されています。
