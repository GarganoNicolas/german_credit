import requests

search_api_url = 'http://0.0.0.0:7860/prediction'


data = {'Age': 42,
        'Sex': 'female',
        'Job': 'skilled',
        'Housing': 'rent',
        'Saving_accounts': 'rich',
        'Checking_account': 'rich',
        'Credit_amount': 409,
        'Duration': 12,
        'Purpose': 'radio/TV'}




response = requests.post(search_api_url, json=data)
print(response.json())

#response = requests.get('http://0.0.0.0:7860/prediction')
#print(response.json())

#response = requests.get('http://0.0.0.0:7860/')
#print(response.json())

