from graph import Graph


def parse_line(line) -> tuple:
    data = line.strip().split(',')
    return tuple([data[0], data[-1]])


if __name__ == "__main__":
    print("In main")

    graph = Graph()

    with open("./time_by_task_20230220.csv") as csv_file:
        for _ in range(1):
            line = csv_file.readline()
        while line:
            client, name = parse_line(line)

            graph.add_relationship(name, "worked on", client)
            line = csv_file.readline()

    with open("./knowledge.json", "at") as json_file:
        json_file.write(graph.to_json())



