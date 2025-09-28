#!/usr/bin/env python3
"""
在庫状況表示機能のテストスクリプト
"""

import sys
import os

# プロジェクトのルートディレクトリをPythonパスに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Streamlitをテスト環境でモック
class MockStreamlit:
    def warning(self, message):
        print(f"WARNING: {message}")
    
    def error(self, message):
        print(f"ERROR: {message}")
    
    def success(self, message):
        print(f"SUCCESS: {message}")

# streamlitをモック
sys.modules['streamlit'] = MockStreamlit()

# constants及びcomponentsモジュールをインポート
import constants as ct
import components as cn

def test_stock_status_display():
    """
    在庫状況表示のテスト
    """
    print("=== 在庫状況表示テスト（定数使用版） ===\n")
    
    # 残りわずかのテスト
    print("1. 「残りわずか」のテスト:")
    cn.display_stock_status(ct.STOCK_STATUS_LOW)
    print()
    
    # 在庫なしのテスト
    print("2. 「なし」のテスト:")
    cn.display_stock_status(ct.STOCK_STATUS_OUT)
    print()
    
    # 在庫ありのテスト
    print("3. 「あり」のテスト:")
    cn.display_stock_status(ct.STOCK_STATUS_AVAILABLE)
    print()
    
    print("=== 定数値の確認 ===")
    print(f"STOCK_STATUS_LOW = '{ct.STOCK_STATUS_LOW}'")
    print(f"STOCK_STATUS_OUT = '{ct.STOCK_STATUS_OUT}'")
    print(f"STOCK_STATUS_AVAILABLE = '{ct.STOCK_STATUS_AVAILABLE}'")
    print(f"STOCK_ICON_WARNING = '{ct.STOCK_ICON_WARNING}'")
    print(f"STOCK_ICON_ERROR = '{ct.STOCK_ICON_ERROR}'")
    print(f"STOCK_ICON_SUCCESS = '{ct.STOCK_ICON_SUCCESS}'")
    
    print("\n=== テスト完了 ===")

if __name__ == "__main__":
    test_stock_status_display()