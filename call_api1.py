import requests

search_api_url = 'http://0.0.0.0:7860/prediction'


data = {'Age': 45,
        'Sex': 'male',
        'Job': 'skilled',
        'Housing': 'free',
        'Saving_accounts': 'little',
        'Checking_account': 'little',
        'Credit_amount': 7882,
        'Duration': 42,
        'Purpose': 'furniture/equipment'}




response = requests.post(search_api_url, json=data)
print(response.json())

#response = requests.get('http://0.0.0.0:7860/prediccion')
#print(response.json())

#response = requests.get('http://0.0.0.0:7860/')
#print(response.json())

#response = await requests.get('http://127.0.0.1:8000/edvai')
#print(response.json())