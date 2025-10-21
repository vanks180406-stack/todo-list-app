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

# Danh sách các công việc (bây giờ là list các dictionary)
tasks = []

def add_task(task_name):
    """Thêm công việc mới, mặc định là chưa hoàn thành"""
    tasks.append({'name': task_name, 'completed': False})

def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành"""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã đánh dấu '{tasks[task_index]['name']}' là hoàn thành!")
    else:
        print("❌ Chỉ số công việc không hợp lệ!")

def list_tasks():
    """Liệt kê tất cả công việc, hiển thị trạng thái [x]/[ ]"""
    if not tasks:
        print("Danh sách công việc trống!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")

if __name__ == "__main__":
    # Thêm vài công việc mẫu
    add_task("Học bài Git")
    add_task("Làm bài tập")

    print("\n📋 Danh sách công việc ban đầu:")
    list_tasks()

    # Đánh dấu công việc 1 là hoàn thành
    complete_task(0)

    print("\n✅ Danh sách sau khi đánh dấu:")
    list_tasks()
