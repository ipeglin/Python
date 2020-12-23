import os

# Lambda function that clears the console
clear = lambda:os.system("cls")

# Contents for the html file
html_content = '''<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8">
        <title>SideTittel</title>
    </head>
    <body>


        <script src="index.js"></script>
    </body>
</html>
'''


# Creating and writing to index.html file
html_file = open("index.html", "w+")
html_file.write(html_content)
html_file.close()


# Creating JS file
js_file = open("index.js", "w+")
js_file.close()