import aspose.words as aw
import sys as sys

arquivoDOC=sys.argv[1]
arquivoPDF= arquivoDOC.replace('docx','pdf')

doc = aw.Document(arquivoDOC)
doc.save(arquivoPDF)