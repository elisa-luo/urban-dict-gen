# urban-dict-gen
Urban Dictionary definition generation using a RNN. Experimentation with text generation with colloquial language, while we wait for our Twitter developer account to be approved. Will probably use a similar model on tweets for an ongoing mystery project ;).

credit to https://www.tensorflow.org/tutorials/text/text_generation for starter code

dataset from: https://www.kaggle.com/therohk/urban-dictionary-words-dataset/data

__write.py:__
python script to parse the data set and convert from csv to one continous text file to use as training dataset. Get rid of 'bad' definitions by only including those with at least 75% positive 'votes'. 

__text_generation.ipynb:__
(python notebook, so I can use google colab and their far, far, superior computing power than my puny macbook)
Builds and trains model. Then generates some of its own urban dictionary definitions.

