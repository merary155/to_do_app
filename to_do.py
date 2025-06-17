tasks = []

def add_task():
    while True:
        add = input('追加するタスクを入力してください(quitを入力して終了)：')
        if add == 'quit':
            break
        tasks.append(add)

def edit_task():
    while True:
        try:
            num = int(input('編集するタスクの番号を入力してください：'))
        except ValueError:
            print('数字を入力してください')
            continue
        if 1 <= num <= len(tasks):
            edit = input('編集内容を入力：')
            tasks[num - 1] = edit
            break
        else:
            print('有効な数字を入力してください')
            
def del_task():
    while True:
        try:
            num = int(input('削除するタスクの番号を入力してください：'))
        except ValueError:
            print('数字を入力してください：')
            continue
        if 1 <= num <= len(tasks):
            del tasks[num - 1]
            print('タスクを削除しました')
            break
        else:
            print('有効な数字を入力してください')
            
def show_task():
    print('タスクを表示します')
    for index,task in enumerate(tasks,1):
        print(f'{index}:{task}')
        
def save_tasks():
    with open('tasks.txt','w',encoding = 'utf-8') as f:
        for index,task in enumerate(tasks,1):
            f.write(str(index) + ':' + task + '\n')
        print('タスクを保存しました')
        
def load_file():
    try:
        with open('tasks.txt','r',encoding = 'utf-8') as f:
            for line in f:
                task = line.strip() #strip() は文字列の両端にある空白や改行コードを取り除くメソッド
                if task:
                    task_text = task.split(':',1)[1] 
                    #splitは結果をリストとして取り出す。(':',1)を付けると':'を最初の一回だけ分割する。
                    #例）5:素振り:30分 → ['5','素振り:30分']みたいにしてくれる。[1] はリストの2番目を取り出す
                    #よってこの場合は['素振り:30分']のみを取り出してくれる
                    tasks.append(task_text)
                    print('タスクを追加しました')
    except FileNotFoundError:
        print('タスクは見つかりませんでした')
        
load_file()

while True:
    print('メニューを選んでください')
    try:
        menu = int(input('1:メニューの追加\n2:メニューの編集：\n3:メニューの削除：\n4:メニューの表示：\n5:保存して終了\n6:保存せず終了'))
    except ValueError:
        print('数字を入力してください')
        continue
    if menu == 1:
        add_task()
    elif menu == 2:
        edit_task()
    elif menu == 3:
        del_task()
    elif menu == 4:
        show_task()
    elif menu == 5:
        save_tasks()
        break
    elif menu == 6:
        break
    else:
        print('有効な数字を入力してください')
