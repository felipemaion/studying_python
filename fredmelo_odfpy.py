#pip install odfpy
from odf.opendocument import OpenDocumentText
from odf.text import P

textdoc = OpenDocumentText()
p = P(text="Fred Melo")
textdoc.text.addElement(p)
textdoc.save("fredmelo_odfpy.odt")