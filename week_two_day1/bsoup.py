from bs4 import BeautifulSoup

html_doc = """ 
<html>
<head>
<title>Hello World</title>
</head>
<body>
<p> i like python</p>
</body>
</html>
"""



soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)
