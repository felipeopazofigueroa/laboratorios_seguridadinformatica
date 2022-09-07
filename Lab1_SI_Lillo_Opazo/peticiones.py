#pip install requests

import requests

def curlPost(mensajeCifrado):

    headers = {
        'Content-Type': 'text/plain',
    }

    data = '{"msg":"'+mensajeCifrado+'"}'    

    response = requests.post('https://finis.mmae.cl/SendMsg', headers=headers, data=data)
   
    print("mensaje enviado: "+data)

def curlGet():

    headers = {
        'Content-Type': 'text/plain',
    }

    response = requests.get('https://finis.mmae.cl/GetMsg', headers=headers)

    return(response.text)
