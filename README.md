# Braille-Search-Engine
This is a search engine that retrieves the text part of search results and converts them into braille (in a format that can easily be printed using a working braille printer).

The files inside the search engine folder utilize a comparatively inaccurate, slightly simplified logic, of the sort used by most digital translators.

However the translator portion inside the High Accuracy Translator folder utilizes a special algorithm to achieve maximum translation accuracy (because Braille does not map 1:1 with the English alphabet.)
 
res.html is a sample output, supported on Chrome, Opera and Firefox.


(credits to Lazo for help with the mapping algorithm.)
The Algorithm for Translating Alphabet Based Text to Grade 2 Braille:
1. Split up the text into words by dividing them based on whitespace characters.
    - Whitespace includes spaces (' ') and new lines ('\n')
2. For each word, handle the numbers first.
    - Numbers in braille use the same symbols as the first 10 letters of the alphabet.
        - The number '7' and the letter 'g' are both represented by '⠛'.
        - To differentiate between numbers and letters, an escape code (⠼) is placed before groups of numbers.
        - Therefore '7' is actually '⠼⠛' whereas 'g' is only '⠛'.
    - In this step, only the numbers are dealt with, so there will be a mix of both braille and Alphabet symbols.
        - Example: "123-456-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK"
3. Handle the capitals.
    - Similarly to numbers in braille, capital letters need an escape code (⠠).
    - The escape code (⠠) is added to the beginning of each capital letter and the letter is changed to lowercase.
        - Example 1: "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-⠠j⠠u⠠n⠠k". The dashes still remain.
        - Example 2: "Sweet" becomes "⠠sweet". The non-capital letters remain untouched.
4. Trim the word.
    - Sometimes the words extracted contain punctuation attached to them such as commas or brackets.
    - Words need to be trimmed so that they can be converted to contractions.
        - Example: The word "the" is represented by a single braille symbol (⠮).
        - If the word "the" has punctuation around it ("the!") then it will not be interpreted correctly.
        - This is also why capitals are converted to lowercase in step 3 because "The" would not work either.
    - The characters that are trimmed off are called "shavings".
        - Example: In the word "!where?", the shavings are "!?" and the trimmed word is "where".
5. Build the translation.
    a) Check to see if the trimmed word can be contracted.
        - This includes common words like "the", "in", "you" etc...
    b) Translate the remaining characters that are still alphabetic.
    c) Translate the shavings (this will mostly just be punctuation).
        - Exceptions to be mindful of:
            - There is no braille symbol for a generic quote (")
            - There is only open quotation (“) and closed quotation (”).
            - Therefore we must keep track of what the last quotation was to convert it correctly.
