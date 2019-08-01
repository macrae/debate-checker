prodigy dataset democratic_primary "2019 democratic primary debates" --author smacrae

prodigy ner.manual trump en_core_web_sm data/debates/trump_time_interview_06_20_2019.jsonl --label "AMBIGUOUS_CLAIM, OPINION, NUMERICAL_CLAIM, POSITION_STATEMENT, OBJECT_PROPERTY_EVENT, PERSON, ORGANIZATION, COUNTRY, GEOGRAPHY, TIME_PERIOD"

prodigy ner.teach trump en_core_web_sm data/debates/trump_time_interview_06_20_2019.jsonl --label "OBJECT_PROPERTY_EVENT"

prodigy textcat.teach trump en_core_web_sm data/debates/trump_time_interview_06_20_2019.jsonl --label "TEXTUAL_CLAIM"

prodigy textcat.teach trump en_core_web_sm data/debates/trump_clinton_09_26_2016.jsonl --label "TEXTUAL_CLAIM"

prodigy textcat.batch-train trump --output-model /tmp/model --eval-split 0.2

prodigy ner.match trump en_core_web_sm data/debates/trump_clinton_09_26_2016.jsonl --patterns patterns.jsonl

prodigy ner.batch-train trump en_core_web_sm --output /tmp/model --eval-split 0.5 --label TIME_PERIOD