#Importando a biblioteca feedparser para fazer a leitura das notícias do feed RSS
import feedparser

#Depositando o URL do RSS 
feed_url = 'https://www.ifpb.edu.br/ifpb/pedrasdefogo/noticias/todas-as-noticias-do-campus-pedras-de-fogo/RSS'

#fazendo parser do feed e armazenando na variável feed
feed = feedparser.parse(feed_url)

#Checando se atualização com a função published_parsed que compara os dados de publicação das últimas entradas com as novas
if 'published_parsed' in feed.feed:
    last_checked = feed.feed.published_parsed
else:
    last_checked = None

#Criando uma lista vazia para guardar as novas entradas (atualizações do feed)
new_entries = []

#Iterando sobre as novas entradas no feed com a função 'feed.entries'
#entry = cada entrada do feed em cada iteração
#No if verifico se 'last_checked' (ultima checagem) é None ou se a data de publicação de 'entry.published_parsed' é maior que o horário da última verificação feita (last_checked)
#Se alguma das condições for verdadeiras, a entrada é uma nova atualização do feed, então é adiciono em 'new_entries' 
for entry in feed.entries:
    if last_checked is None or entry.published_parsed > last_checked:
        new_entries.append(entry)
