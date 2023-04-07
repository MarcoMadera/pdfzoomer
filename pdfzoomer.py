import argparse
from pdfzoomer.zoomer import PDFZoomer

def main():
    parser = argparse.ArgumentParser(description='PDFZoomer')
    parser.add_argument('-input', help='input PDF file path', required=True)
    parser.add_argument('-output', help='output PDF file path', required=True)
    parser.add_argument('-scale', type=int, help='zoom scale', default=2)
    args = parser.parse_args()

    zoomer = PDFZoomer(args.input, args.output, args.scale)
    zoomer.zoom()

if __name__ == '__main__':
    main()