# Word Counter API

We're excited to announce the launch of our first free and open-source ChatGPT plugin that serves a useful purpose!

## What Does It Do?
This plugin is designed for counting characters and words in a given text.

## Why Create This Plugin?
ChatGPT's base model isn't always great at accurately counting characters and words, so we created this plugin to address that need.

## Use Cases
- Check the word count of your essays or articles.
- Verify the character count of your tweets to ensure they fit within the limit.
- Use this plugin as a template to create your own ChatGPT plugins.

## Demo Video
Check out this [demo video on Twitter](https://twitter.com/ykdojo/status/1646060716833783808) to see how you might want to use the Word Counter API plugin.

## Setup and Run

1. Navigate to the root directory of the Word Counter API.

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

   or

   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the FastAPI application:
   ```
   uvicorn server:app --reload
   ```

The application will be accessible at "http://localhost:8000/".

## How It Works

The Word Counter API is a FastAPI application that serves as a ChatGPT plugin. It provides an endpoint `/count` that counts characters and words in a given text when accessed.

The main code for the application is in the `server.py` file. Here's a snippet of the code that defines the `/count` endpoint:

```python
@app.post("/count")
def count_characters_and_words(data: TextData):
    text = data.text
    character_count = len(text)
    word_count = len(text.split())
    return {
        "character_count": character_count,
        "word_count": word_count
    }
```

When a user accesses the `/count` endpoint and provides text data, the application returns a JSON response containing the character count and word count.

## Setting Up the Plugin with ChatGPT

To set up the Word Counter API as a ChatGPT plugin, follow these steps:

1. Go to the "Develop your own plugin" section of the ChatGPT API documentation.

2. Input the localhost URL of the Word Counter API (e.g., "http://localhost:8000/") to set it up as a plugin.

3. Once the plugin is set up, you can interact with it through ChatGPT. For example, you can send the message "count characters and words in 'Hello, world!'" to ChatGPT, and it will return the character count and word count provided by the Word Counter API.
