import os
import json
import requests
import pandas as pd


SEPARATOR = "\n==========\n"


if __name__ == "__main__":
    index = pd.read_csv('ro_index.csv')
    print("[*] Dataset size: ", len(index))

    for _, row in index.iterrows():
        print("[-] Fetching URL: ", row['URL'], " ", int(row['ID']), "/", len(index))

        response = requests.get('https://boilerpipe-178618.appspot.com/demo-extract',
                                params={'url': row['URL'],
                                        'extractor': 'DefaultExtractor',
                                        'output': 'json'})
        if response.status_code == 200:
            data = json.loads(response.content.decode("utf-8", "ignore"))

            if data['success']:
                cleaned_text = data['response']['content']
                cleaned_title = data['response'].get("title", "")

                with open(os.path.join('data', "%s.txt" % row['ID']), 'w+') as f:
                    f.write(cleaned_title + SEPARATOR + cleaned_text)
                    print("[*] Fetched successfully. \n")
            else:
                print("[!] Couldn't parse page. \n")
                print(data)
                print("\n\n")
        else:
            print("[!] Couldn't successfully fetch page. \n")
            print(response.content)
            print("\n\n")





