
import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
input_file_path = "1a_book//1a manual chess combinations.pdf"

def pdf2png(input_file_path=input_file_path, output_dir="pages_png"): 
    doc = fitz.open(input_file_path)  # open document
    for i, page in enumerate(doc):
        zoom = 2    # zoom factor
        mat = fitz.Matrix(zoom, zoom)        # Matrix gives better resolution. 
        pix = page.get_pixmap(matrix = mat)  # render page to an image
        pix.save(f"{output_dir}//page_{i}.png") 
        print(f"Saved page_{i}.png in the folder {output_dir}") 

# png', 'pnm', 'pgm', 'ppm', 'pbm', 'pam', 'psd', 'ps', 'jpg', 'jpeg 

if __name__ == "__main__": 
    pdf2png(input_file_path) 

