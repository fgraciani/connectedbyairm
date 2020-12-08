import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def compress(path, name):
  zipf = zipfile.ZipFile('data/zip/'+name + '.zip', 'w', zipfile.ZIP_DEFLATED)
  zipdir(path, zipf)
  zipf.close()
  print("Done")