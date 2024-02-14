def get_link():
    import csv
    csv_file = "C:/Users/hosei/Documents/GIT/Recommender/ScrapingKojaro/Links/links.csv"
    link_list = []
    with open(csv_file, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            link_list.append(lines[0])
    return link_list