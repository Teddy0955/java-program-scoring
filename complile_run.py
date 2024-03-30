import os

def compile_and_run_files_in_folders():
    # 獲取當前目錄下所有的檔案和資料夾名稱
    for folder_name in os.listdir("."):
        # 確認是否為資料夾
        if os.path.isdir(folder_name):
            parts = folder_name.split()  # 以空格分割資料夾名稱
            if len(parts) == 2 or len(parts) == 1:
                student_id = parts[0]  # 學號為名稱的第一部分
                print(f"Compiling in {folder_name} with student ID {student_id}...")

                # 變更目錄到該資料夾
                os.chdir(folder_name)

                # 動態生成編譯命令，將學號插入到檔名中
                compile_command = f"javac -d . A04_{student_id}.java Coach_{student_id}.java Schedule_{student_id}.java Student_{student_id}.java"
                
                # 執行編譯命令
                os.system(compile_command)
                
                # 動態生成運行命令，將學號插入到類名中
                for i in range(1,6):
                    run_command = f"java assignment.A04_{student_id} < ../{i}.in > {i}.out"
                    # 執行Java檔案
                    os.system(run_command)
                
                # 變更回上層目錄
                os.chdir("..")


if __name__ == "__main__":
    compile_and_run_files_in_folders()