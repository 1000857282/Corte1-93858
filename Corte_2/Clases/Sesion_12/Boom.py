
def boom (x):
    if x>0:
        print(x)
        boom(x-1)
    else:
        print('Booom!')
    print(f'finsalizo {x}')

def main():
    boom(5)

if __name__=='__main__':
    main()