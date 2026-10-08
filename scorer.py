"""
scorer.py

judge(question, expects, answer, results) -> bool

A simple substring test: does the "expects" phrase show up in what the
system produced? Case-insensitive. Used by run_eval.py to mark each run
pass/fail automatically instead of leaving the Run columns blank.
"""


def judge(question: str, expects: str, answer: str, results) -> bool:
    if not expects:
        return False
    return expects.strip().lower() in answer.strip().lower()
