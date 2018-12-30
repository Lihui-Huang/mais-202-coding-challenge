import csv
import matplotlib.pyplot as plt;


class Pair:
    def __init__(self, num, average):
        self.number = num
        self.avgint = float(average)

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
    final_result = {}

    for row in csv_reader:
        if line_count == 0:
            for element in row:
                if element == "int_rate":
                    rate_index = index
                if element == "purpose":
                    purpose_index = index
                index += 1
            print str(rate_index) + ',' + str(purpose_index)
            line_count += 1
        else:
            if row[purpose_index] in purpose_intrate:
                purpose_intrate[row[purpose_index]].calculateavg(row[rate_index])
            else:
                purpose_intrate[row[purpose_index]] = Pair(1, row[rate_index])

    print len(purpose_intrate)

    for element in purpose_intrate:
        final_result[element] = purpose_intrate[element].avgint
        print element + '   ' + str(purpose_intrate[element].avgint)

    # generate a chart
    with open('output.csv', 'wb') as output:
        writer = csv.writer(output)
        writer.writerow(['Purpose', 'avg_rate'])
        for key, value in final_result.iteritems():
            writer.writerow([key, round(value,2)])

    plt.bar(range(len(final_result)), final_result.values(), width=30)  # python 2.x
    plt.xticks(range(len(final_result)), final_result.keys())  # in python 2.x

    plt.show()
