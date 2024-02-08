import contextlib
import os
import random
import shutil
import socket
import sys
import webbrowser
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow
import cv2
from PIL import Image
from http.server import SimpleHTTPRequestHandler
from http.server import CGIHTTPRequestHandler
from functools import partial
from http.server import ThreadingHTTPServer
import threading


def start_thread(name, kwargs):
    thread = threading.Thread(target=name, kwargs=kwargs)
    thread.setDaemon(True)
    thread.start()

"规则：\n1. 图片从小到大排列。\n2. 生成按钮会在ready文件夹生成一个可以玩的版本的源文件；\n而部署按钮会将这个版本发送到站点上，让你可以在线上玩。"

class DualStackServer(ThreadingHTTPServer):
    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()

ext = ['.exr', '.webp', '.rgb', '.gif', '.pbm', '.pgm', '.ppm', '.tiff', '.rast', '.xbm', '.jpeg', '.bmp', '.png', '.webp', '.exr', '.jpg']
comparison = [52, 80, 108, 119, 153, 183, 193, 258, 308, 309, 408]
places = [
    "./ready/res/raw-assets/ad/ad16ccdc-975e-4393-ae7b-8ac79c3795f2.png",
    "./ready/res/raw-assets/0c/0cbb3dbb-2a85-42a5-be21-9839611e5af7.png",
    "./ready/res/raw-assets/d0/d0c676e4-0956-4a03-90af-fee028cfabe4.png",
    "./ready/res/raw-assets/74/74237057-2880-4e1f-8a78-6d8ef00a1f5f.png",
    "./ready/res/raw-assets/13/132ded82-3e39-4e2e-bc34-fc934870f84c.png",
    "./ready/res/raw-assets/03/03c33f55-5932-4ff7-896b-814ba3a8edb8.png",
    "./ready/res/raw-assets/66/665a0ec9-6c43-4858-974c-025514f2a0e7.png",
    "./ready/res/raw-assets/84/84bc9d40-83d0-480c-b46a-3ef59e603e14.png",
    "./ready/res/raw-assets/5f/5fa0264d-acbf-4a7b-8923-c106ec3b9215.png",
    "./ready/res/raw-assets/56/564ba620-6a55-4cbe-a5a6-6fa3edd80151.png",
    "./ready/res/raw-assets/50/5035266c-8df3-4236-8d82-a375e97a0d9c.png"
          ]

def circle(img_path, cir_path):
    ima = Image.open(img_path).convert("RGBA")
    size = ima.size
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2))
    r3 = int(r2/2)
    imb = Image.new('RGBA', (r3*2, r3*2),(255,255,255,0))
    pima = ima.load()
    pimb = imb.load()
    r = float(r2/2)
    for i in range(r2):
        for j in range(r2):
            lx = abs(i-r)
            ly = abs(j-r)
            l = (pow(lx,2) + pow(ly,2))** 0.5
            if l < r3:
                pimb[i-(r-r3),j-(r-r3)] = pima[i,j]
    imb.save(cir_path)
    return cir_path

