import json

class ToDoList:
  def __init__(self):
      self.tasks = []

  def exception_handling(self,prompt): #ここで例外処理
      while True:
            try:
                num = int(input(prompt))
                return num
            except ValueError:
                print('数字を入力してください')

  def add_task(self): #タスクを追加
      while True:
          add = input('追加するタスクを入力してください(quitを入力して終了)：')
          if add == 'quit':
              break
          elif add == '':
              print('空白のままです。タスクを入力してください')
              continue
          add_dl = input('期限を入力してください：')
          task = {
              'title':add,
              'deadline':add_dl,
              'done' : False,
          }
          self.tasks.append(task)

  def edit_task(self): #タスクを編集
      while True:
          num = self.exception_handling('編集するタスクの番号を入力してください：')
          if 1 <= num <= len(self.tasks):
              edit = input('編集内容を入力：')
              edit_dl = input('編集する期限を入力してください(期限を変更しない場合はNoと入力):')
              if edit_dl == 'No':
                  edit_dl = self.tasks[num - 1]['deadline']
              self.tasks[num - 1] = {
                  'title':edit,
                  'deadline':edit_dl,
                  'done' : self.tasks[num - 1]['done'],  # 編集時に完了状態は維持
              }
              break
          else:
              print('有効な数字を入力してください')

  def del_task(self): #タスクを削除
      while True:
          num = self.exception_handling('削除するタスクの番号を入力してください：')
          if 1 <= num <= len(self.tasks):
              del self.tasks[num - 1]
              print('タスクを削除しました')
              break
          else:
              print('有効な数字を入力してください')

  def show_task(self): #タスクを表示
      print('タスクを表示します')
      for index,task in enumerate(self.tasks,1):
          status = '完了' if task['done'] else '未完了'
          print(f"{index}:{task['title']} 期限：{task['deadline']} 状態：{status}")

  #tasks[]を文字リストから辞書リストへ変更したのでjsonの読み込みに変更

  # def save_tasks(self): #タスクを保存
  #     with open('tasks.txt','w',encoding = 'utf-8') as f:
  #         for index,task in enumerate(self.tasks,1):
  #             f.write(str(index) + ':' + task + '\n')
  #         print('タスクを保存しました')

  # def load_file(self): #最初にタスクを読み込む
  #     try:
  #         with open('tasks.txt','r',encoding = 'utf-8') as f:
  #             for line in f:
  #                 task = line.strip() #strip() は文字列の両端にある空白や改行コードを取り除くメソッド
  #                 if task:
  #                     task_text = task.split(':',1)[1] 
  #                     #splitは結果をリストとして取り出す。(':',1)を付けると':'を最初の一回だけ分割する。
  #                     #例）5:素振り:30分 → ['5','素振り:30分']みたいにしてくれる。[1] はリストの2番目を取り出す
  #                     #よってこの場合は['素振り:30分']のみを取り出してくれる
  #                     self.tasks.append(task_text)
  #                     print('タスクを追加しました')
  #     except FileNotFoundError:
  #         print('タスクは見つかりませんでした')

  def save_tasks(self):
      with open('tasks.json','w',encoding = 'utf-8') as f:
          json.dump(self.tasks, f, ensure_ascii=False, indent=2)
      print('ファイルを保存しました')

  def load_file(self):
      try:
          with open('tasks.json', 'r', encoding='utf-8') as f:
              self.tasks = json.load(f)
          print('タスクを読み込みました')
      except FileNotFoundError:
          print('ファイルは見つかりませんでした')  

  def complete_task(self):  # ここでタスク完了を設定するメソッドを追加
      while True:
          num = self.exception_handling('完了にするタスクの番号を入力してください：')
          if 1 <= num <= len(self.tasks):
              self.tasks[num - 1]['done'] = True
              print(f"タスク「{self.tasks[num - 1]['title']}」を完了にしました。")
              break
          else:
              print('有効な数字を入力してください')

todo = ToDoList()
todo.load_file()

while True:
  print('メニューを選んでください')
  try:
      menu = int(input('1:タスクの追加：\n2:タスクの編集：\n3:タスクの削除：\n4:タスクの表示：\n5:タスク完了：\n6:保存して終了\n7:保存せず終了\n'))
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
          todo.complete_task()
      else:
          print('タスクはありません')
  elif menu == 6:
      if todo.tasks:
          todo.save_tasks()
      else:
          print('保存するタスクはありません')
      break
  elif menu == 7:
      break
  else:
      print('有効な数字を入力してください')
