import requests

search_api_url = 'http://0.0.0.0:7860/prediction'


data = {'Age': 22,
        'Sex': 'female',
        'Job': 'skilled',
        'Housing': 'own',
        'Saving_accounts': 'little',
        'Checking_account': 'moderate',
        'Credit_amount': 5951,
        'Duration': 48,
        'Purpose': 'radio/TV'}



response = requests.post(search_api_url, json=data)
print(response.json())

#response = requests.get('http://0.0.0.0:7860/prediccion')
#print(response.json())

#response = requests.get('http://0.0.0.0:7860/')
#print(response.json())

#response = await requests.get('http://127.0.0.1:8000/edvai')
#print(response.json())