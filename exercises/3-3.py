def table(col_w, lenght_of_row,nlines):
        for i in range(lenght_of_row): #the lenght of the raw is indicated in number of columns
            print('+',col_w*'-','+',col_w*'-','+')
            for ii in range(lenght_of_row):
                print('|', col_w*' ','|', col_w*' ','|')
            if nlines == 1 :
                print('+',col_w*'-','+',col_w*'-','+')
            else:
                pass


        
table(5,4,5)
    