s = "let q = JSON.stringify(%r); console.log(\"s = \" + q + \";\\nprint(s%%s)\")";
print(s%s)