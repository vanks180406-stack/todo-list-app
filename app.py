# todo-list-app
#Một ứng dụng To-Do List đơn giản bằng Python.#
tasks = []
def add_task(task_name):
  """Thêm một công việc mới vào danh sách."""
  tasks.append(task_name)
  print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
  print("Chào mừng đến với ứng dụng To-Do List!")
  add_task("Học bài Git và GitHub")
  add_task("Làm bài tập thực hành ở nhà")
  # app.py

tasks = []

def add_task(task_name):
    """Thêm 1 công việc (ở bước này tasks là list of string)."""
    tasks.append(task_name)

def list_tasks():
    """Liệt kê tất cả công việc, có đánh số thứ tự."""
    if not tasks:
        print("Không có công việc nào trong danh sách.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    # ví dụ khởi tạo dữ liệu ban đầu — bạn có thể thay đổi
    add_task("Học bài Git")
    add_task("Làm bài tập")
    # gọi hàm list_tasks() theo đề
    list_tasks()
