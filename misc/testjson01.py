import json

with open('apod.json', 'r') as f:
        json_text = f.read()

# Decode the JSON string into a Python dictionary.
print('json_text is {} type'.format(type(json_text)))#json_text is <class 'str'> type
apod_dict = json.loads(json_text)
print('apod_dict is {} type'.format(type(apod_dict)))#apod_dict is <class 'dict'> type
print(apod_dict['explanation'])#Meteors have been shooting out from the constellation of Orion...

# Encode the Python dictionary into a JSON string.
new_json_string = json.dumps(apod_dict, indent=4)
print('new_json_string is {} type'.format(type(new_json_string)))#new_json_string is <class 'str'> type
print(new_json_string)
# {
#     "copyright": "Yin Hao",
#     "date": "2018-10-30",
#     "explanation": "Meteors have been shooting out from the constellation of Orion...",
#     "hdurl": "https://apod.nasa.gov/apod/image/1810/Orionids_Hao_2324.jpg",
#     "media_type": "image",
#     "service_version": "v1",
#     "title": "Orionids Meteors over Inner Mongolia",
#     "url": "https://apod.nasa.gov/apod/image/1810/Orionids_Hao_960.jpg"
# }