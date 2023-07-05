
# qna-bot-template-py

[![](https://dcbadge.vercel.app/api/server/nhvCbCtKV?style=flat)](https://discord.gg/nhvCbCtKV)

qna-bot-template-py is a frontend app created in Flask powered by [embedchain](https://github.com/embedchain/embedchain). embedchain is a framework to easily create LLM powered bots over any dataset. If you want a javascript version, check out [embedchain-js](https://github.com/embedchain/embedchainjs)

It abstracts the entire process of loading dataset, chunking it, creating embeddings and then storing in vector database.

You can add a single or multiple dataset using `.add` and `.add_local` function and then use `.query` function to find an answer from the added datasets.

If you want to create a Naval Ravikant bot which has 2 of his blog posts, as well as a question and answer pair you supply, all you need to do is add the links to the blog posts and the QnA pair and embedchain will create a bot for you.

# Getting Started

## Installation

- First make sure that you have the following installed.

* Python 3 and virtualenv

- Make sure that you have the package cloned locally, using the following commands

```bash
git clone https://github.com/embedchain/qna-bot-template-py.git
cd qna-bot-template-py
```

- Create and activate your virtual environment as follows

```bash
# For Linux Users
virtualenv -p $(which python3) pyenv
source pyenv/bin/activate

# For Windows users
virtualenv pyenv
.\pyenv\Scripts\activate
```

- Now install the required packages using

```bash
pip install -r requirements.txt
```

- We use OpenAI's embedding model to create embeddings for chunks and ChatGPT API as LLM to get answer given the relevant docs. Make sure that you have an OpenAI account and an API key. If you have don't have an API key, you can create one by visiting [this link](https://platform.openai.com/account/api-keys).

- Rename the `sample.env` to `.env` and set your environment variables. Here BOT_NAME is the name of the bot that will be displayed in your app.

```bash
OPENAI_API_KEY=""
BOT_NAME=""
```

## Usage

- Activate your virtual environment

```bash
# For Linux Users
source pyenv/bin/activate

# For Windows Users
.\pyenv\Scripts\activate
```

- Run the development server, using

```bash
python main.py
```

- Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

- By default we have setup a `Naval Ravikant Bot` app.

- Wait for the data to load completely and then ask any query using the input box and then click on Submit.

- Your answer will be displayed in the result box below.

- To customize and create your own bot app, go to `main.py` and enter your own data sources in the load_app() function in the following manner

```python
# Embed Online Resources
chat_bot_app.add("youtube_video", "https://www.youtube.com/watch?v=3qHkcs3kG44")
chat_bot_app.add("pdf_file", "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")
chat_bot_app.add("web_page", "https://nav.al/feedback")
chat_bot_app.add("web_page", "https://nav.al/agi")

# Embed Local Resources
chat_bot_app.add_local("qna_pair", ("Who is Naval Ravikant?", "Naval Ravikant is an Indian-American entrepreneur and investor."))
```

- Go to your `.env` file and change the bot name to your desired bot name using the `BOT_NAME` env variable.

- Now reload or run your app again to see the changes.

## Format supported

We support the following formats:

### Youtube Video

To add any youtube video to your app, use the data_type (first argument to `.add`) as `youtube_video`. Eg:

```python
app.add('youtube_video', 'a_valid_youtube_url_here')
```

### PDF File

To add any pdf file, use the data_type as `pdf_file`. Eg:

```python
app.add('pdf_file', 'a_valid_url_where_pdf_file_can_be_accessed')
```

Note that we do not support password protected pdfs.

### Web Page

To add any web page, use the data_type as `web_page`. Eg:

```python
app.add('web_page', 'a_valid_web_page_url')
```

### Text

To supply your own text, use the data_type as `text` and enter a string. The text is not processed, this can be very versatile. Eg:

```python
app.add_local('text', 'Seek wealth, not money or status. Wealth is having assets that earn while you sleep. Money is how we transfer time and wealth. Status is your place in the social hierarchy.')
```
Note: This is not used in the examples because in most cases you will supply a whole paragraph or file, which did not fit.

### QnA Pair

To supply your own QnA pair, use the data_type as `qna_pair` and enter a tuple. Eg:

```python
app.add_local('qna_pair', ("Question", "Answer"))
```

# How does it work?

Creating a chat bot over any dataset needs the following steps to happen

* load the data
* create meaningful chunks
* create embeddings for each chunk
* store the chunks in vector database

Whenever a user asks any query, following process happens to find the answer for the query

* create the embedding for query
* find similar documents for this query from vector database
* pass similar documents as context to LLM to get the final answer.

The process of loading the dataset and then querying involves multiple steps and each steps has nuances of it is own.

* How should I chunk the data? What is a meaningful chunk size?
* How should I create embeddings for each chunk? Which embedding model should I use?
* How should I store the chunks in vector database? Which vector database should I use?
* Should I store meta data along with the embeddings?
* How should I find similar documents for a query? Which ranking model should I use?

These questions may be trivial for some but for a lot of us, it needs research, experimentation and time to find out the accurate answers.

embedchain is a framework which takes care of all these nuances and provides a simple interface to create bots over any dataset.

In the first release, we are making it easier for anyone to get a chatbot over any dataset up and running in less than a minute. All you need to do is create an app instance, add the data sets using `.add` function and then use `.query` function to get the relevant answer.

# Tech Stack

embedchain is built on the following stack:

- [Langchain](https://github.com/hwchase17/langchain) as an LLM framework to load, chunk and index data
- [OpenAI's Ada embedding model](https://platform.openai.com/docs/guides/embeddings) to create embeddings
- [OpenAI's ChatGPT API](https://platform.openai.com/docs/guides/gpt/chat-completions-api) as LLM to get answers given the context
- [Chroma](https://github.com/chroma-core/chroma) as the vector database to store embeddings

# Author

* Taranjeet Singh ([@taranjeetio](https://twitter.com/taranjeetio))

## Maintainer

- [sahilyadav902](https://github.com/sahilyadav902)
