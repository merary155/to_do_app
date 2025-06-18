class ToDoList:
  def __init__(self):
      self.tasks = []

  def add_task(self):
      while True:
          add = input('追加するタスクを入力してください(quitを入力して終了)：')
          if add == 'quit':
              break
          self.tasks.append(add)

  def edit_task(self):
      while True:
          try:
              num = int(input('編集するタスクの番号を入力してください：'))
          except ValueError:
              print('数字を入力してください')
              continue
          if 1 <= num <= len(self.tasks):
              edit = input('編集内容を入力：')
              self.tasks[num - 1] = edit
              break
          else:
              print('有効な数字を入力してください')

  def del_task(self):
      while True:
          try:
              num = int(input('削除するタスクの番号を入力してください：'))
          except ValueError:
              print('数字を入力してください：')
              continue
          if 1 <= num <= len(self.tasks):
              del self.tasks[num - 1]
              print('タスクを削除しました')
              break
          else:
              print('有効な数字を入力してください')

  def show_task(self):
      print('タスクを表示します')
      for index,task in enumerate(self.tasks,1):
          print(f'{index}:{task}')

  def save_tasks(self):
      with open('tasks.txt','w',encoding = 'utf-8') as f:
          for index,task in enumerate(self.tasks,1):
              f.write(str(index) + ':' + task + '\n')
          print('タスクを保存しました')

  def load_file(self):
      try:
          with open('tasks.txt','r',encoding = 'utf-8') as f:
              for line in f:
                  task = line.strip() #strip() は文字列の両端にある空白や改行コードを取り除くメソッド
                  if task:
                      task_text = task.split(':',1)[1] 
                      #splitは結果をリストとして取り出す。(':',1)を付けると':'を最初の一回だけ分割する。
                      #例）5:素振り:30分 → ['5','素振り:30分']みたいにしてくれる。[1] はリストの2番目を取り出す
                      #よってこの場合は['素振り:30分']のみを取り出してくれる
                      self.tasks.append(task_text)
                      print('タスクを追加しました')
      except FileNotFoundError:
          print('タスクは見つかりませんでした')

todo = ToDoList()
todo.load_file()

while True:
  print('メニューを選んでください')
  try:
      menu = int(input('1:タスクの追加：\n2:タスクの編集：\n3:タスクの削除：\n4:タスクの表示：\n5:保存して終了\n6:保存せず終了\n'))
  except ValueError:
      print('数字を入力してください')
      continue
  if menu == 1:
      todo.add_task()
  elif menu == 2:
      if todo.tasks:
          todo.edit_task()
      else:
          print('タスクはありません')
  elif menu == 3:
      if todo.tasks:
          todo.del_task()
      else:
        print('タスクはありません')
  elif menu == 4:
      if todo.tasks:
          todo.show_task()
      else:
        print('タスクはありません')
  elif menu == 5:
      if todo.tasks:
          todo.save_tasks()
      else:
        print('保存するタスクはありません')
      break
  elif menu == 6:
      break
  else:
      print('有効な数字を入力してください')
