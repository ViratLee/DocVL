import io, json, base64, binascii, codecs
oFileName = 'D:\\rest_response\\uat\\getClaimInfo_1055145_Resp_2018-11-26_1720.json'
#jsonData = open('D:\\rest_response\\prod\\getClaimInfo_3231405_Resp_2018-11-20_0955.json', 'r')
def read_json():
    r_data = ''
    with io.open(oFileName,'r',encoding='UTF-8') as o:
    #with open(oFileName, encoding="latin-1") as datafile:
        r_data = o.read()
        #print(type(r_data))
    return r_data

#open(oFileName, "rb").read().decode("base64")

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise

def decode_cmic_data(jsonData):
    data = json.loads(jsonData)
    #print(type(data))#<class 'dict'>
    if 'data' not in data:
        raise ValueError("No data in json")
    cmic_info = data['data']['jsonData']
    #print(cmic_info)
    print('------------------------------')
    #bytes = [ord(c) for c in cmic_info] 
    #print(bytes)
    #a = base64.b64decode(cmic_info)
    abc = base64.b64encode(cmic_info.encode('utf-8'))
    print(type(abc))
    print(base64.b64decode(abc).decode('iso-8859-1'))
   # b = a.encode('utf-8')
    #print(b)
    #print(base64.b64decode(cmic_info))
    #print('------------------------------')
    #b = binascii.hexlify(base64.b64decode(cmic_info))
    #print(b)
    #print('------------------------------')
    #print(bytearray.fromhex(base64.b64decode(a)))
    # str2 = base64.b64decode(cmic_info).decode('iso-8859-1').encode('utf-8')
    # print('------------------------------')
    # print(str2)
    #cdec1 = codecs.decode(str2)
    #print(cdec1)
    #import base64
    #a = 'eW91ciB0ZXh0'
    #base64.b64decode(a)
    #cmic_info.encode('utf-8')
    #print(cmic_info)
    #str1 = cmic_info[3:]
    # str2 = base64.b64decode(cmic_info).decode('iso-8859-1').encode('utf-8')
    # print(str2.hex())
    # str3 = bytes.fromhex(str2.hex()).decode('utf-8')
    # print(str3)
    #u = binascii.hexlify((cmic_info))
    #print(str3)
    """ISO-8859-1
    str2 = base64.b64decode(cmic_info).decode('iso-8859-1').encode('utf-8')
    print(str2)
    str3 = base64.b64decode(cmic_info).decode('utf-8', "backslashreplace")
    print('------------------------------')
    print(str3)
    """
    #with io.open("D:\\testcmic_json.txt",'a',encoding='utf8') as o:  
    #    write_output_file(o,str3, True)
    """
    b = bytes(cmic_info, 'utf-8')
    print(type(b))
    print(b)
    print('-----------------------------------------')
    decoded_string = base64.b64decode(b,'ISO8859_1')
    print(type(decoded_string))
    print(decoded_string[1])
"""



#Converts this String to a byte encoding using the default encoding as specified 
#by the file.encoding sytem property. If the system property is not defined, the default encoding is ISO8859_1 (ISO-Latin-1). If 8859-1 is not available, an ASCII encoding is used.

    #decoded_string2 = base64.b64encode(decoded_string)
    #print(decoded_string)
    #print(cmic_info)#eJyVWN2LHDcS/1eWeQ7nntkPr/fNO+M9b...
    """
    decoded_string = base64.b64decode(cmic_info)
    decoded_string2 = base64.b64encode(decoded_string)
    decoded_string3 = base64.b64decode(decoded_string2)
    """
    #decoded_string2 = bytes.decode(base64.b64decode(cmic_info))
    #str = base64.unicode(base64.b64decode(cmic_info), errors='replace')
    #decoded_string4 = binascii.unhexlify(bytes.decode(decoded_string2)) #.decode('utf8')
    #print(decoded_string2)
    #encoded_string = base64.b64encode(decoded_string)
    #print(encoded_string)
    """
    str1 = decoded_string.hex()
    print(str1)
    """
    #str2 = binascii.unhexlify(cmic_info).decode('utf8')
    #print(str2)
    
def test():
    en_byte = base64.b64encode(b'\x00\x00\x00\x00\x19\x4B\xD6')
    print(type(en_byte)) #<class 'bytes'>
    print(en_byte) #b'AAAAABlL1g=='
    str1 = base64.b64encode(en_byte)
    print(str1)
    #de_str = base64.b64decode(en_byte)
    #print(de_str) #b'\x00\x00\x00\x00\x19\x4B\xD6'

def main():
    json_data = read_json()
    decode_cmic_data(json_data)
    #test()

if __name__ == '__main__':
    main()