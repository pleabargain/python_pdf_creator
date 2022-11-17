import jinja2
import pdfkit
import pandas as pd
from datetime import datetime

#create a pandas function to open a csv and import the data one field at a time
def open_csv_name(file):
    df = pd.read_csv(file)
    # return first cell as a string
    my_name =  df.iloc[0,0]
    return my_name  
open_csv_name('sample_headers.csv')

my_name = open_csv_name('sample_headers.csv')
item1 = "TV"
item2 = "Couch"
item3 = "Washing Machine"




today_date = datetime.today().strftime(" %Y  %b %d")
print (today_date)

context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3,
           'today_date': today_date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'basic-template.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

#C:\Program Files\wkhtmltopdf
# config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin")
# config = pdfkit.configuration(wkhtmltopdf="Program Files/wkhtmltopdf/bin")
# config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")


# output the pdf
output_pdf = today_date + open_csv_name('sample_headers.csv') + 'pdf_generated.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')