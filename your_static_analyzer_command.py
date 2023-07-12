
with open("bug_report.txt", 'w') as f:
    bug_report = "main.py:5: SyntaxError: invalid syntax\nmain.py:10: NameError: name 'x' is not defined"
    f.write(bug_report)

exit(1)