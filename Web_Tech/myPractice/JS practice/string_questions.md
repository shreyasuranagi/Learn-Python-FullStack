
# JS strings easy level MANUAL coding questions
---
1. reverse string
2. count vowels
3. find non-repeating character
4. remove duplicate characters
5. check anagrams
6. find longest word in sequence
7. frequency of each character
8. capitalize first letter of every word
9. most frequenct character
10. check palindrom
11. run length encoding
12. cheicf if two strings are rotations of each other
13. truncate a string with ellipsis
14. Shift Letters by $K$ Positions (Caesar Cipher)
15. find all substring of a string

---
# JS medium level String METHOD questions
### Some problems may also require loops or arrays along with string methods.

---
1. **Reverse the Order of Words**

Reverse the order of words in a sentence without reversing the individual words.


js
Input: "I love JavaScript"
Output: "JavaScript love I"

2. **Find the Longest Word in a Sentence**

Return the longest word from a given sentence.


js
Input: "I love learning programming"
Output: "programming"

3. **Remove Duplicate Words**

Remove duplicate words from a sentence while maintaining their original order.


js
Input: "java is easy and java is powerful"
Output: "java is easy and powerful"

4. **Find All Words Starting With a Vowel**

Return all words that start with a vowel.


js
Input: "Apple is an amazing orange"
Output: ["Apple", "is", "an", "amazing", "orange"]

5. **Convert a String to Title Case**

Capitalize the first letter of every word and convert the remaining letters to lowercase.


js
Input: "hELLO wORLD javascript"
Output: "Hello World Javascript"

6. **Find the Most Repeated Word**

Find the word that appears most frequently in a sentence.


js
Input: "apple banana apple orange banana apple"
Output: "apple"

7. **Remove a Specific Character From a String**

Remove all occurrences of a given character from a string.


js
Input: "programming"
Character: "g"
Output: "prorammin"

8. **Check Whether Two Strings Are Rotations**

Check whether one string is a rotation of another string.


js
Input: "ABCD", "CDAB"
Output: true

9. **Find the Second Longest Word**

Return the second-longest word in a sentence.


js
Input: "I love JavaScript programming"
Output: "JavaScript"

10.**Compress a String**

Compress consecutive repeated characters by writing each character followed by its count. Return the original string if compression does not make it shorter.


js
Input: "aaabbccccd"
Output: "a3b2c4d1"
Interview practice tip: Try solving all 10 using JavaScript string methods such as split(), join(), slice(), substring(), replace(), replaceAll(), includes(), startsWith(), endsWith(), match() and toLowerCase().

---

### 11. Extract and Format a File Extension

Given a filename string like `"document.report.final.pdf"`:

1. Find the position of the last dot (`.`).
2. Extract the file extension (`"pdf"`).
3. Convert the extension to uppercase (`"PDF"`).

* **Methods to practice:** `lastIndexOf()`, `slice()` (or `substring()`), `toUpperCase()`

---

### 12. Sanitize and Pad User Input

Given a messy phone extension string like `"  402 "`:

1. Remove all leading and trailing whitespace.
2. Pad the front of the string with zeros so it is guaranteed to be 6 digits long (`"000402"`).

* **Methods to practice:** `trim()`, `padStart()`

---

### 13. Mask a Credit Card Number

Given a 16-character credit card string like `"4532718293841029"`:
Create a new string where all characters except the last 4 are replaced with `"*"`, resulting in `"************1029"`.

* **Methods to practice:** `slice()`, `repeat()` (or `padStart()`)

---

### 14. Check Substring Positions (Prefix & Suffix)

Given a URL string like `"[https://example.com/api/v1/users](https://example.com/api/v1/users)"`:

1. Verify if it starts with `"https://"` (returns `true`/`false`).
2. Verify if it ends with `"/users"` (returns `true`/`false`).
3. Check if it contains the substring `"api"` (returns `true`/`false`).

* **Methods to practice:** `startsWith()`, `endsWith()`, `includes()`

---

### 15. Title Case the First Word

Given a sentence string `"javascript is fun"`:

1. Extract the first word (`"javascript"`).
2. Capitalize its first letter while keeping the rest lowercased (`"Javascript"`).
3. Combine it back with the rest of the original sentence (`"Javascript is fun"`).

* **Methods to practice:** `indexOf()`, `slice()`, `charAt()` (or bracket notation `[0]`), `toUpperCase()`

---

### 16. Replace All Target Occurrences

Given a paragraph string `"The cat chased another cat under the dark bridge."`:
Replace **every** occurrence of `"cat"` with `"dog"` without using regular expressions (`RegExp`).

* **Methods to practice:** `replaceAll()` (or a combination of `split()` and `join()`)

---

### 17. Find Character Code and Rebuild

Given the letter `"G"`:

1. Get its ASCII code value (number).
2. Add `3` to that code value.
3. Convert the new number back into a character to find the letter 3 positions ahead in the alphabet (`"J"`).

* **Methods to practice:** `charCodeAt()`, `String.fromCharCode()`

---

### 18. Normalize and Compare Case-Insensitively

