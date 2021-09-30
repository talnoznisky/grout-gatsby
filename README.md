# The Great Groutsby   
## What it's doing

1. Every instance of "great" has been replaced with "grout"

2. Every sentence is pre-sorted by: 
    - its original position in the text, 
    - length, 
    - and alphabetically. 
    
    Each sequence can be reversed as well.

3. When the sentences are re-sorted, they are distributed to each paragraph according to the number of sentences it originally contained.

## Why it's doing these things
1. I saw "the great groutsby" graffitied among other grout puns in the grouting in the mens room of the music building at University of Washington. 
I made [thegreatgroutsby.com](https://thegreatgroutsby.com/) and decided to abstract the code base enough to accomodate the substituion of "grout" for "great" as well.

2. To provide a quasi-ecommerce interface to meritorious literary products like FSG's overwrought sentences. 

3. To extend the discussion of literary structure and literary content by through newly interactive reading and publishing tools.

4. Other reasons I won't go into here. Please email me if you wanna chat about it.

## Some considerations
-  A complete "sentence" is a difficult concept to enforce programmatically, especially in a literary context. Mercifully, The Great Gatsby is grammatically and syntactically conventional.
- Reading a re-sorted draft of The Great Gatsby kind of feels like an Alain Resnais script.
- Simple web design/UX patterns, not just natural language processing tools, are fun models for literary production. And free!

## Thank yous
- [Alex Cabal](https://github.com/acabal) for their stellar reproduction of [The Great Gatsby](https://www.gutenberg.org/files/64317/64317-h/64317-h.htm) into HTML for Project Gutenberg.
- [Jay Kaiser](https://github.com/jayckaiser), my colleague, for alerting me to the [spacy](https://spacy.io/) NLP package and talking me through the current state of the art.
- [BramVanoy](https://github.com/BramVanroy) for sharing their solution to similar sentence boundary detection challenges. I created a pipeline component out of the function you wrote. Thank you so much.
- Whoever graffitied "the great groutsby" among other grout puns in the grouting in the mens room of the music building at University of Washington.

## P.S.
Neither the processing nor web presentation code looks great right now. Please avert your eyes. Refactoring to come.
