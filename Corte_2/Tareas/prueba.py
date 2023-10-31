
# def bake_time_remaining( expectec_bake_time):
#     tiempo_restante =  expectec_bake_time - elapsed_bake_time
#     return tiempo_restante


# capas = int(input('Cuantas capas quiere agregarle a la lasaña: ')) 
# def preparation_time_in_minutes(capas):
#     tiempo_por_capa = 2
#     minutos_en_preparar = capas*tiempo_por_capa
#     return minutos_en_preparar
    

# def elapsed_time_in_minutes(minutos_en_preparar,elapsed_bake_time):
#     total_minutos_cocinando = minutos_en_preparar + elapsed_bake_time
#     return total_minutos_cocinando

# expectec_bake_time = 40
# elapsed_bake_time = int(input('Ingrese el tiempo actual que lleva la lazaña en el horno'))
# minutos_en_preparar = preparation_time_in_minutes(capas)
# tiempo_total= elapsed_time_in_minutes(minutos_en_preparar,elapsed_bake_time)
# print
# vocab_words = ['naranje', 'feliz', 'triste']
# v1= vocab_words[:-1]
# print(v1)
# """
# For example: list('en', 'close', 'joy', 'lighten'),
# produces the following string: 'en :: enclose :: enjoy :: enlighten'.
# """
# print(v1 +' :: '+ ' :: '.join([v1 + w for w in vocab_words])) 
# word= 'happiness'
# word = word[:-4]
# if word[-1] == 'i' and word[-2] not in 'a,e,i,o,u':
#         word = word.rstrip('i')
#         wordf= word + 'y'
#         print(wordf)
index = 0

sentence = "I need to make that bright."


if sentence[-1]=='.':#si dejo elpunto me sale error porque el index = -1 me coje el punto
    #sentence = sentence[:-1]
    sentence  = sentence.split()[:-1]
    print(sentence)
verb = sentence[index] + 'en'
print(verb)


def elapsed_time_in_minutes(minutos_en_preparar,elapsed_bake_time):
    total_minutos_cocinando = minutos_en_preparar + elapsed_bake_time
    return total_minutos_cocinando

expectec_bake_time = 40
elapsed_bake_time = int(input('Ingrese el tiempo actual que lleva la lazaña en el horno'))
minutos_en_preparar = preparation_time_in_minutes(capas)
tiempo_total= elapsed_time_in_minutes(minutos_en_preparar,elapsed_bake_time)
print
vocab_words = ['naranje', 'feliz', 'triste']
v1= vocab_words[:-1]
print(v1)