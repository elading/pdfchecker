import os
import shutil
import glob
import re
import sys
import argparse

#Script to check and delete documents with a pdf version
#run with: python slette_doc.py -d /path/to/dir 
file_types = ['.pptx', '.docx']

parser = argparse.ArgumentParser(description='slett dokumenter som har en pdf versjon')
parser.add_argument('-d', '--dir', help='Directory to search in', required=True)
args = parser.parse_args()
dir = args.dir

output_file = open('log_pdfcheck.txt', 'w')

#run for each file_type
for file_type in file_types:
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(file_type):
                #hent pdf filnavn
                pdf_file = glob.glob(root + '/' + file.replace(file_type, '.pdf'))
                if pdf_file: 
                    #slett fil
                    os.remove(root + '/' + file)
                    print('Slettet: ' + file)
                    output_file.write('Slettet: ' + file + '\n')
                else:
                    print('doc uten PDF: ' + file)
                    output_file.write('doc uten PDF: ' + file + '\n')
            else:
                pass


print('Done!')
sys.exit(0)



