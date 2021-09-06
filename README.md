# Extension - matrix and vocabulary extractor for TF-IDF and Doc2Vec
An extension for ASReview that adds a tf-idf extractor that saves the matrix and the vocabulary to pickle and JSON respectively, and a doc2vec extractor that grabs the entire doc2vec model. Requested in discussion post [#650](https://github.com/asreview/asreview/discussions/650).


## Getting started

Install the new classifier with:

```bash
pip install .
```

or

```bash
python -m pip install git+https://github.com/asreview/asreview-extension-vocab-extractor.git
```


## Usage

Run the simulation as usual, but this time use `tfidf_grab` or `doc2vec_grab` as feature extractor. Extracts the matrix and the vocabulary during simulation preparation. The new Feature extractor `tfidf_grab` is defined in [`asreviewcontrib.models.tfidf_grab.py`](asreviewcontrib.models.tfidf_grab:Tfidf_grab), and `doc2vec_grab` is defined in [`asreviewcontrib.models.doc2vec_grab.py`](asreviewcontrib.models.doc2vec_grab:Doc2Vec_grab).

The new tf-idf extractor can be used like this:
```bash
asreview simulate benchmark:van_de_Schoot_2017 --state_file myreview.h5 -e tfidf_grab
```

The vocabulary is saved to the current folder as `vocabulary.json`, and the matrix is pickled to `matrix.pickle`.

---
**NOTE**
Extracting the pickle can be done like this:

```Python
import pickle

matrix = pickle.load(open("matrix.pickle","rb"))
print(matrix.shape)
```
---


The new doc2vec extractor can be used like this, assuming gensim is installed:
```bash
asreview simulate benchmark:van_de_Schoot_2017 --state_file myreview.h5 -e doc2vec_grab
```
The doc2vec extractor will store the entire model to `gensim.model`. As this might be a difficult file to work with, included in the repo is the file `example_doc2vec.ipynb`. This notebook contains code that transforms the gensim model to a dict object with words and their corresponding vector.

## Contact
The best resources to find an answer to your question or ways to get in
contact are:

- Issues or feature requests - [Extension issue tracker](https://github.com/asreview/asreview-extension-vocab-extractor/issues)
- Contact - [j.j.teijema@uu.nl](mailto:j.j.teijema@uu.nl)

## License

Apache-2.0
