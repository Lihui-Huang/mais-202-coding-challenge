import csv
import matplotlib.pyplot as plt


# create a class that stores the number of datas and the current average of the interest rate for each purpose
class Pair:
    def __init__(self, num, average):
        self.number = num
        self.avgint = float(average)

    # update the average interest rates when we have a new data of the same purpose
    def calculateavg(self, intrate):
        self.avgint = (self.avgint * self.number + float(intrate)) / (self.number + 1)
        self.number += 1


with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    row_count = 0
    rate_index = 0
    purpose_index = 0
    index = 0
    purpose_intrate = {}

    # create a dictionary that matches a purpose to a Pair class
    final_result = {}

    # first find out the index of the purpose and interest rate in each row of the input data
    # if the purpose exsist in the dictionary, update the corresponding average
    # if the purpose does not exist in the dictionary, create a mathed pair in the dictionary and a new Pair class
    for row in csv_reader:
        if line_count == 0:
            for element in row:
                if element == "int_rate":
                    rate_index = index
                if element == "purpose":
                    purpose_index = index
                index += 1
            # print str(rate_index) + ',' + str(purpose_index)
            line_count += 1
        else:
            if row[purpose_index] in purpose_intrate:
                purpose_intrate[row[purpose_index]].calculateavg(row[rate_index])
            else:
                purpose_intrate[row[purpose_index]] = Pair(1, row[rate_index])

    # print len(purpose_intrate)

    for element in purpose_intrate:
        final_result[element] = purpose_intrate[element].avgint
        print 'Purpose: ' + element
        print 'Average interest rate: ' + str(purpose_intrate[element].avgint) + '\n'

    # generate a chart
    with open('output_table.csv', 'wb') as output:
        writer = csv.writer(output)
        writer.writerow(['Purpose', 'avg_rate'])
        for key, value in final_result.iteritems():
            writer.writerow([key, round(value, 2)])

    # generate a graph
    plt.rcParams.update({'font.size': 5})
    plt.bar(range(len(final_result)), final_result.values(), align='center')
    plt.xticks(range(len(final_result)), final_result.keys())
    plt.savefig('output_graph.png', dpi=300)
    plt.show()
