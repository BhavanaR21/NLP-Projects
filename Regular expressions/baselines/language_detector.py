import argparse
import random
import re


def detect_language(sentence):
    """
    Detect the language of a document

    Args
        sentence: a tokenized sentence. Tokens are separated by white space.

    Returns:
        String indicating the language of sentence
          "en" if the document is en English
          "es" if the document is en Spanish
    """

    language = None
    # TODO Change the code below so the return value is not random
    #   You will get full credit as long as your implementation gets more than 65% accuracy
    #   Your implementation should be simple: a few if statements is all you need
    #   We will test your code with new sentences, so write a generic language detector
    if random.random() < 0.5:
        language = "en"
    else:
        language = "es"

    assert language in ["en", "es"]
    return language


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect the language of document.')
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    preds_check = []
    for sentence in args.file.readlines():
        sentence = sentence.rstrip()
        gold_language, sentence = re.search("(\w{2}) (.*)", sentence).groups()
        pred_language = detect_language(sentence)

        if gold_language == pred_language:
            preds_check.append(1)
        else:
            preds_check.append(0)

        print(f"PRED: {pred_language} | GOLD : {gold_language} | {sentence}")

    print("*" * 40)
    print(f"  Accuracy: {sum(preds_check) / len(preds_check):.2f} [{sum(preds_check)}/{len(preds_check)}]")
