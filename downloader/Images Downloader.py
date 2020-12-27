from simple_image_download import simple_image_download as simp

response = simp.simple_image_download()

response.download(keywords='galho, tree branch, arvore, tree', limit=300, extensions={'.jpeg', '.jpg', '.gif', '.png', '.ico'})
