from fpdf import FPDF
import sys
import os

def main():
    if len(sys.argv)!= 2:
        sys.exit('Path to output file was expected.')
    file_name = sys.argv[1]
    name = input("Your name: ")
    generate_shirtificate(name, file_name)


def generate_shirtificate(name, output_file_path):
    if name in ('', None):
        raise ValueError('Invalid name.')

    if output_file_path in ('', None):
        raise ValueError('Invalid file path.')

    if not output_file_path.endswith('.pdf'):
        raise ValueError('Invalid file extension.')

    pdf = FPDF()
    pdf.add_page()
    pdf.image(os.path.abspath(os.path.dirname(__file__))+'/shirtificate.png', x=20, y=90, w=pdf.epw*0.9)
    pdf.set_font("helvetica", "B", 35)
    pdf.set_text_color(255,0,0)
    pdf.cell(200, 50, "CS50 Shirtificate", align='C')
    pdf.set_font("helvetica", "I", 25)
    pdf.set_text_color(255,255,255)
    pdf.cell(-210, 260, f'{name} took CS50', align='C')
    pdf.output(output_file_path)

if __name__ == "__main__":
    main()
