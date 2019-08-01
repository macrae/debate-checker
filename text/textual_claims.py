"Methods for identifying and parsing textual claims."

import random
import string

import spacy
from sklearn.base import TransformerMixin
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


def listen_for_textual_claims(text_stream):
    """Flags statements containing a factual claim.
    NOTE: Will need a statistical model, but will need to start w/ rules based to bootstrap labels.
    """
    claim = None
    return claim


punctuations = string.punctuation

parser = spacy.load("en_core_web_sm")

# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}


# Basic utility function to clean the text
def clean_text(text):
    return text.strip().lower()


# Create spacy tokenizer that parses a sentence and generates tokens
# these can also be replaced by word vectors
def spacy_tokenizer(sentence):
    tokens = parser(sentence)
    tokens = [
        tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_
        for tok in tokens
    ]
    tokens = [
        tok for tok in tokens if (tok not in stopwords and tok not in punctuations)
    ]
    return tokens


# create vectorizer object to generate feature vectors, we will use custom spacy’s tokenizer
vectorizer = CountVectorizer(tokenizer=spacy_tokenizer, ngram_range=(1, 1))
classifier = LinearSVC()

# Create the  pipeline to clean, tokenize, vectorize, and classify
pipe = Pipeline(
    [("cleaner", predictors()), ("vectorizer", vectorizer), ("classifier", classifier)]
)

# Load sample data
# TODO: load data
data: list = []
random.shuffle(data)

n_train, n_test = int(len(data) * 0.70), len(data) - int(len(data) * 0.70)
train, test = data[:n_train], data[n_train:]

# Create model and measure accuracy
pipe.fit([x[0] for x in train], [x[1] for x in train])
pred_data = pipe.predict([x[0] for x in test])
for (sample, pred) in zip(test, pred_data):
    print(sample, pred)
print("Accuracy:", accuracy_score([x[1] for x in test], pred_data))


def find_numerical_claims():
    """Involving numerical properties about entities and comparisons among them.
    """


def find_entity_and_event_properties():
    """Involving such things as professional qualifications or events.
    """


def find_position_statements():
    """Involving such things as whether a political entity supported a certain policy.
    """


def find_quote_verification_assessments():
    """Involving such things as whether the claim states precisely the source of a quote, 
    its content, and the event at which it supposedly occurred.
    """
