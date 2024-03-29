from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import views
import sys

YEAR = 1987

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)


parser = views.createParser()
namespace = parser.parse_args(sys.argv[1:])
template = env.get_template('template.html')
excel_data_df = pandas.read_excel(
    namespace.path, na_values=['N/A', 'NA'], keep_default_na=False
    )
products = excel_data_df.to_dict(orient='records')


rendered_page = template.render(
    wines=views.get_wines(products), year=views.years(YEAR)
    )

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
