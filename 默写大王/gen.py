from PyPDF2 import PdfReader, PdfWriter

def remove_page(input_pdf, output_pdf, page_number):
    # 打开原始 PDF 文件
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 将所有页面（除了要删除的页面）写入新文件
    for i in range(len(reader.pages)):
        if i != page_number:  # 跳过要删除的页面
            writer.add_page(reader.pages[i])

    # 将结果保存到新文件
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

# 使用示例
remove_page("input.pdf", "output.pdf", 24)  # 删除第三页
