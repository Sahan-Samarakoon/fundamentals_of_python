import csv

with open('data.csv', 'w') as file:
    # method takes in a file object to create a writer object
    writer = csv.writer(file)
    writer.writerow(['transaction_id', 'product_id', 'price'])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

with open('data.csv') as file:
    reader = csv.reader(file)
    print(list(reader))  # converts all items in file to a list
    # we get a list of lists
    for data in reader:
        print(data)