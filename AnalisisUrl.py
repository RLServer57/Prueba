import requests,json

answers = 0
noanswers = 0
maxOwners = 0
minViews = 9999

resp = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow', 'r')
data = json.loads(resp.content)

for item in data['items']:
    if item['is_answered'] == True:
        answers = answers+1
    else:
        noanswers = noanswers+1
    if item['owner']['reputation'] > maxOwners:
        maxOwners = item['owner']['reputation']
        titleOwner = item['title']
    if item['view_count'] < minViews:
        minViews = item['view_count']
        titleView = item['title']

print ('Respuestas contestadas/no contestadas: '+str(answers)+'/'+str(noanswers))
print ('Respuesta con mayor owners: '+titleOwner)
print ('Respuesta con menor views: '+titleView)

#El ultimo punto no pude resolverlo, ya que requeria saber de fechas
#Por lo que el valor de dichas fechas no pude interpretarlos
#Pero me divertí mucho haciendo este reto ya que aprendí a programar el
#lenguaje Python