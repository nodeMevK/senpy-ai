1. PACKAGES
    1. `pip install anthropic`
    2. `pip install tweepy`
    3. `pip install ollama`
    4. `pip install twitter-api-client`
    5. `pip install pandas`
    6. `pip install Flask-SQLAlchemy`
    7. `pip install psycopg2`
    8. `pip install psycopg2-binary`

2. Download Ollama for your machine `https://ollama.com/download`
    - `ollama run {model}` to download and run model

    - make sure ollama version is >=0.5.7

3. Psql Version: 16.4
    - `psql -U postgres` - for windows
    - have to run this in powershell to see empjis i guess `chcp 65001`
    - to go back to regular encoding use `chcp 437` or `chcp 1252`
    - *** Getting error in psql rn because of emojis and UTF8 drama on windows

4. Llama Version:

5. Docker:
    - setup docker soon
    - Run docker setup coming soon
    - Need to get docker to listen to ollama locally i guess or may have to do an ec2 instance (not sure yet)

6. Speech Modeling
    - Working on finding STT -> TTS options now

