#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To Doアプリのデモスクリプト
実際の使用例を示す
"""

import os
from todo_app import TodoApp

# デモ用の一時ファイル
DEMO_FILE = 'demo_tasks.json'

# 既存のデモファイルがあれば削除
if os.path.exists(DEMO_FILE):
    os.remove(DEMO_FILE)

print("=" * 50)
print("To Doアプリ - デモンストレーション")
print("=" * 50)

# アプリのインスタンスを作成
app = TodoApp(filename=DEMO_FILE)

print("\n【ステップ1】タスクを追加")
print("-" * 50)
app.add_task("買い物に行く")
app.add_task("メールを返信する")
app.add_task("プロジェクトの資料を作成する")
app.add_task("ミーティングの準備をする")

print("\n【ステップ2】現在のタスク一覧")
print("-" * 50)
app.list_tasks()

print("\n【ステップ3】タスクを完了にする")
print("-" * 50)
app.complete_task(1)
app.complete_task(3)

print("\n【ステップ4】更新後のタスク一覧")
print("-" * 50)
app.list_tasks()

print("\n【ステップ5】タスクを削除")
print("-" * 50)
app.delete_task(2)

print("\n【ステップ6】最終的なタスク一覧")
print("-" * 50)
app.list_tasks()

print("\n" + "=" * 50)
print("デモ完了！")
print("=" * 50)
print(f"\nタスクは '{DEMO_FILE}' に保存されています。")
print("\n実際のアプリを使うには:")
print("  python todo_app.py")
print("\nを実行してください。")

# デモファイルのクリーンアップ（オプション）
# os.remove(DEMO_FILE)
