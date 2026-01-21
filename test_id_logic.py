#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID割り当てロジックの追加テスト
削除後のID重複を確認
"""

import os
import sys
from todo_app import TodoApp

TEST_FILE = 'test_id_logic.json'

def test_id_assignment():
    """ID割り当てロジックをテスト"""
    
    # クリーンアップ
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    print("=== ID割り当てロジックのテスト ===\n")
    
    app = TodoApp(filename=TEST_FILE)
    
    # ステップ1: 3つのタスクを追加
    print("ステップ1: 3つのタスクを追加")
    app.add_task("タスク1")
    app.add_task("タスク2")
    app.add_task("タスク3")
    app.list_tasks()
    assert app.tasks[0]['id'] == 1
    assert app.tasks[1]['id'] == 2
    assert app.tasks[2]['id'] == 3
    print("✓ ID: 1, 2, 3\n")
    
    # ステップ2: 中間のタスク(ID=2)を削除
    print("ステップ2: ID=2のタスクを削除")
    app.delete_task(2)
    app.list_tasks()
    assert len(app.tasks) == 2
    assert app.tasks[0]['id'] == 1
    assert app.tasks[1]['id'] == 3
    print("✓ 残りのID: 1, 3\n")
    
    # ステップ3: 新しいタスクを追加
    print("ステップ3: 新しいタスクを追加")
    app.add_task("タスク4")
    app.list_tasks()
    assert len(app.tasks) == 3
    assert app.tasks[0]['id'] == 1
    assert app.tasks[1]['id'] == 3
    assert app.tasks[2]['id'] == 4  # 重複なし！
    print("✓ ID: 1, 3, 4 (重複なし！)\n")
    
    # ステップ4: 最初のタスクを削除
    print("ステップ4: ID=1のタスクを削除")
    app.delete_task(1)
    app.list_tasks()
    assert len(app.tasks) == 2
    assert app.tasks[0]['id'] == 3
    assert app.tasks[1]['id'] == 4
    print("✓ 残りのID: 3, 4\n")
    
    # ステップ5: さらに新しいタスクを追加
    print("ステップ5: さらに新しいタスクを追加")
    app.add_task("タスク5")
    app.list_tasks()
    assert len(app.tasks) == 3
    assert app.tasks[0]['id'] == 3
    assert app.tasks[1]['id'] == 4
    assert app.tasks[2]['id'] == 5
    print("✓ ID: 3, 4, 5 (正しく採番！)\n")
    
    # クリーンアップ
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    print("=== すべてのID割り当てテストが成功！ ===")
    return True


if __name__ == '__main__':
    try:
        test_id_assignment()
        sys.exit(0)
    except AssertionError as e:
        print(f"\n✗ テスト失敗: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ エラー: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
