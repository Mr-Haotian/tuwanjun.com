from threading import Thread
import zipfile
import os


def unzip(filename, unzippath):
    if zipfile.is_zipfile(filename):
        z = zipfile.ZipFile(filename)
        z.extractall(path = unzippath)
        z.close()
        print('已解压%s' % file)


def rename():
    for i in os.listdir(UnZipPath):
        if i !='.DS_Store':
            z = i.encode('cp437', errors = 'ignore').decode('gbk', errors = 'ignore')
            os.rename(UnZipPath+i, UnZipPath+z)
            print('原名:%s ------>修正:%s'%(i, z))

if __name__ == '__main__':
    ZipPath = '../zip_dir/'
    UnZipPath = '../images_dir/'
    for file in os.listdir(ZipPath):
        t = Thread(target=unzip,args=(ZipPath+file,UnZipPath,))
        t.start()
        t.join()
    rename()