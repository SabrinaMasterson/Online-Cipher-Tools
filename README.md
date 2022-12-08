# Online-Cipher-Tools
This version can be locally hosted to allow users online access 

This version uses Django to host my two tools, these tools being in the appropriately named tools app. You can run the code with the command: "python3 manage.py runserver" like any other django project.

These tools are meant to be used to help students learn and test their forensics. The cipher tools allow them to uncover or create hidden messages, and the password dictionary can help create a dictionary to aid in password cracking. It is not meant to be used for malicious means, and current functionality is limited.

The cipher tools allows users to: Encode and decode lines of text Offer an explanation and exxample of each cipher Combine two ciphers together to encode or decode text with both Limitations: Special characters and numbers can't be encoded or decoded, and as such the Base64 cipher has limitations in how it can be applied in the combinations of text. Only 5 ciphers are availalbe at this moment.

The password dictionary allow users to: input a word or phrase to search scrapes websites for a definition of the word writes a dictionary of related words and phrases this dictionary does not have spaces between the phrases to aid in hashing or password cracking (for example, the phrase "chicken casserole" has its space removed to become "chickencasserole", as some cracking tools like Hashcat would see the space as a seperator for two words instead of a single phrase) Limitations: Only one website is scraped at this moment, https://www.onelook.com/thesaurus/ and it cannot collect every single page of results, only the first page for each tab.
