#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To Doアプリのテストスクリプト
"""

import os
import sys

# テスト用の一時ファイル名
TEST_FILE = 'test_tasks.json'

# アプリのインポート
from todo_app import TodoApp


def test_todo_app():
    """To Doアプリの基本機能をテスト"""
    
    # 既存のテストファイルがあれば削除
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    print("=== To Doアプリのテスト開始 ===\n")
    
    # アプリのインスタンスを作成
    app = TodoApp(filename=TEST_FILE)
    
    # テスト1: タスクの追加
    print("テスト1: タスクの追加")
    app.add_task("買い物に行く")
    app.add_task("メールを返信する")
    app.add_task("資料を作成する")
    assert len(app.tasks) == 3, "タスクが3つ追加されるべき"
    print("✓ テスト1 成功\n")
    
    # テスト2: タスクの一覧表示
    print("テスト2: タスクの一覧表示")
    app.list_tasks()
    print("✓ テスト2 成功\n")
    
    # テスト3: タスクの完了
    print("テスト3: タスクの完了")
    app.complete_task(1)
    assert app.tasks[0]['completed'] == True, "タスク1が完了になるべき"
    print("✓ テスト3 成功\n")
    
    # テスト4: タスクの削除
    print("テスト4: タスクの削除")
    app.delete_task(2)
    assert len(app.tasks) == 2, "タスクが2つになるべき"
    print("✓ テスト4 成功\n")
    
    # テスト5: データの永続化
    print("テスト5: データの永続化")
    app2 = TodoApp(filename=TEST_FILE)
    assert len(app2.tasks) == 2, "保存されたタスクが2つ読み込まれるべき"
    assert app2.tasks[0]['completed'] == True, "完了状態が保存されるべき"
    print("✓ テスト5 成功\n")
    
    # テスト6: 存在しないタスクの操作
    print("テスト6: 存在しないタスクの操作")
    app.complete_task(999)
    app.delete_task(999)
    print("✓ テスト6 成功\n")
    
    # 最終状態の表示
    print("最終的なタスク一覧:")
    app.list_tasks()
    
    # テストファイルのクリーンアップ
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    print("\n=== すべてのテストが成功しました！ ===")
    return True


if __name__ == '__main__':
    try:
        test_todo_app()
        sys.exit(0)
    except AssertionError as e:
        print(f"\n✗ テスト失敗: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ エラー: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
