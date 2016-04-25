# Cosima Sequence #
SPOILER ALERT: This project may contain spoilers for the BBC TV series, Orphan Black.

## Plot Summary (TL;DR Version) ##
Sarah Manning founds out she is a clone and is seeking answers. She meets a clone, Cosima, who is a geneticist and is aware of their existence. Cosima obtains her DNA sequence and notices a unqiue sequence compared to the rest of the clones. Delphine, Cosima's love interest, states that she knows Cosima's tag # and is somehow encoded in her genome.

## Analysis ##
Okay, so here is what we know. This is Cosima's Tag: 

    324b21 
    
This is the unique sequence that was highligted:

    GCTTGCTT CGAAGGTC GCAAGTGC GAAGCGTG CGTTGGAG CGATGCGA

One thing you can notice here is that squence is 48 nucleotides long. 48 is a multiple of 8 and Cosima's tag is also 6 characters long! Making the assumption that the encoding schema had to be limited to technology that existed 30 years ago, Cosima figures the connection between her tag and her genome was a nucleotide to binary to ASCII conversion. It takes 8 bits to encode a single ASCII character.

So lets work our way backwards to test our analysis. `3` on the ASCII chart has the hex value of `51` which is also `00110011` in binary. Following this assumption, we would match the binary values of `00110011` with the bair pairs of `GCTTGCTT`. Therefore, G and C would be zeroes, and A and T would be ones.

## Method ##
Now, here are the rules that the script follows and to decode clone DNA:

1. Substitutes As and Ts with 1s
1. Substitutes all other letters with 0s
1. Convert each 8-bit part to an integer from base 2
1. Convert each integer to a character
1. Join all the characters

## The Test ##
Lets try it on our sequence:

    $ ./decode.py -g
    Enter Your Genetic Sequence: GCTTGCTTCGAAGGTCGCAAGTGCGAAGCGTGCGTTGGAGCGATGCGA
    324b21

Well, well, well. That is Cosima's tag!
