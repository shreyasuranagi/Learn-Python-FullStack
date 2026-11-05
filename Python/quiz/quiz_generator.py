import random
import html
from pathlib import Path


# ============================================================
# SETTINGS
# ============================================================

SOURCE_FILE = "set_methods.txt"
OUTPUT_FILE = "set_quiz.html"

# Number of questions to randomly select
NUMBER_OF_QUESTIONS = 10


# ============================================================
# LOAD QUESTIONS
# ============================================================

def load_questions(filename):
    questions = []

    path = Path(filename)

    if not path.exists():
        print(f"ERROR: File '{filename}' was not found.")
        return questions

    with open(path, "r", encoding="utf-8") as file:

        for line_number, line in enumerate(file, start=1):

            line = line.strip()

            # Ignore blank lines
            if not line:
                continue

            # Ignore comments
            if line.startswith("#"):
                continue

            # Must contain a comma
            if "," not in line:
                print(
                    f"WARNING: Skipping line {line_number}: "
                    f"no comma found."
                )
                continue

            # Split only at the FIRST comma
            question, answer = line.split(",", 1)

            question = question.strip()
            answer = answer.strip()

            if not question or not answer:
                print(
                    f"WARNING: Skipping line {line_number}: "
                    f"empty question or answer."
                )
                continue

            questions.append((question, answer))

    return questions


# ============================================================
# RANDOM QUESTION SELECTION
# ============================================================

def select_questions(questions, number):

    if not questions:
        return []

    number = min(number, len(questions))

    # Select without duplicates
    selected = random.sample(questions, number)

    # Extra shuffle for clarity
    random.shuffle(selected)

    return selected


# ============================================================
# GENERATE HTML
# ============================================================

def generate_html(questions):

    question_elements = []

    for index, (question, answer) in enumerate(questions, start=1):

        safe_question = html.escape(question)
        safe_answer = html.escape(answer)

        question_elements.append(f"""
        <div class="question">

            <span class="number">{index}.</span>

            <span
                class="question-text"
                tabindex="0"
                role="button"
                aria-label="Show answer"
                onclick="toggleAnswer(this)"
                onkeydown="handleKey(event, this)"
            >{safe_question}</span>

            <span class="answer">{safe_answer}</span>

        </div>
        """)

    questions_html = "\n".join(question_elements)


    # ========================================================
    # COMPLETE HTML
    # ========================================================

    page = f"""<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Python Quiz</title>


    <style>

        * {{
            box-sizing: border-box;
        }}


        body {{
            margin: 20px;

            background: white;

            color: #222;

            font-family:
                Arial,
                Helvetica,
                sans-serif;

            font-size: 18px;
        }}


        /*
         * ALWAYS TWO COLUMNS.
         *
         * This remains two columns even on mobile.
         */

        .quiz {{
            display: grid;

            grid-template-columns:
                minmax(0, 1fr)
                minmax(0, 1fr);

            column-gap: 35px;

            row-gap: 18px;

            width: 100%;
        }}


        /*
         * Individual question area.
         *
         * There is NO hover behavior here.
         */

        .question {{
            min-width: 0;

            line-height: 1.5;
        }}


        /*
         * Question number is NOT interactive.
         */

        .number {{
            color: #777;

            margin-right: 5px;
        }}


        /*
         * ONLY THIS TEXT is interactive.
         */

        .question-text {{
            cursor: pointer;

            /*
             * Allows long questions to wrap properly.
             */

            overflow-wrap: anywhere;
        }}


        /*
         * Desktop:
         *
         * Hovering over the QUESTION TEXT
         * reveals the answer.
         */

        .question-text:hover + .answer {{
            display: inline;
        }}


        /*
         * Answer is hidden by default.
         */

        .answer {{
            display: none;

            margin-left: 8px;

            color: #16803c;

            font-family:
                Consolas,
                "Courier New",
                monospace;

            overflow-wrap: anywhere;
        }}


        /*
         * JavaScript adds this class when
         * the question is tapped/clicked.
         */

        .answer.show {{
            display: inline;
        }}


        /*
         * Small visual indication when keyboard
         * users focus on the question.
         */

        .question-text:focus {{
            outline: 1px dotted #888;

            outline-offset: 3px;
        }}


        /*
         * MOBILE
         *
         * Keep TWO columns.
         *
         * Reduce spacing/font slightly so it
         * remains usable on narrow screens.
         */

        @media (max-width: 600px) {{

            body {{
                margin: 12px;

                font-size: 15px;
            }}

            .quiz {{
                column-gap: 18px;

                row-gap: 14px;
            }}

            .number {{
                margin-right: 3px;
            }}

            .answer {{
                margin-left: 4px;
            }}

        }}


    </style>

</head>


<body>


    <div class="quiz">

        {questions_html}

    </div>


    <script>

        /*
         * ====================================================
         * MOBILE / CLICK SUPPORT
         * ====================================================
         *
         * Tap/click the QUESTION TEXT to show/hide its answer.
         */

        function toggleAnswer(element) {{

            const answer = element.nextElementSibling;

            answer.classList.toggle("show");

        }}


        /*
         * Keyboard support.
         *
         * Enter or Space will also reveal/hide
         * the answer.
         */

        function handleKey(event, element) {{

            if (
                event.key === "Enter" ||
                event.key === " "
            ) {{

                event.preventDefault();

                toggleAnswer(element);

            }}

        }}

    </script>


</body>

</html>
"""

    return page


# ============================================================
# SAVE HTML
# ============================================================

def save_html(filename, content):

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


# ============================================================
# MAIN
# ============================================================

def main():

    print("Loading questions...")

    questions = load_questions(SOURCE_FILE)

    if not questions:
        print("No valid questions found.")
        return

    print(f"Loaded {len(questions)} questions.")

    selected = select_questions(
        questions,
        NUMBER_OF_QUESTIONS
    )

    print(
        f"Selected {len(selected)} questions."
    )

    html_page = generate_html(selected)

    save_html(
        OUTPUT_FILE,
        html_page
    )

    print()
    print("Quiz created successfully!")
    print(f"Output: {OUTPUT_FILE}")


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()