Given two strings `str1 = "  Hello World  "` and `str2 = "hello world"`:
Clean both strings by trimming whitespace and normalizing their letter case to check if they represent the exact same text ignoring case/spaces.

* **Methods to practice:** `trim()`, `toLowerCase()` (or `toUpperCase()`)

---

### 19. Truncate Text with an Ellipsis

Given a string `"The quick brown fox jumps over the lazy dog"` and a maximum length of `15`:
If the string length exceeds 15 characters, cut it off at 15 characters and append `"..."` to the end (`"The quick brown..."`). Otherwise, leave it unchanged.

* **Methods to practice:** `length`, `slice()` (or `substring()`), `concat()` (or string interpolation)

---

### 20. Repeat a Custom Separator Pattern

Given a word string `"JS"`:
Use string methods to repeat it 4 times separated by dashes, resulting in `"JS-JS-JS-JS"`.

*(Hint: Avoid ending with a trailing dash like `"JS-JS-JS-JS-"`)*.

* **Methods to practice:** `repeat()`, `slice()` (or `concat()`)

---
---

---
# Real world SCENARIO using string METHODS
---

1. **The Modern Avatar Fallback:** A user has a long full name, but your UI design only has space to display their very first letter. How would you grab the character at the very beginning of the string?
2. **The Username Initial Checker:** A user inputs their username, and you need to validate whether a specific character exists at a precise index position (for example, checking if index `3` is an underscore).
3. **The Unicode Icon Lookup:** You are building an emoji picker or text character inspector. How do you find the Unicode (UTF-16) value of a character at a specific position in a string?
4. **The User Profile Merging:** You have a user's first name stored in one variable and their last name in another, and you need to combine them into a single full name string.
5. **The Live Search Filter:** As a user types a search query into an input box, you need to check if a product title contains that specific substring (case-sensitive).
6. **The First Occurrence Locator:** You are parsing an HTML string and need to find the exact index position where a specific CSS class name first appears.
7. **The File Extension Extractor:** A user uploads a file with multiple dots in the name (e.g., `my.document.pdf`). How do you find the index of the *last* dot to safely extract the file extension?
8. **The URL Slug Generator:** You want to extract a specific portion of a URL path (e.g., grabbing characters from index `5` to `15`) to display as a breadcrumb.
9. **The CSV Data Parser:** A user pastes a comma-separated list of tags into an input field (e.g., `javascript, html, css`), and you need to convert that single string into an array of individual tag strings.
10. **The Legacy Text Truncator:** You are working with an older codebase and need a method similar to `slice()` that extracts characters between two index positions, handling arguments even if the start index is greater than the end index.
11. **The Navigation Header Title Case:** You receive raw category names from an API in lowercase (e.g., `electronics`), but your UI requires them to be fully capitalized.
12. **The Email Normalizer:** Users might type their email address with accidental uppercase letters (e.g., `John.Doe@Example.com`). How do you convert the entire string to lowercase before saving it to your database?
13. **The Form Input Cleaner:** A user accidentally types leading and trailing whitespace into a password or username input field. How do you clean up the string by removing whitespace from both ends?
14. **The Left-Padding Cleanup:** An API returns user input where someone accidentally left extra spaces only at the very beginning of a bio sentence. How do you strip out just those starting spaces?
15. **The Right-Padding Cleanup:** You have a log message that accidentally accumulated trailing spaces at the very end. How do you remove only the trailing whitespace?
16. **The Navigation Breadcrumb Check:** You want to check if the current page URL path begins with `/admin` to conditionally render an admin dashboard header.
17. **The Image Format Validator:** You need to check if an uploaded image file's name ends with `.png` or `.jpg`.
18. **The Loading Bar Visualizer:** You want to repeat a loading character string (like `=-=`) a specific number of times to create a custom progress bar animation.
19. **The Transaction ID Formatter:** You are displaying a transaction ID and need to ensure it is always a certain length (e.g., 8 characters) by padding it with leading zeros if it is too short.
20. **The Receipt Column Alignment:** You are printing a text-based receipt for an e-commerce checkout page, and you need to pad product prices with trailing spaces or characters so they align neatly on the right side.
21. **The Content Moderation Tool:** You are building a blog comment section and need to replace a specific banned word with asterisks (e.g., replacing `"badword"` with `"***"`).
22. **The Global Profanity Filter:** A user's comment contains multiple instances of the same prohibited word. How do you replace *every single occurrence* of that word across the entire string?
23. **The Regular Expression Match Finder:** You want to search a user's bio for a pattern (like a phone number format) and return the index position where the match is found.
24. **The First Regex Extraction:** You want to extract the very first email address found inside a long paragraph of text using a regular expression.
25. **The Global Regex Match Iterator:** You need to extract *all* matching hashtags (e.g., `#webdev`, `#coding`) from a tweet and get detailed iterator results for each match.
26. **The Explicit Object Converter:** You are debugging or writing utility functions where you explicitly need to convert a String object wrapper back into its primitive string primitive value.

---



---
# **senior/INTERVIEW-level questions**
---

