from PyPDF2 import PdfReader, PdfWriter, generic

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Zoom in or out a PDF file.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input PDF file path.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output PDF file path.')
    parser.add_argument('-s', '--scale', type=float, required=True, help='Zoom scale.')
    args = parser.parse_args()

    zoomer = PDFZoomer(args.input, args.output, args.scale)
    zoomer.zoom()

class PDFZoomer:
    def __init__(self, input_path, output_path, scale):
        self.input_path = input_path
        self.output_path = output_path
        self.scale = scale

    def zoom(self):
        with open(self.input_path, 'rb') as input_file:
            pdf_reader = PdfReader(input_file)
            pdf_writer = PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                media_box = page.mediabox
                new_width = float(media_box.width) - (float(media_box.width) * (1 - 1/self.scale))
                new_height = float(media_box.height) - (float(media_box.height) * (1 - 1/self.scale))
                left_margin = (float(media_box.width) - new_width) / 2
                bottom_margin = (float(media_box.height) - new_height) / 2
                right_margin = float(media_box.width) - new_width - left_margin
                top_margin = float(media_box.height) - new_height - bottom_margin
                new_media_box = generic.RectangleObject([left_margin, bottom_margin, float(media_box.width) - right_margin, float(media_box.height) - top_margin])
                page.cropbox = new_media_box
                pdf_writer.add_page(page)

            with open(self.output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

    