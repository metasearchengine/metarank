import json, sys
from googleapiclient.discovery import build
import requests

###for google
if __name__ == '__main__':
    ###output_dir = './Desktop/'
    output_fname = "outp.json"
    search_term = str(raw_input())
    num_requests = int(raw_input())

    search_engine_id = 'custom search engine id'
    api_key = 'google api key'
    service = build('customsearch', 'v1', developerKey=api_key)
    collection = service.cse()

    output_f = open(output_fname, 'ab')

    for i in range(0, num_requests):
        start_val = 1 + (i * 10)
        request = collection.list(q=search_term,
            num=10,
            start=start_val,
            cx=search_engine_id
        )
        response = request.execute()
        output = json.dumps(response, sort_keys=True, indent=2)
        output_f.write(output)
        print('Wrote 10 search results...')
    output_f.write("\n\n\n\n\n\n\n\n\n")
    output_f.close()
    print('Output file "{}" written.'.format(output_fname)) 




####for bing
headers2 = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'bing api-key',
}

params2 = {
    'q': search_term ,
    'count': str(num_requests*10),
    'offset': '0',
    'mkt': 'en-in',
    'safesearch': 'Moderate',
}

r = requests.get("https://api.cognitive.microsoft.com/bing/v5.0/search?%s", params=params2, headers=headers2)
with open('outp.json','a+') as text1:
    text1.write(r.text.encode('utf-8').strip())