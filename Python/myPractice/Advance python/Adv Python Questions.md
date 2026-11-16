Here are 5 advanced, real-world Python problems for each of the categories you requested (**Lambda, Map, Filter, List Comprehensions, Set Comprehensions, and Dictionary Comprehensions**).

---

### 1. Lambda Functions

1. **Multi-Key Sorting:** Given a list of dictionaries representing products (`{'name': str, 'price': float, 'rating': float}`), use `sorted()` with a lambda key to sort them primarily by `rating` in descending order, and secondarily by `price` in ascending order.
2. **Conditional Max Element:** Given a list of tuples containing numeric values, use `max()` with a custom lambda function to find the tuple that has the highest product of its elements.
3. **Dynamic Multiplier Factory:** Write a higher-order function `multiplier(n)` that returns a lambda function multiplying its input by `n`. Use it to generate a function that triples numbers.
4. **String Length Reduction:** Use `reduce()` from the `functools` module combined with a lambda function to find the longest string in a list of words.
5. **Custom Filtering Predicate:** Create a lambda function that checks if a number is both a multiple of 3 and not a multiple of 5, and pass it to a list filter operation.

---

### 2. `map()` Function

1. **Polynomial Evaluator:** Given a list of coefficients $[a, b, c]$ and a list of $x$-values, use `map()` with a lambda to compute the quadratic polynomial result $ax^2 + bx + c$ for each $x$.
2. **Name Formatter:** Given a list of full name strings in lowercase (e.g., `"john doe"`), use `map()` to transform them into title-cased initials and last names (e.g., `"J. Doe"`).
3. **Currency Conversion & Formatting:** Given a list of float transaction amounts, use `map()` to apply an exchange rate and format each result into a currency string (e.g., `"$1,234.56"`).
4. **Parallel List Combination:** Use `map()` with multiple iterables to perform element-wise string concatenation of two lists of differing lengths/types into formatted summary strings.
5. **Date String Parser:** Given a list of date strings in various formats, use `map()` combined with `datetime.strptime` to normalize them into standard `datetime` objects.

---

### 3. `filter()` Function

1. **Prime Number Extraction:** Given a list of integers, use `filter()` with a custom helper function to extract only the prime numbers.
2. **Log Level Filtering:** Given a list of log entry dictionaries containing `'level'` and `'message'`, use `filter()` to retain only entries where the level is `'ERROR'` or `'CRITICAL'`.
3. **Student Grade Threshold:** Given a list of student records stored as tuples `(name, [grades_list])`, use `filter()` to retain students whose overall grade average is strictly above 85.
4. **Anagram Removal:** Given a target word and a list of candidate strings, use `filter()` to remove all words from the list that are anagrams of the target.
5. **Valid IPv4 Validation:** Use `filter()` with a regular expression check to filter a list of strings and keep only those that represent valid IPv4 addresses.

---

### 4. List Comprehensions

1. **Matrix Transposition:** Write a single-line list comprehension to transpose a given $M \times N$ matrix (a 2D list).
2. **Pythagorean Triples:** Generate a list of all unique Pythagorean triples $(a, b, c)$ where $a^2 + b^2 = c^2$ and $c \le 50$.
3. **Deep List Flattening:** Flatten a nested list of lists (up to 2 levels deep) while keeping only even numbers.
4. **Pascal's Triangle:** Generate the first $N$ rows of Pascal's Triangle using nested list comprehensions.
5. **Moving Average:** Given a list of numbers and a window size $k$, use a list comprehension to compute the moving averages.

---

### 5. Set Comprehensions

1. **Unique Vowel Harvester:** Given a list of sentences, use a set comprehension to find all unique vowels used across all sentences, ignoring case and whitespace.
2. **Duplicate Finder:** Given a list of integers, use a set comprehension to extract only the numbers that appear more than once (duplicates).
3. **Common Characters:** Given a list of strings, use a set comprehension (with set intersection) to find all unique characters that appear in *every* string.
4. **Dice Roll Prime Sums:** Generate a set of all possible sums of two dice rolls where the resulting sum is a prime number.
5. **Domain Extractor:** Given a list of email addresses, use a set comprehension to extract all unique domain names (e.g., `gmail.com`, `yahoo.com`).

---

### 6. Dictionary Comprehensions

1. **Dictionary Inversion with Grouping:** Invert a dictionary (swap keys and values), ensuring that if multiple keys map to the same value, the values are grouped into a list.
2. **Character Frequency Counter:** Given a string, use a dictionary comprehension to map each unique character to its frequency count.
3. **Price Threshold & Conversion:** Given a dictionary mapping product names to prices in USD, create a new dictionary containing only products priced above $50, with their prices converted to Euros.
4. **Multiplication Table Grid:** Create a dictionary where keys are coordinate tuples `(i, j)` for $1 \le i, j \le 5$ and values are their products ($i \times j$).
5. **Employee Department Grouping:** Given a list of employee dictionaries (`{'name': str, 'department': str}`), use a dictionary comprehension/grouping technique to map each department to a list of employee names.

---





