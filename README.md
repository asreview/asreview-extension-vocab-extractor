# Extension - matrix and vocabulary extractor for TF-IDF
An extension for ASReview that adds a tf-idf extractor that saves the matrix and the vocabulary to pickle and JSON respectively. Requested in discussion post #650.


## Getting started

Run install the new classifier with:

```bash
pip install .
```

or

```bash
python -m pip install git+https://github.com/asreview/asreview-extension-tfidf-extractor.git
```


## Usage

Run the simulation as usual, but this time use `tfidf_grab` as feature extractor. Extracts the matrix and the vocabulary during simulation preparation. The new Feature extractor `tfidf_grab` is defined in [`asreviewcontrib.models.tfidf_grab.py`](asreviewcontrib.models.tfidf_grab:Tfidf_grab).

The new extractor can be used like this:
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

## License

apache-2.0
