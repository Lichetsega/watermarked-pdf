import pypdf
template=pypdf.PdfReader(open('super.pdf','rb'))
watermark=pypdf.PdfReader(open('wtr.pdf','rb'))
output=pypdf.PdfWriter()
for i in range(len(template.pages)):
    page=template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)
with open("watermarked.pdf","wb") as outputfile:
    output.write(outputfile)
