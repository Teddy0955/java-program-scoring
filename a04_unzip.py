import zipfile
import os
import shutil  # 用於刪除資料夾
import sys

def unzip_file(zip_file, extract_to=None):
    """解壓縮單個 ZIP 檔案到指定目錄或檔案所在目錄"""
    extract_to = extract_to or os.path.dirname(zip_file)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"檔案已解壓縮至: {extract_to}")
    # 在解壓縮完成後重命名文件或目錄
    rename_extracted_items(extract_to)

def rename_extracted_items(directory):
    """遍歷目錄，重命名所有文件和子目錄，只保留名字的第一部分"""
    for root, dirs, files in os.walk(directory, topdown=False):
        # 先重命名文件，避免與目錄重名導致問題
        for name in files:
            new_name = name.split()[0]
            if new_name != name:
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
                print(f"重命名檔案：{name} -> {new_name}")
        
        # 重命名目錄
        for name in dirs:
            new_name = name.split()[0]
            new_path = os.path.join(root, new_name)
            old_path = os.path.join(root, name)
            if new_name != name:
                # 如果新目錄已存在，則先刪除原目錄
                if os.path.exists(new_path):
                    shutil.rmtree(old_path)
                    print(f"刪除未改名的資料夾：{old_path}")
                else:
                    os.rename(old_path, new_path)
                    print(f"重命名資料夾：{name} -> {new_name}")

def unzip_files_in_folder(folder):
    """遍歷目錄下的所有檔案，如果是 ZIP 則解壓縮"""
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                print(f"找到 ZIP 檔案: {zip_path}")
                unzip_file(zip_path, root)

def main(zip_file):
    """主函數，先解壓縮指定的 ZIP 檔案，然後遍歷解壓縮出來的目錄尋找並解壓縮 ZIP 檔案"""
    if zipfile.is_zipfile(zip_file):
        unzip_file(zip_file, os.getcwd())
        unzip_files_in_folder(os.getcwd())
    else:
        print("提供的檔案不是 ZIP 格式。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("請提供 ZIP 檔案名稱作為命令行參數。")
    else:
        zip_file = sys.argv[1]
        main(zip_file)