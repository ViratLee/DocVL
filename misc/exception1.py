def exeception_func_1():
    try:
        result = 4/0
        return 1
    except Exception as e:
        print('in exception')
        return 2
    finally:
        print('in finally')
        return 3

if __name__ == '__main__':
    print(f"in main {exeception_func_1()}")
# output
# in exception
# in finally
# in main 3