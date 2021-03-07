import requests
import json
import random

import sys



amb = sys.argv[1]
print(amb)

data = [
    {
        "image": "http://4.bp.blogspot.com/_67YWDX97X2A/TBphiiFBNKI/AAAAAAAAACc/pQ_k-F4ovCQ/s400/high04_img01.gif",
        "name": "Selo da Alma",
        "description": "Caso deseje transferir um personagem celestial entre contas você deverá utilizar o item Selo da Alma.",
        "price": "179.35",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "wyd"
    },
    {
        "image": "https://pbs.twimg.com/media/Eg7_b0IXkAk-8T7?format=png&name=360x360",
        "name": "espada gpc",
        "description": "uma espada grande pra caramba",
        "price": "9.99",
        "type_": "item",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    }, 
    {
        "image": "https://pbs.twimg.com/media/Eg7_byqXkAc8NBR?format=png&name=360x360",
        "name": "capuz da morte de rabadon",
        "description": "famoso chapeu seletor",
        "price": "9.99",
        "type_": "item",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    }, 
    {
        "image": "https://i.pinimg.com/originals/21/4b/87/214b87ab5b7ca8562b1ed6493870b5ad.jpg",
        "name": "eco de luden",
        "description": "o bastaozin roxo",
        "price": "9.99",
        "type_": "item",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    }, 
    {
        "image": "https://pbs.twimg.com/media/EPoihwqXkAA3mC7?format=png&name=360x360",
        "name": "morello",
        "description": "é o morellomanicão",
        "price": "9.99",
        "type_": "item",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://3.bp.blogspot.com/-VysH0JLMhoU/W75Tbu1VCoI/AAAAAAABI34/vJxUqXP9MzwyT1OUd3WPC_cTkBHWACUKQCLcBGAs/s1600/popstar-bag-490px.png",
        "name": "Saco de presentes kda",
        "description": "Abra para adquirir uma skin kda all out",
        "price": "35",
        "type_": "gold",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://static.wikia.nocookie.net/lolesports_gamepedia_en/images/0/0b/Skin_Loading_Screen_KDA_ALL_OUT_Kai%27Sa_Prestige_Edition.jpg",
        "name": "K/DA ALL OUT Kai'Sa Prestige Edition",
        "description": "Skin da patroa",
        "price": "9.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://static.wikia.nocookie.net/lolesports_gamepedia_en/images/1/10/Skin_Loading_Screen_KDA_ALL_OUT_Ahri.jpg",
        "name": "KDA ALL OUT Ahri",
        "description": "narutinha estilosa",
        "price": "9.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://cdn-products.eneba.com/resized-products/MdhEwswVoDD9xBwEB1iuEeKqApCMZ0C6qEzhteF0Rik_350x200_1x-0.jpeg",
        "name": "RR LIGA DAS LENDAS",
        "description": "10 bozos de RPzin",
        "price": "10",
        "type_": "gold",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://exitoina.uol.com.br/media/_versions/lol_emicida_widelg.jpg",
        "name": "Ekko True Damage",
        "description": "bora mandar um rap",
        "price": "10",
        "type_": "item",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Caitlyn_19.jpg",
        "name": "Skin Caitlyn Fliperama",
        "description": "Alvo marcado!",
        "price": "21.89",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_8.jpg",
        "name": "Skin Aatrox Lua Sangrenta EDIÇÃO DE PRESTÍGIO",
        "description": "Gold aatrox",
        "price": "45.80",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_17.jpg",
        "name": "Skin Ashe Velho Oeste",
        "description": "UUUUPI",
        "price": "30.89",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Brand_8.jpg",
        "name": "Skin Brand Dragão Eterno",
        "description": "Gold aatrox",
        "price": "45.80",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Corki_18.jpg",
        "name": "Skin Corki Corgi",
        "description": "Pega eles menino!",
        "price": "21.00",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Galio_13.jpg",
        "name": "Skin Galio Infernal",
        "description": "Queime como o Brand!",
        "price": "25.77",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Heimerdinger_6.jpg",
        "name": "Skin Heimerdinger Treinador de Dragões",
        "description": "Deita! Rola! Morde!",
        "price": "35.00",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Pantheon_16.jpg",
        "name": "Skin Pulsefire Pantheon",
        "description": "Atacaaar!",
        "price": "30.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/TwistedFate_13.jpgg",
        "name": "Skin Twisted Fate Odisseia",
        "description": "Seu destino pertence as cartas!",
        "price": "35.00",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Veigar_8.jpg",
        "name": "Skin Veigar chefão Final",
        "description": "Vou te deletar do game!",
        "price": "35.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/XinZhao_20.jpg",
        "name": "Skin Xin Zhao Defensor Cósmico",
        "description": "Minha lança carrega a vitória!",
        "price": "35.80",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Leona_11.jpg",
        "name": "Skin Leona Eclipse Lunar",
        "description": "A escolhida da lua!",
        "price": "35.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Leona_10.jpg",
        "name": "Skin Leona Eclipse Lunar",
        "description": "A escolhida da lua!",
        "price": "35.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Senna_9.jpg",
        "name": "Skin Senna True Damage EDIÇÃO DE PRESTÍGIO",
        "description": "A escolhida do sol!",
        "price": "40.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Rakan_5.jpg",
        "name": "Skin Rakan Guadião Estelar",
        "description": "Amor, cadê você?!",
        "price": "35.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Samira_1.jpg",
        "name": "Skin Samira Psyops",
        "description": "Tome bala!",
        "price": "29.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Teemo_8.jpg",
        "name": "Skin Teemo Esquadrão ômega",
        "description": "Reagrupar!",
        "price": "35.89",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server1",
        "game": "lol"
    },
    {
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Vayne_11.jpg",
        "name": "Skin Projeto Vayne",
        "description": "Tome bala!",
        "price": "29.99",
        "type_": "account",
        "salesman_uuid": random.randint(1,5),
        "server": "server2",
        "game": "lol"
    }
    
]

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTQzNTU4ODgsIm5iZiI6MTYxNDM1NTg4OCwianRpIjoiZTU2YWVjMDAtN2EwZS00OWVjLWEzMTEtZmZiNzY1ZGQwNGE0IiwiZXhwIjoxNjE0NDQyMjg4LCJpZGVudGl0eSI6eyJpZCI6MiwiZW1haWwiOiJnZW92YW5lQGdlb3ZhbmUuY29tIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.X9vIsIHl8QyvN5k9okuMcS8mK0vSUJhvoF6tYPsbCiw'
}

URL = 'https://roct-api.herokuapp.com/announcements/add' if amb=='prod' else 'http://localhost:5001/announcements/add'

for item in data:
    data_ = json.dumps(item)
    response = requests.post(URL, headers=headers, data=data_)
    print(response.__dict__)
    print(response)
