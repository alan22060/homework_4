print('Building our static site')

#Reads in the top.html
print('Readin in html variables')
top_html = open('./templates/top.html').read()


#Reads in the botton.html
botton_html = open('./templates/bottom.html').read()

#Reads in the middle index.html

middle_html = open('./content/index.html').read()

print('combining HTML')
combined_html = top_html +  middle_html + botton_html
# print(combined_html)

#Reads in the middle index.html

middle_html = open('./content/index.html').read()


import glob
all_html_files = glob.glob("content/*.html")
print(all_html_files)

import os
file_path = "content/index.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)
print(extension)

output_folder = "docs/" + file_name
print(output_folder)


page = {
  "filename": file_path,
   "title": name_only,
  "output": output_folder
}
print(page)




