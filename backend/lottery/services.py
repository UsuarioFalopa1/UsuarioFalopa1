import json
from urllib import request
import requests
from datetime import date

def generate_request(url, params={}):
    response = requests.get(url, params=params)
    urls = response.url
    if response.status_code == 200:
        return response

def get_username(params={}):
    response = generate_request('https://randomuser.me/api', params)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return ''

def get_lotteries_payed_api( ):
    url = "https://loterias-y-quinielas-argentinas.p.rapidapi.com/loterias"

    headers = {
        'x-rapidapi-host': "loterias-y-quinielas-argentinas.p.rapidapi.com",
        'x-rapidapi-key': "f724a1b711msh5671c38eb2e7fecp110739jsn8bddb2999cc9"
        }
    response = generate_request(url, headers )
    if response:
       numero = response.get('results')[0]
       ''' premio = response.get('results')[1]
       timestamp =  response.get('results')[2]
       status =  response.get('results')[3]
       error =  response.get('results')[4]
       '''
       return numero.get('numero').get('first')

def get_lotteries( ):
    url = "https://api.elpais.com/ws/LoteriaNavidadPremiados"
    #?sorteo=2022/01/QNL51P20220125.xml
    params = {'n' : 'resumen' }
    response = generate_request(url, params )
    response_decode = response.content.decode()
    if response_decode:
        response_decode = response_decode.strip('premios=')
        return json.loads(response_decode)

#get_lotteries()