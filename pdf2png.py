
import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
file_path = "1a.pdf"

def pdf2png(file_path): 
    doc = fitz.open(file_path)  # open document
    for i, page in enumerate(doc):
        zoom = 2    # zoom factor
        mat = fitz.Matrix(zoom, zoom)        # Matrix gives better resolution. 
        pix = page.get_pixmap(matrix = mat)  # render page to an image
        pix.save(f"page_{i}.png")

# png', 'pnm', 'pgm', 'ppm', 'pbm', 'pam', 'psd', 'ps', 'jpg', 'jpeg 

if __name__ == "__main__": 
    pdf2png(file_path) 

