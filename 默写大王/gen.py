import argparse
from PyPDF2 import PdfReader, PdfWriter

def remove_page(input_pdf, output_pdf, page_number):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 删除指定页码
    for i in range(len(reader.pages)):
        if i != page_number - 1:  # page_number 从1开始，所以要减去1
            writer.add_page(reader.pages[i])

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description="Remove a page from a PDF file.")
    parser.add_argument("input_pdf", help="The input PDF file")
    parser.add_argument("output_pdf", help="The output PDF file")
    parser.add_argument("page_number", type=int, help="The page number to remove (1-indexed)")
    
    # 解析命令行参数
    args = parser.parse_args()

    # 调用删除页面函数
    remove_page(args.input_pdf, args.output_pdf, args.page_number)
    print(f"Page {args.page_number} has been removed from {args.input_pdf} and saved as {args.output_pdf}")

if __name__ == "__main__":
    main()
