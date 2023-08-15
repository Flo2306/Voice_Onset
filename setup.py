from setuptools import setup

setup(name='Voice_Onset',
      version= "0.1",
      description='A modul that can be used to detemine voice onset times',
      url='https://github.com/Flo2306/Voice_Onset',
      author='Florian Burger',
      author_email='f.burger@uva.nl',
      license='MIT',
      packages=['Voice_Onset'],
      package_data = {'Voice_Onset': ['Sample_Experiment/**']},
      install_requires=[
        'SpeechRecognition',
        'pandas',
        'numpy',
        'glob2', 
        'soundfile',
        'scikit-learn',
        'sentence-transformers',
        'scipy',
        'unipath',
        'numpy'
    ],
    classifiers=[
        "Development Status :: 1 - Trial Setup",
        "Intended Audience :: Science/Research",
        "License :: MIT",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific Research :: Voice Onset/Response Time"
    ],
    keywords="Voice Onset Word Onset Voice Data Analysis Binary Search Word Similarity"
    )
