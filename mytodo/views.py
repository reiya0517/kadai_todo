from django.shortcuts import render, redirect  # ← redirect を追加
from django.views import View
from .models import Task
from .forms import TaskForm  # ← TaskForm を追加

class IndexView(View):
    def get(self, request):
        incomplete_tasks = Task.objects.filter(complete=False).order_by('start_date')
        complete_tasks = Task.objects.filter(complete=True).order_by('start_date')
        context = {
            'incomplete_tasks': incomplete_tasks,
            'complete_tasks': complete_tasks,
        }
        return render(request, "mytodo/index.html", context)




class AddView(View):
    def get(self, request):
        form = TaskForm()
        # テンプレートのレンダリング処理
        return render(request, "mytodo/add.html",{'form':form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに渡す
        form = TaskForm(request.POST)
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()

        # データが正常であれば
        if is_valid:
            # モデルに登録
            form.save()
            return redirect('/')

        # データが正常じゃない
        return render(request, 'mytodo/add.html', {'form': form})

class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()

        return redirect('/')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm  # モデルフォームを使う場合

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # ← ここで編集したデータが保存される
            return redirect('index')  # 編集後にトップへ戻る
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()  # ← 本当に削除
        return redirect('index')

    return render(request, 'mytodo/delete.html', {'task': task})  # ← 確認画面





# この行は一番下に置く
index = IndexView.as_view()
add = AddView.as_view()
update_task_complete = Update_task_complete.as_view()
