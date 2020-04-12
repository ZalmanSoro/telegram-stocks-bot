import plotly.express as px


def get_img():
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    path = "./temp.html"
    fig.write_html(path)
    file = open(path)
    content = file.read()
    file.close()
    print(content)
    return content
