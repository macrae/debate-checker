python3 -m venv .venv
source .venv/bin/activate

pip install resources/prodigy-1.4.0-cp35.cp36-cp35m.cp36m-macosx_10_13_x86_64.whl
pip install resources/en_vectors_web_lg-2.0.0.tar.gz
pip install resources/en_core_web_sm-2.0.0.tar.gz

pip uninstall spacy
pip uninstall thinc
pip uninstall hug
pip uninstall falcon

pip install spacy==2.0.12
pip install thinc==6.10.3
pip install hug==2.4.1
pip install falcon==1.4.1

export PRODIGY_HOME=/Users/smacrae/github/debate-checker/