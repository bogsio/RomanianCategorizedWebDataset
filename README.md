# Romanian Categorized Web Dataset

Around 5.000 categorized and sentiment annotated Romanian web articles.

## Gathering the data

Due to copyright reasons, the data is not included in the corpus. You will need to run a Python script
in order to download and parse the text data from the URLs included in the `ro_index.csv` file.

The script is ran as follows:

```
pip install -r requirements.txt
python gather.py
```

The text data will be saved in the `./data` folder. 
The script sends the URL to a web service that downloads 
the web page contents and properly strips away the HTML tags, leaving only the cleaned text.

## Categories

- Arta si Traditii
- Astrologie
- Automobile
- Business
- Divertisment
- DIY
- Economic
- Educatie
- Familie
- Gastronomie
- Istorie
- IT&C
- Legal
- Media
- Medical
- Meteo
- Moda & Frumusete
- Monden
- Natura & Ecologie
- Politic
- Relatii si Sex
- Religie
- Sanatate
- Social 
- Sport
- Stiinta & Tehnologie
- Turism & Calatorii

## Sentiment Labels:

- Negative
- Neutral
- Positive