1. **The Emoji-Safe Text Truncator:**
You are building a social media feed component that cuts off post previews at 140 characters. However, when using standard index-based extraction, posts containing multi-byte UTF-16 characters like emojis ($\U0001F600$) or complex non-English scripts get corrupted, resulting in broken "surrogate pairs" and stray replacement characters ($\text{}$). How would you safely extract characters up to a limit without splitting surrogate pairs?
2. **The High-Performance Autocomplete Substring Matcher:**
Your team is reviewing a high-traffic search bar where users type rapidly. You notice memory spikes and unnecessary allocations when validating whether a product list contains a search term. Aside from basic inclusion checks, how would you search a string while ignoring case sensitivity without creating expensive temporary lowercase copies of large catalog strings?
3. **The Multi-Format File Upload Sanitizer:**
A user uploads files with messy names containing nested extensions, query parameters, or extra trailing dots (e.g., `archive.tar.gz...`). You need to reliably extract the *deepest* file extension from the end of the string regardless of trailing whitespace or trailing punctuation. Which sequence of parsing strategies would you use?
4. **The Custom Template Engine Variable Interpolation:**
You are writing a lightweight front-end template engine. You need to parse a raw template string, locate the exact index of the *very first* interpolation tag (`{{`), and dynamically extract or replace tokens. If the tag doesn't exist, your function must fail gracefully without throwing. How do you locate and extract this efficiently?
5. **The Deep Configuration Path Locator:**
You are parsing a nested JSON path string representing a deeply nested object state (e.g., `user.preferences.theme.mode`). To update your UI store, you need to find the index of the *last* delimiter (`.`) to separate the final property key from its parent path object. How do you isolate this cleanly?
6. **The Flexible Breadcrumb / Sub-Path Router:**
You are writing a custom client-side router. You receive a full URL pathname and need to slice out a segment dynamically based on variable dynamic parameters (e.g., extracting everything between dynamic start and end markers). How do you handle edge cases where the end index is smaller than the start index, or where indices exceed the string length, without crashing?
7. **The Bulk CSV Data Stream Ingestion:**
You are building a file-upload utility that ingests large CSV string chunks from a client upload. Each row is separated by erratic newline characters (`\r\n` or `\n`). How do you split and sanitize this bulk data stream into clean, trimmed row arrays while discarding empty trailing lines caused by trailing carriage returns?
8. **The Dynamic UI Breadcrumb Path Segmenter:**
You need to extract a specific window of a breadcrumb trail from a legacy string format where negative index counting or reverse positioning from the end of the string is required. How would you grab a specific substring slice working backwards from the end of a path?
9. **The Navigation Category Normalization Pipeline:**
An e-commerce API returns category slugs with mixed casing and inconsistent spacing (e.g., ` mEnS-sHoEs `). Before rendering them into navigation links or matching them against database routes, how do you completely normalize the string by stripping all surrounding whitespace and transforming it to a uniform case?
10. **The Form Input Hygiene & SQL Injection / XSS Sanitization Pre-check:**
Before sending user input to an API, you need to strip accidental leading/trailing spaces or invisible formatting characters from text inputs. Furthermore, you need to verify whether the route path starts with a specific secure protocol or ends with a trusted file extension before rendering untrusted content. Which combination of boundary-cleaning and prefix/suffix validation methods ensures strict safety?
11. **The Custom Progress Bar Animation Engine:**
You are building a custom text-based CLI or terminal progress bar for a developer tooling dashboard. You need to dynamically generate a repeating visual track of blocks (like `[▓▓▓░░░]`) whose length scales based on an ongoing percentage completion state. How do you cleanly generate and pad this repeating visual string?
12. **The Receipt Column Alignment & Receipt Printer Formatter:**
You are building a Point-of-Sale (POS) receipt printing module where product names and prices must align perfectly into fixed-width columns (e.g., exactly 40 characters wide). If a product name is too short, you must pad it with spaces; if a price needs alignment on the right edge, how do you pad it on the left?
13. **The Automated Profanity & PII Redaction Pipeline:**
You are building a compliance tool that scans user-generated chat logs and replaces specific sensitive keywords (like phone numbers, emails, or banned terms) with masked characters (`[REDACTED]`). If a log contains *multiple* instances of the same sensitive token across a massive log string, how do you replace every single occurrence globally and dynamically?
14. **The Analytics Regex Pattern Match Locator & Extractor:**
You are parsing raw telemetry logs to extract session tokens matching a complex alphanumeric pattern. You need to find the exact starting index of the pattern match, extract the matched group, and iterate through *all* subsequent overlapping or sequential occurrences in the log for deep analytics without infinite loop traps. How do you approach this using advanced string matching patterns?
15. **The Wrapper Object Primitive Unboxing:**
You are writing a low-level utility library that normalizes incoming parameters, which might occasionally be passed as explicit `String` object wrappers (created via `new String("hello")`) instead of primitive strings. How do you explicitly unbox these wrapper objects back into raw primitives to prevent strict equality bugs in your business logic?

---




---
# SOLUTION NOTES
---
### HEADING -
#### QUESTION NO.- 
- TRIED:
- MISTAKE-
- FINAL