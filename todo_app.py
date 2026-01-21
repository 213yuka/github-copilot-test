#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡単なTo Doアプリ
コマンドラインで動作するシンプルなタスク管理アプリケーション
"""

import json
import os
from datetime import datetime


class TodoApp:
    """To Doアプリのメインクラス"""
    
    def __init__(self, filename='tasks.json'):
        """
        初期化
        
        Args:
            filename: タスクを保存するJSONファイル名
        """
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """JSONファイルからタスクを読み込む"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_tasks(self):
        """タスクをJSONファイルに保存"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
    
    def add_task(self, description):
        """
        新しいタスクを追加
        
        Args:
            description: タスクの説明
        """
        # 既存の最大IDを取得し、+1する
        max_id = max([task['id'] for task in self.tasks], default=0)
        task = {
            'id': max_id + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ タスクを追加しました: {description}")
    
    def list_tasks(self):
        """すべてのタスクを表示"""
        if not self.tasks:
            print("\nタスクはありません。")
            return
        
        print("\n=== To Doリスト ===")
        for task in self.tasks:
            status = "✓" if task['completed'] else "□"
            print(f"{task['id']}. {status} {task['description']}")
    
    def complete_task(self, task_id):
        """
        タスクを完了にする
        
        Args:
            task_id: タスクのID
        """
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"✓ タスクを完了しました: {task['description']}")
                return
        print(f"✗ ID {task_id} のタスクが見つかりません。")
    
    def delete_task(self, task_id):
        """
        タスクを削除
        
        Args:
            task_id: タスクのID
        """
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"✓ タスクを削除しました: {deleted_task['description']}")
                return
        print(f"✗ ID {task_id} のタスクが見つかりません。")
    
    def show_menu(self):
        """メニューを表示"""
        print("\n=== To Doアプリ ===")
        print("1. タスクを追加")
        print("2. タスク一覧を表示")
        print("3. タスクを完了")
        print("4. タスクを削除")
        print("5. 終了")
    
    def run(self):
        """アプリを実行"""
        print("To Doアプリへようこそ！")
        
        while True:
            self.show_menu()
            choice = input("\n選択してください (1-5): ").strip()
            
            if choice == '1':
                description = input("タスクの内容: ").strip()
                if description:
                    self.add_task(description)
                else:
                    print("✗ タスクの内容を入力してください。")
            
            elif choice == '2':
                self.list_tasks()
            
            elif choice == '3':
                self.list_tasks()
                try:
                    task_id = int(input("\n完了するタスクのID: ").strip())
                    self.complete_task(task_id)
                except ValueError:
                    print("✗ 有効な数字を入力してください。")
            
            elif choice == '4':
                self.list_tasks()
                try:
                    task_id = int(input("\n削除するタスクのID: ").strip())
                    self.delete_task(task_id)
                except ValueError:
                    print("✗ 有効な数字を入力してください。")
            
            elif choice == '5':
                print("\nTo Doアプリを終了します。お疲れ様でした！")
                break
            
            else:
                print("✗ 1から5の数字を選択してください。")


if __name__ == '__main__':
    app = TodoApp()
    app.run()
