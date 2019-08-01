# Supervised Sentence-level Classification of Textual Claims

Textual claims are short sentences constructed from longer passages, a
common practice among human fact checkers. The purpose is to include only
the relevant context of the claim from the original passage.

The goal of this project is to parse from unstructured, streaming text
any fact-based claims and return a corresponding textual claim.
(specifically, text generated from a voice to text transformation which
may be lacking in robust grammatical characteristsics like punctuation,
etc...).

```
f(text_stream) => textual_claim
```

Following the [HeroX](https://www.herox.com/factcheck/5-practise-claims)
taxonomy we will consider four types of claims:

1. Numerical claims
2. Verification of quotes
3. Position statements
4. Objects, properties, and events

The goal of this project is simply to parse and return _any textual claim_,
and one approach for research and development is to break the problem down
into more manageable pieces - and this taxonomy may do that - however
it is not a requirement to parse, for example, numerical claims from
position claims.

# Named Entities that Support Supervised Task

Since we will be using supervised learning to classify textual claims,
engineering a robust set of features, or named entities, within the text
will hopefully guide our learner towards more effective classification.

## Named Entities to Model
1. Comparisons
2. Time periods (also in human terms, such as: "since the World War II...")
3. Imprecise adjectives (sky rocketing, biggest drop, etc...)
4. Proportionalities (half, the majority, one in five, etc...)
5. Hedges (roughly, generally, broadly, etc...)
6. Geographies (New York, the west coast, the EU, etc..)

# Models as a Service Framework

