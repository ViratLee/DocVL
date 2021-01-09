def method_01(param1, param3 = 0 , param2 = "not bark" ):
	print('{} have {}, {}'.format(param1,param3, param2))
def main():
	method_01("dog", 4)
	method_01("cat", param2='meaw meaw')
if __name__ == '__main__':
    main() 