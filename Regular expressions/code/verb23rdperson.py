import argparse
import re

def read_verbs(file_path):
    with open(file_path) as f:
        for verb in f.readlines():
            verb = verb.rstrip()
            if len(verb) < 1:
                continue
            yield verb.rstrip()


def get_3rdperson(verb):
    # YOUR CODE GOES HERE
    # Use the re module to do string matching. A good solution is as short as 5 lines

    verb_3rdperson = verb + "_3rdperson"
    return verb_3rdperson


def main(file_path):
    for verb in read_verbs(file_path):
        verb3rdperson = get_3rdperson(verb)
        print(f"{verb:10} {verb3rdperson}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE_PATH",
                        help="Path to file with verbs in their base form, one verb per line")
    args = parser.parse_args()

    main(args.FILE_PATH)