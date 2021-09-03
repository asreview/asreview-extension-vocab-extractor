from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name=' asreview-extension-tfidf-extractor',
    version='0.1',
    description='tf-idf with saving functionality',
    url='https://github.com/asreview/asreview-extension-tfidf-extractor',
    author='Jelle Teijema',
    author_email='j.j.teijema@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'sklearn',
        'asreview>=0.13'
    ],
    entry_points={
        'asreview.models.classifiers': [
        ],
        'asreview.models.feature_extraction': [
            'tfidf_grab = asreviewcontrib.models.tfidf_grab:Tfidf_grab',
        ],
        'asreview.models.balance': [
            # define balance strategy algorithms
        ],
        'asreview.models.query': [
            # define query strategy algorithms
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/asreview/asreview/issues',
        'Source': 'https://github.com/asreview/asreview/',
    },
)
