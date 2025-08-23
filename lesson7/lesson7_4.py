from PIL import Image

# 載入圖片
image_path = "bear.jpg"  # 確保圖片與程式碼在同一資料夾下
original_image = Image.open(image_path)

# 裁剪為正方形（中心裁切）
width, height = original_image.size
min_edge = min(width, height)
left = (width - min_edge) / 2
top = (height - min_edge) / 2
right = (width + min_edge) / 2
bottom = (height + min_edge) / 2

cropped_image = original_image.crop((left, top, right, bottom))

# 調整大小為 200x200 像素
resized_image = cropped_image.resize((200, 200))

# 儲存新圖片
resized_image.save("bear_200x200.jpg")