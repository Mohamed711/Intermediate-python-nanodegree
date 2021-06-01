import csv
import json
from collections import defaultdict
import helper


def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}  # Map from code -> name
    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}  # Map from code -> name
    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        for line in reader:
            if line[2] not in routes.keys():
                routes[line[2]] = list()

            routes[line[2]].append(line[4])
    return routes


def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.

    avail_paths = [[source]]
    output_paths = defaultdict(list)

    # Visited Nodes
    visited_airports = set()
    visited_airports.add(source)

    for _ in range(max_segments):

        avail_length = len(avail_paths)
        for _ in range(avail_length):
            out = avail_paths.pop(0)
            last_airport = out[len(out) - 1]

            # Check for trips from last airport
            if last_airport in routes.keys():
                for airport in routes[last_airport]:
                    new_route = out.copy()
                    new_route.append(airport)

                    if airport == dest:
                        if tuple(new_route) not in output_paths[len(new_route) - 1]:
                            output_paths[len(new_route) - 1].append(tuple(new_route))

                    elif airport not in out:
                        # visited_airports.add(airport)
                        avail_paths.append(new_route)

    return output_paths


def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = defaultdict(list)

    for key, routes in paths.items():
        for route in routes:
            rt = list()
            for airport in route:
                rt.append(airports[airport])
            output[key].append(rt)

    # Don't forget to write the output to JSON!
    with open("outputFile.json", 'w') as file:
        json.dump(output, file, indent=4)


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
