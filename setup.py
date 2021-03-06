import sys
if sys.version_info.major != 3: raise Exception('ktrain requires Python 3')
tf_version_str = 'tensorflow==2.1.0'
if sys.version_info.minor == 8:
    tf_version_str = 'tensorflow>=2.2.0'

from distutils.core import setup
import setuptools

with open('README.md', encoding='utf-8') as readme_file: 
    readme_file.readline()
    readme = readme_file.read()
exec(open('ktrain/version.py').read())


setup(
  name = 'ktrain',
  packages = setuptools.find_packages(),
  package_data={'ktrain': ['text/shallownlp/ner_models/*']},
  version = __version__,
  license='Apache License 2.0',
  description = 'ktrain is a wrapper for TensorFlow Keras that makes deep learning and AI more accessible and easier to apply',
  #description = 'ktrain is a lightweight wrapper for TensorFlow Keras to help train neural networks',
  long_description = readme,
  long_description_content_type = 'text/markdown',
  author = 'Arun S. Maiya',
  author_email = 'arun@maiya.net',
  url = 'https://github.com/amaiya/ktrain',
  keywords = ['tensorflow', 'keras', 'deep learning', 'machine learning'],
  install_requires=[
          #tf_version_str, # removed TensorFlow dependency in v0.20.3
          #'tensorflow_datasets',
          #'scipy==1.4.1', # removed due to https://github.com/tensorflow/tensorflow/commit/78026d6a66f7f0fc
          #'pillow'
          'scikit-learn>=0.21.3', # previously pinned to 0.21.3 due to TextPredictor.explain, but no longer needed as of 0.19.7
          'matplotlib >= 3.0.0',
          'pandas >= 1.0.1',
          'fastprogress >= 0.1.21',
          'keras_bert>=0.81.0',
          'requests',
          'joblib',
          'langdetect',
          'jieba',
          'cchardet',  # previously pinned to 2.1.5 (due to this issue: https://github.com/PyYoshi/cChardet/issues/61) but no longer needed
          'networkx>=2.3',
          'bokeh',
          'seqeval',
          'packaging',
          'transformers>=3.1.0', # due to breaking change in v3.1.0
          'ipython',
          'syntok',
          'whoosh',
          # these libraries are manually installed on-the-fly when required by an invoked method
          # 'shap',  # used by TabularPredictor.explain
          #'eli5 >= 0.10.0', # forked version used by TextPredictor.explain and ImagePredictor.explain
          #'stellargraph>=0.8.2', # forked version used by graph module
          #'allennlp', # required for Elmo embeddings since TF2 TF_HUB does not work
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',

    # Pick your license as you wish
    'License :: OSI Approved :: Apache Software License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
