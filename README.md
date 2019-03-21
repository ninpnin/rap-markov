# rap-markov

```
Jauhetaan sut, ku prameita 
Niin ku äiti ompeli hameita 
Kaikki kuvat tosin osin kaameita 
Valmis totuus muistuttaa lähinnä turhii haaveita
```
 
## How it works

Since rap is based on rhymes, ie. the last words of consecutive rows rhythmically matching, the regular Markov chain approach fails to produce good results. To counter this, this algorithm first generates the last word of each row. After that, the rest of each row is generated as a normal Markov process.

This algorithm also takes a somewhat Bayesian approach to the Markov process. With a probability 1/(1+n) - where n is the number of the current word appearing in the training data – a random word is generated instead. This can be thought as the mean of the proportion of the __observed__ following words in the underlying distribution.

For example, if the word "hello" (being followed by "world") has only occured once in the training data, the probability of it being followed by the word "world" would be 1/2. On the other hand, if we had observed the same "hello world" pair 1000 times, the probability of the word "hello" being followed by "world" would have been a lot higher, namely 1000/1001.

## How to use it

Just copy paste any (preferably large) set of lyrics into a text file. The default name of the text file is __data.txt__, but this can easily be changed from the code.
