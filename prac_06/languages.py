"""estimate: 15 minutes
actual: 10 minutes

this program demonstrates use of the programminglanguage class.
"""

from programming_language import ProgrammingLanguage


def main():
    """demonstrate the programminglanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic]
    print("the dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
