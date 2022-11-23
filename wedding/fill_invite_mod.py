'''
This script was written to generate eInvites for my wedding.
Import -> any
Export -> flattened pdf
'''

import os, sys
from fillpdf import fillpdfs

dirPath = os.path.dirname(sys.argv[0])
pdfPath = f"{dirPath}/eInvite_editable.pdf"

def genInvites():
    with open(f'{dirPath}/guest_list.txt', 'r') as guest_list:
        names = guest_list.read().splitlines()

    for name in names:
        data_dict = {'Text-77WGBU-cMt': f'{name}'}
        fillpdfs.write_fillable_pdf(pdfPath, f'{dirPath}/generated/{name}.pdf', data_dict)
        fillpdfs.flatten_pdf(f'{dirPath}/generated/{name}.pdf', f'{dirPath}/generated/{name}.pdf')

if __name__ == "__main__":
    genInvites()
    print("Done!")