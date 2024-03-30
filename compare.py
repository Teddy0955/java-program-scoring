# import os
# import csv

# def compare_files(file1, file2):
#     """比較兩個文件的內容是否相同"""
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         return f1.read() == f2.read()

# def compare_and_record():
#     """遍歷目錄，比較每個子目錄的.out與上層目錄的.out是否相同，並記錄到CSV檔案"""
#     results = {}  # 初始化結果存儲結構
#     # 獲取當前目錄下所有的檔案和資料夾名稱
#     for folder_name in os.listdir("."):
#         if os.path.isdir(folder_name):  # 確認是否為資料夾
#             results[folder_name] = []  # 為每個資料夾初始化一個結果列表

#     # 對於每一個測試案例
#     for i in range(1, 6):
#         parent_out = os.path.join(os.getcwd(), f"{i}.out")
#         if not os.path.exists(parent_out):
#             print(f"上層目錄的{i}.out文件不存在。")
#             return

#         for folder_name in results.keys():
#             child_out = os.path.join(folder_name, f"{i}.out")
#             # 比較文件並記錄結果
#             results[folder_name].append("correct" if os.path.exists(child_out) and compare_files(parent_out, child_out) else "incorrect")

#     # 將結果記錄到CSV檔案
#     with open("comparison_result.csv", "w", newline="") as csvfile:
#         writer = csv.writer(csvfile)
#         # 寫入表頭
#         writer.writerow(["Student ID", *["Test Case {}".format(i) for i in range(1, 6)]])
#         # 逐行寫入每個目錄的名稱及其對於每個測試案例的比較結果
#         for folder_name, result_list in results.items():
#             writer.writerow([folder_name, *result_list])
#     print("比較結果已記錄到comparison_result.csv文件中。")

# if __name__ == "__main__":
#     compare_and_record()

import os
import csv

# def compare_files(file1, file2):
#     """比較兩個文件的內容是否相同"""
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         return f1.read() == f2.read()

def compare_files(file1, file2):
    """比較兩個文件的內容是否相同，忽略換行"""
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # 使用read()讀取文件內容，然後用replace()去除換行符
        content1 = f1.read().replace('\n', '').replace('\r', '')
        content2 = f2.read().replace('\n', '').replace('\r', '')
        return content1 == content2

def calculate_score(results):
    """根據比較結果計算分數"""
    return results.count("correct") * 20  # 每個correct結果加20分

def compare_and_record():
    """遍歷目錄，比較每個子目錄的.out與上層目錄的.out是否相同，並記錄到CSV檔案，包括分數"""
    results = {}  # 初始化結果存儲結構
    for folder_name in os.listdir("."):
        if os.path.isdir(folder_name):  # 確認是否為資料夾
            results[folder_name] = []  # 為每個資料夾初始化一個結果列表

    for i in range(1, 6):
        parent_out = os.path.join(os.getcwd(), f"{i}.out")
        if not os.path.exists(parent_out):
            print(f"上層目錄的{i}.out文件不存在。")
            return

        for folder_name in results.keys():
            child_out = os.path.join(folder_name, f"{i}.out")
            # 比較文件並記錄結果
            result = "correct" if os.path.exists(child_out) and compare_files(parent_out, child_out) else "incorrect"
            results[folder_name].append(result)

    # 將結果記錄到CSV檔案
    with open("comparison_result.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # 寫入表頭，增加一列為"Score"
        writer.writerow(["Student ID", *["Test Case {}".format(i) for i in range(1, 6)], "Score"])
        # 逐行寫入每個目錄的名稱及其對於每個測試案例的比較結果以及分數
        for folder_name, result_list in results.items():
            score = calculate_score(result_list)  # 計算分數
            writer.writerow([folder_name, *result_list, score])
    print("比較結果已記錄到comparison_result.csv文件中。")

if __name__ == "__main__":
    compare_and_record()
