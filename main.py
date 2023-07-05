import os

from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

from embedchain import App

chat_bot_app = App()

app = Flask(__name__)


def load_app():
    chat_bot_app.add("youtube_video", "https://www.youtube.com/watch?v=3qHkcs3kG44")
    chat_bot_app.add(
        "pdf_file",
        "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf",
    )
    chat_bot_app.add("web_page", "https://nav.al/feedback")
    chat_bot_app.add("web_page", "https://nav.al/agi")
    chat_bot_app.add_local(
        "qna_pair",
        (
            "Who is Naval Ravikant?",
            "Naval Ravikant is an Indian-American entrepreneur and investor.",
        ),
    )


@app.route("/", methods=["GET", "POST"])
def home():
    context = {}
    context["bot_name"] = os.environ["BOT_NAME"]
    context["query"] = ""
    context["result"] = ""
    if request.method == "POST":
        user_query = request.form["query"]
        query_result = chat_bot_app.query(user_query)
        context["query"] = user_query
        context["result"] = query_result
    return render_template("index.html", **context)


if __name__ == "__main__":
    load_app()
    app.run(debug=False, port=8000)