"""
    *                             _ooOoo_
    *                            o8888888o
    *                            88" . "88
    *                            (| -_- |)
    *                            O\ ... /O
    *                         ____/`---'\____
    *                       .'  \\|     |//  `.
    *                      /  \\|||  :  |||//  \
    *                     /  _||||| -:- |||||-  \
    *                     |   | \\\  -  /// |   |
    *                     | \_|  ''\---/''  |   |
    *                     \  .-\__  `-`  ___/-. /
    *                   ___`. .'  /--.--\  `. . __
    *                ."" '<  `.___\_<|>_/___.'  >'"".
    *               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
    *               \  \ `-.   \_ __\ /__ _/   .-` /  /
    *          ======`-.____`-.___\_____/___.-`____.-'======
    *                             `=---='
    *          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    *                     佛祖保佑        永无BUG
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.file = [""] * 11
        self.ui.Opener.clicked.connect(self.opening)
        self.ui.Deployer.clicked.connect(self.deploy)
        self.ui.Generator.clicked.connect(self.generate)
        self.ui.Activator.clicked.connect(self.activate)
        self.ui.About.clicked.connect(self.showAbout)
        self.ui.Remover.clicked.connect(self.remove)
        self.ui.Ruler.clicked.connect(self.rule)
        self.ui.Starter.clicked.connect(self.start)
        self.ui.Deployer.setEnabled(False)
        if os.path.exists("./tmp/"):
            self.ui.Starter.setEnabled(False)
        if os.path.exists("./ready/") == False:
            self.ui.Remover.setEnabled(False)
    
    def activate(self):
        def run(server_class=DualStackServer,
            handler_class=SimpleHTTPRequestHandler,
            port=8000,
            bind='127.0.0.1',
            cgi=False,
            directory=os.getcwd()
            ):
            """Run an HTTP server on port 8000 (or the port argument).

            Args:
                server_class (_type_, optional): Class of server. Defaults to DualStackServer.
                handler_class (_type_, optional): Class of handler. Defaults to SimpleHTTPRequestHandler.
                port (int, optional): Specify alternate port. Defaults to 8000.
                bind (str, optional): Specify alternate bind address. Defaults to '127.0.0.1'.
                cgi (bool, optional): Run as CGI Server. Defaults to False.
                directory (_type_, optional): Specify alternative directory. Defaults to os.getcwd().
            """
            if cgi:
                handler_class = partial(CGIHTTPRequestHandler, directory=directory)
            else:
                handler_class = partial(SimpleHTTPRequestHandler, directory=directory)
            with server_class((bind, port), handler_class) as httpd:
                webbrowser.open("http://127.0.0.1:8000")
                httpd.serve_forever()
        start_thread(run, kwargs={"directory": "./ready"})

    def rule(self):
        QMessageBox.information(self, "食用方法, 务必看完", """
初次启动需要“初始化”，之后不需要，然后“打开”一个装有11张图片的文件夹(其他什么都不要有)。
点击“生成”，然后等待跳出“已完成”提示窗口。
点击“启动”可启动游戏，部署功能还未写完，请勿使用。
生成完毕的游戏代码在"ready"文件夹中，请保管好。
如果要再次生成游戏，请点击“清除缓存”，这会导致上一次生成的游戏文件丢失，请保证自己已保管好。
                                """)
    def start(self):
        os.mkdir("./tmp")
        QMessageBox.information(self, "初始化完成", "初始化完成。")

    def remove(self):
        shutil.rmtree("./ready")
        QMessageBox.information(self, "已清除缓存", "已清除缓存。")

    def generate(self):
        def go():
            shutil.copytree(r'./original', r'./ready')
            for x in range(11):
                circle(self.file[x], "./tmp/"+str(x)+".png")
                img = cv2.imread("./tmp/"+str(x)+".png", cv2.IMREAD_UNCHANGED)
                img = cv2.resize(img, (comparison[x], comparison[x]))
                cv2.imwrite(places[x], img)
        start_thread(go)
        QMessageBox.information(self, "成功", "生成完毕！")
    
    def showAbout(self):
        QMessageBox.information(self, "关于","""
WaterMello v0.1 Beta
开发: 玄云海 OblivionOcean
Special Thanks: liyupi, Fgaoxing.
Enjoy the game, thy life as well.
                                """)

    def opening(self):
        correction = True
        filepath = QFileDialog.getExistingDirectory(self, "打开装有11张图片的文件夹。", ".")
        files = os.listdir(filepath)
        for f in files:
            _, a = os.path.splitext(f)
            if a not in ext:
                correction = False
        if len(files) == 11 and correction:
            for i in files:
                self.file[files.index(i)] = os.path.join(filepath, i)
                print(self.file)
            QMessageBox.information(self, "成功！","已导入图片。")
        else:
            QMessageBox.information(self, "出错！","图片数量过多/过少，图片后缀名错误。")
    
    def deploy(self):
        QMessageBox.information(self, "我饿啦！","把这个功能吃了，下个版本还你们。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())