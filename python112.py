# Exercise 8 merge the pdf
import os
from pypdf import pdfWriter

merge = pdfWriter()
folder_path = "pdf_files"
pdf_list = sorted(
    [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
)
for pdf in pdf_list:
    full_path = os.path.join(folder_path,pdf)
    print(f"Adding: {full_path}")
    merge.append(full_path)


output_file = "merged_output.pdf"
merge.write(output_file)
merge.close()
print(f"\nSab PDF kamyabi se '{output_file}' mein merge ho gaye hain")





    