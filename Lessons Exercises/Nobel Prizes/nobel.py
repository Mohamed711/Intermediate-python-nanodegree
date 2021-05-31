import json

import helper


def load_nobel_prizes(filename='prize.json'):
    with open(filename, 'r') as inputfile:
        data = json.load(inputfile)
    return data


def main(year, category):
    content = load_nobel_prizes()

    output_content = dict()
    output_content["prizes"] = list()

    for prize in content["prizes"]:
        if year and year != prize["year"]:
            continue

        if category and prize["category"] != category:
            continue

        output_content["prizes"].append(prize)

    if year or category:
        content = output_content

    with open('outputfile.json', 'w') as outputFile:
        json.dump(content, outputFile, indent=2)


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)

