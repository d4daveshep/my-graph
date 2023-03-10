from graph import Graph


def parse_line(line) -> tuple:
    data = line.strip().split(',')
    return tuple(data[:3])


if __name__ == "__main__":
    print("In main")

    graph = Graph()

    with open("./staff_list.csv") as csv_file:
        for _ in range(9):
            line = csv_file.readline()
        while line:
            name, gm, employment_type = parse_line(line)
            graph.add_relationship(name, "under GM", gm)
            graph.add_relationship(name, "employment", employment_type)
            line = csv_file.readline()

    with open("./knowledge.json", "at") as json_file:
        json_file.write(graph.to_json())



