import argparse
import os, re
import collections
import math

def preprocess(line):
    # DO NOT CHANGE THIS METHOD unless you want to explore other options and discuss your finding in the report

    # get rid of the stuff at the end of the line (spaces, tabs, new line, etc.)
    line = line.rstrip()
    # lower case
    line = line.lower()
    # remove everything except characters and white space
    line = re.sub("[^a-z ]", '', line)
    # tokenized, not done "properly" but sufficient for now
    tokens = line.split()

    # adding $ before and after each token because we are working with bigrams
    tokens = ['$' + token + '$' for token in tokens]

    return tokens


def create_model(path):
    # This is just some Python magic ...
    # unigrams[key] will return 0 if the key doesn't exist
    global unigrams
    unigrams = collections.defaultdict(int)
    # and then you have to figure out what bigrams will return
    bigrams = collections.defaultdict(lambda: collections.defaultdict(int))
    #print(path)
    f = open(path, 'r')
    ## You shouldn't visit a token more than once
    # FIXME Update the counts for unigrams and bigrams
    for l in f.readlines():
        tokens = preprocess(l)
        #print(tokens)
        
        if len(tokens) == 0:
            continue
        for token in tokens:
        	bi_char = [token[i:i+2] for i in range(len(token)-1)]
        	for BiChar in bi_char:
        		bigrams[BiChar[0]][BiChar[1]] += 1
        	uni_char = [token[i:i+1] for i in range(len(token))]
        	for UniChar in uni_char:
        		unigrams[UniChar] += 1
          			
   #print(bigrams)
   #print(unigrams)
   #print(b)
    # pass
    # FIXME After calculating the counts, calculate the smoothed log probabilities
    for char1 in bigrams:
        for char2 in bigrams[char1]:
            prob = (bigrams[char1][char2] +1)/(unigrams[char1]+26)
            bigrams[char1][char2] = math.log(prob)  
 		
#     print(bigrams)
#     print(unigrams)
    
	
    # return the actual model: bigram (smoothed log) probabilities and unigram counts (the latter to smooth
    # unseen bigrams in predict(...)
#     return None
    return bigrams;


def predict(file, model_en, model_es):
    prediction = None

    # FIXME Use the model to make predictions.
    # FIXME: Predict whichever language gives you the highest (smoothed log) probability
    # - remember to do exactly the same preprocessing you did when creating the model (that's why it is a method)
    # - you may want to use an additional method to calculate the probablity of a text given a model (and call it twice)
   
    CalcProb_en =0
    CalcProb_es=0
    f = open(file, 'r')
    for l in f.readlines():
        tokens = preprocess(l)
        for token in tokens:
        	bi_char = [token[i:i+2] for i in range(len(token)-1)]
        	for BiChar in bi_char:
        	    Prob_en = probabilityPred(BiChar, model_en)
        	    Prob_es = probabilityPred(BiChar, model_es)
        	    
        	    CalcProb_en = CalcProb_en+Prob_en;
        	    CalcProb_es = CalcProb_es+Prob_es;
     # prediction should be either 'English' or 'Spanish'   	    	
    if(CalcProb_en>CalcProb_es):
    	 prediction = 'English'
    else:
    	 prediction = 'Spanish'
    
    return prediction

def probabilityPred(bigram_chars, model):
       if(model[bigram_chars[0]][bigram_chars[1]]==0):
                prob = 1/(unigrams[char1]+27)
                return prob
       else:
	        return model[bigram_chars[0]][bigram_chars[1]]
	
def main(en_tr, es_tr, folder_te):
    # DO NOT CHANGE THIS METHOD

    # STEP 1: create a model for English with en_tr
    model_en = create_model(en_tr)

    # STEP 2: create a model for Spanish with es_tr
    model_es = create_model(es_tr)

    # STEP 3: loop through all the files in folder_te and print prediction
    folder = os.path.join(folder_te, "en")
    print("Prediction for English documents in test:")
    for f in os.listdir(folder):
        f_path = os.path.join(folder, f)
        print(f"{f}\t{predict(f_path, model_en, model_es)}")

    folder = os.path.join(folder_te, "es")
    print("\nPrediction for Spanish documents in test:")
    for f in os.listdir(folder):
        f_path = os.path.join(folder, f)
        print(f"{f}\t{predict(f_path, model_en, model_es)}")


if __name__ == "__main__":
    # DO NOT CHANGE THIS CODE

    parser = argparse.ArgumentParser()
    parser.add_argument("PATH_TR_EN",
                        help="Path to file with English training files")
    parser.add_argument("PATH_TR_ES",
                        help="Path to file with Spanish training files")
    parser.add_argument("PATH_TEST",
                        help="Path to folder with test files")
    args = parser.parse_args()

    main(args.PATH_TR_EN, args.PATH_TR_ES, args.PATH_TEST)
