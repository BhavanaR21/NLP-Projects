import argparse
import re


def tagger(file):
    """
    Detect the language of a document

    Args
        file: a file with one sentence per line. Tokens are separated by white space.

    Returns:
        Generator of sentences in file with part-of-speech tagged tokens. Each token is in the format "word/POS_TAG"
    """

    # TODO Change the code below so that not all tokens are assigned the NN part-of-speech tag (Noun, singular or mass)
    #   See the full tagset here: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    #   Hint: hard code with an if statement words that are common and easy to assign part-of-speech tags to.
    #   For example, "the" is always a DT (determiner) and words ending in "ly" tend to be RB (adverbs)
    #   Your are implementing a baseline, which has to be simple: a few if statement is all you need.
    #   We will test your code with additional sentences, so aim at a generic part-of-speech tagger for English
    #   An acceptable accoracy is above 30%
    for sentence in file.readlines():
        sentence = sentence.rstrip()
        tokens = sentence.split(" ")
        pos_tags = []
        for token in tokens:
            pos_tags.append("NN")
        yield " ".join([f"{t}/{p}" for t, p in zip(tokens, pos_tags)])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect the language of document.')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('file_gold', type=argparse.FileType('r'))
    args = parser.parse_args()

    num_tokens = 0
    num_tokens_correct = 0
    for tagged_sentence, gold_sentence in zip(tagger(args.file), args.file_gold.readlines()):
        gold_sentence = gold_sentence.rstrip()
        tagged_tokens = tagged_sentence.split(" ")
        gold_tokens = gold_sentence.split(" ")
        for tagged_token, gold_token in zip(tagged_tokens, gold_tokens):
            t_word, t_tag = tagged_token.split("/")
            g_word, g_tag = gold_token.split("/")
            assert t_word == g_word
            if t_tag == g_tag:
                num_tokens_correct += 1
            num_tokens += 1
        print(f"PRED: {tagged_sentence}")
        print(f"GOLD: {gold_sentence}")
        print("*" * 40)

    print(f"  Accuracy: {num_tokens_correct / num_tokens:.2f} [{num_tokens_correct}/{num_tokens}]")

