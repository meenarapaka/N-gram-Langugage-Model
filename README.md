# N-gram-Langugage-Model
To generate a sequence of words, the program calculates the probability that a word follows specific word/phrase. It randomly picks the next word based on a probability distribution -- a series of ranges that each correspond to likelihoods of occurrence. The size (number of words) of the phrase to use for generation is N; a statistical model created from the likelihood of N-sized phrases is called an N-gram model.

Usage: The program can be called via a command-line interface. It takes 3+ arguments: arg1 is the N-value, used for computing ngrams arg2 is M, the number of sentences to generate args 3+ are the texts to pull words from
