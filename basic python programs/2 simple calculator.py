while True:
    try:
        print('==========Simple Calculator============')
        a = float(input('Enter your 1st number: '))
        b = float(input('Enter your 2nd number: '))
        inp = input('What operation you want to perform (sub/sum/mul/div):')

        if inp == 'sum':
            sum = a + b
            print('Sum is of', a, ' and ', b, ' is:', sum)
        elif inp == 'sub':
            sub = a - b
            print('Subtraction of ', b, ' from ', a, ' is: ', sub)
        elif inp == 'mul':
            mul = a * b
            print('Multiplcation of', a, ' and ', b, ' is: ', mul)
        elif inp == 'div':
            div = a / b
            print('Division of ', a, ' by ', b, ' is:', round(div, 4))
    except Exception as e:
        print("ERROR: ", e)

        
 ## OUTPUT:
#           ==========Simple Calculator============
#           Enter your 1st number: 4634
#           Enter your 2nd number: 4
#           What operation you want to perform (sub/sum/mul/div):mul
#           Multiplcation of 4634.0  and  4.0  is:  18536.0
