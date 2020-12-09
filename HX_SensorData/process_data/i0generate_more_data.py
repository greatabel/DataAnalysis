from  i0csv_operation import csv_write, csv_reader


times = 3

def main():
    global times
    sourcelist = csv_reader('source_demo.csv')
    # print(len(sourcelist))
    lastrow = sourcelist[-1]
    i = int(lastrow[0])
    
    csv_write('genreated_demo.csv', sourcelist)
    print('original turn added')
    del sourcelist[0]
    for i_turn in range(0, times-1):
        print(i_turn, ' turn added')

        for idx, val in enumerate(sourcelist):
            # print(idx, val)
            if idx != 0:
                i += 1
                sourcelist[idx][0] = i
        csv_write('genreated_demo.csv', sourcelist, 'a')

if __name__ == "__main__":
    main()