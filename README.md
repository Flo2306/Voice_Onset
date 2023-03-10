# Voice-Onset

This module can be used to estimate word onset data using a method that is based on voice transcription. It works by continuously splitting the audio file until the voice recognition just recognizes the input word. It also allows for words with high similarity (e.g., ship & boat) to be considered correct responses depending on a value you can decide yourself. Now why would you use my approach compared to other approaches available already?

Pro:

- It is similarly accurate to existing approaches (e.g. high correlation r=0.8 with Chronset).
- It allows for automatic target word application (e.g. the picture shown is a boat and only if the said word is "boat", the algorithm will return the onset value)
- It allows for the target word to be semantically related to the shown picture (e.g. the picture shown is a boat and the said word is "ship", the response would still be considered correct)

Con:

- The audio quality plays a big role in how many audio files are classified. Using a computer microphone, we lost about 15% of the data to the voice transcription not recognizing the correct word.
- It can take quite some time as it is splitting the document multiple times (a 5 second recording takes about 5 seconds to process, the algorithm has a complexity of log(n))

The idea for this project came about in a research internship at the University of Sydney. In the experiment, pictures were shown and participants had to name the object they saw. As I was unaware that there were other softwares available (e.g. Chronset), I decided to try and write my own function. I decided to use a binary search + transcribe approach which, to my knowledge, has not been used before this way. I am currently in the process of writing a paper about this and I hope to publish within this year.

The use case I can think of the most is to use it in response time related experiments using verbal responses. It can be used to automate almost the whole process of analyzing data as it returns the onset times and determines whether the word is close enough to the target word/right response. An example of how this could work can be found using the example\_analysis function.

Potential future functions could expand to keyword search in audio recordings as the approach should work for this kind too. Another potential expansion is to implement different ways of voice recognition which could improve the accuracy of the algorithm.

The current members of this module are:

Florian Burger, [flo.burger@sydney.edu.au](mailto:flo.burger@sydney.edu.au)
