import helper
import gold


def parse_content(content):
    """ Parse the content of the file """
    words = dict()
    for line in content.split('\n'):
        word, frequency = line.split()
        words[word] = int(frequency)

    return words


def make_tree(words):
    trie_structure = dict()
    for key, value in words.items():
        current_loc = trie_structure
        for character in key:
            if character not in current_loc.keys():
                current_loc[character] = dict()

            current_loc = current_loc[character]
        current_loc["$" + key] = value

    return trie_structure


def get_leaves(node):
    """ Get the leaves from a given tree """
    leaf_nodes = list()
    search_list = [node]

    while search_list:
        search_node = search_list.pop()
        for key in search_node.keys():
            if key.startswith("$"):
                leaf_nodes.append((key.replace("$", ""), search_node[key]))
            else:
                search_list.append(search_node[key])

    return leaf_nodes


def predict(tree, numbers):
    """ Predict the value from the input numbers """
    output_predictions = list()
    search_list = [tree]
    t9 = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    for number in numbers:
        length = len(search_list)

        for _ in range(length):
            node = search_list.pop(0)
            for key in node.keys():
                if key in t9[number]:
                    search_list.append(node[key])

    for node in search_list:
        output_predictions.extend(get_leaves(node))

    output_predictions.sort(key=lambda x: x[1], reverse=True)
    return output_predictions


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
