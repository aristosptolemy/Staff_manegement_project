

import win32print
import win32com.client
printer_name = 'EPSON EW-M5071FT Series'


# プリンター名とポート名を取得しフォーマット
printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
target_printer = None
port_name = "Ne01:"  # 仮のポート名を設定
for p in printers:
    if printer_name in p[2]:
        # 可能であればポート名を取得し、空白を削除
        if p[1]:
            port_name = p[1].split(',')[0].strip()
        # プリンター名のフォーマット
        target_printer = f"{p[2]} on {port_name}:"
        break

if target_printer is None:
    raise Exception(f"指定されたプリンターが見つかりません: {printer_name}")

print(f"Using printer: {target_printer}")

# Excelアプリケーションをバックグラウンドで起動
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False  # Excelウィンドウを非表示にする
excel.DisplayAlerts = False  # アラートを非表示にする
# プリンターを設定
excel.ActivePrinter = target_printer
