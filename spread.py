def get_max_spread():
    '''
    A function that reads through a file - weather.dat, loops through the rows and returns to
    console the maximum spread (difference between columns MxT and MnT) by printing the day of
    the month and the spread.
    '''

    # initialize the max spread variable to 0
    max_spread=0
    # initialize the day and the max spread dict
    day_spread = {'day':0, 'max_spread':0}
    # a variable to skip row 1 - header, and row 2 - empty row
    count=0

    # open the file
    for line in open('weather.dat', 'r'):
        # skip the first two rows
        if count == 0 or count == 1:
            count +=1
            continue

        # split the rows into python lists
        row = line.split()

        # get the difference between column 2 - MxT and column 3 - MnT
        diff = float(row[1].strip('*')) - float(row[2].strip('*'))

        # compare the maxspread and the difference between MxT and MnT
        if diff > max_spread:
            max_spread=diff
            day_spread['day'], day_spread['max_spread'] = row[0], max_spread

    # print day and the max_spread
    print  day_spread['day'], day_spread['max_spread']

if __name__ == "__main__":
    get_max_spread()