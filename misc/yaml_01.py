import yaml
import json
import pprint
config = confuse.Configuration('MyApp', __name__)

config['AWS']['Lambda']['Runtime'].get()

pp = pprint.PrettyPrinter(indent=4)
data = yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
""")
#print(data)
def open_treeyaml():
    with open('treeyaml.yaml', 'r') as f:
         # use safe_load instead load
        dataMap = yaml.safe_load(f)
        pp.pprint(dataMap)
        treeroot = dataMap['treeroot']
        print(len(treeroot))
        branch2 = treeroot['branch2']
        pp.pprint(branch2)
        name = treeroot['branch2']['name']
        pp.pprint(name)
        #print(branch2)
def open_productyaml():
    with open('product.yaml', 'r') as f:
        product = yaml.safe_load(f)
        pp.pprint(product)
        pp.pprint(type(product))
        for key, value in product.items(): 
            print(f'{key},{value}')
        prod_list = product['product']
        print(type(prod_list))

def open_scalarsyaml():
    with open('scalarsyaml.yaml','r') as f:
        scalars = yaml.safe_load(f)
        pp.pprint(scalars)        

if __name__ == '__main__':
    #open_scalarsyaml()
    open_productyaml()
# yaml_file = yaml.load('learnyaml.yaml')
# print(type(yaml_file))
# yaml_dict = json.loads(yaml_file)