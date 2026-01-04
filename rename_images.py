import os
import re

def natural_sort_key(s):
    """
    实现自然排序的关键字函数，例如让 '2.jpg' 排在 '10.jpg' 前面
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def rename_images(folder_path):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"错误：找不到目录 '{folder_path}'")
        return

    # 支持的图片格式
    extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    
    # 获取目录下所有图片文件
    files = [f for f in os.listdir(folder_path) 
             if f.lower().endswith(extensions)]

    # 按照文件名中的数字逻辑进行排序（自然排序）
    files.sort(key=natural_sort_key)

    print(f"开始重命名，共找到 {len(files)} 张图片...")

    # 为了防止重命名冲突（例如把 A 改成 B，但 B 已经存在），
    # 我们先将所有文件重命名为一个临时名称，然后再统一改回数字顺序
    temp_files = []
    for i, filename in enumerate(files, 1):
        old_path = os.path.join(folder_path, filename)
        ext = os.path.splitext(filename)[1] # 获取后缀名
        temp_name = f"temp_rename_{i}{ext}"
        temp_path = os.path.join(folder_path, temp_name)
        
        os.rename(old_path, temp_path)
        temp_files.append((temp_path, i, ext))

    # 第二步：将临时名称改为最终的 1, 2, 3...
    for temp_path, index, ext in temp_files:
        final_name = f"{index}{ext}"
        final_path = os.path.join(folder_path, final_name)
        os.rename(temp_path, final_path)
        print(f"已重命名: {os.path.basename(temp_path)} -> {final_name}")

    print("任务完成！")

if __name__ == "__main__":
    # 指定图片所在的文件夹名称
    target_folder = "images"
    rename_images(target_folder)