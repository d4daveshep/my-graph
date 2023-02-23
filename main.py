from graph import Graph


def parse_line(line):
    data = line.strip().split(',')
    return tuple(data[:3])


if __name__ == "__main__":
    print("In main")

    graph = Graph()

    with open("./graph/staff_list.csv") as csv_file:
        line = csv_file.readline()
        while line:
            name, gm, employment_type = parse_line(line)
            graph.add_relationship(name, "under GM", gm)
            graph.add_relationship(name, "employment", employment_type)
            line = csv_file.readline()

    pass
