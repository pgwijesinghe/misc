from PyPDF2 import PdfReader, PdfWriter
import fillpdf
from fillpdf import fillpdfs

reader = PdfReader("./wedding/form.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()
writer.add_page(page)
'''
print(fields)
fieldAttributes = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name', '/TU': 'Alternate Field Name',
                   '/TM': 'Mapping Name', '/Ff': 'Field Flags', '/V': 'Value', '/DV': 'Default Value'}
link: {issue} https://stackoverflow.com/questions/47288578/pdf-form-filled-with-pypdf2-does-not-show-in-print
https://pypi.org/project/fillpdf/
'''

names = ['abc', 'def', 'ghi']

for name in names:
    writer.update_page_form_field_values(writer.pages[0], {'Text-77WGBU-cMt': name})

    with open(f"./wedding/{name}.pdf", "wb") as output_stream:
        writer.write(output_stream)
    fillpdfs.flatten_pdf(f"./wedding/{name}.pdf", f"./wedding/{name}1.pdf")