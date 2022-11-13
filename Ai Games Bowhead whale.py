import os
import sys
import numpy as np
import fnmatch
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import pandas

import time 


model = tf.keras.models.load_model("hXception_e4_20epoch.h5")
# Create application
app = QtWidgets.QApplication(sys.argv)


# Dark style
app.setStyle('Fusion')
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
     
palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
app.setPalette(palette)

# Create form and init UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Hook logic
# To prevent TensorFlow from making an error
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#filePath = []
dirPath = []
top_1 =[]
top_2 =[]
top_3 =[]
top_4 =[]
top_5 =[]

def setImage():
    '''
    Loading images
    '''
    global dirPath
    folderpath = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Folder')
   
    if folderpath:
        dirPath = [folderpath]
        #pixmap = QtGui.QPixmap(fileName)
        #ui.label.setPixmap(pixmap)
        #ui.label.setAlignment(QtCore.Qt.AlignCenter)

def predictImage():
    '''
    Image prediction
    '''
    
    global dirPath, model, top_list

    if dirPath !=[]:
        dirName = dirPath[0].split("/")[-1]
        print(dirName)
        image_size = (299, 299)
        start = time.time() ## точка отсчета времени
        ##код программы
        ui.label.setText(f'Select folder: {dirName}\t\nTop Predict:\t\n1)\t\n2)\t\n3)\t\n4)\t\n5)')
        time.sleep(0.2)
        count = len(fnmatch.filter(os.listdir(dirPath[0]), '*.jp*'))
        sumPredict =[]
        now = 0
        
        for file in os.listdir(dirPath[0]):
            if (file.endswith(".jpg") or file.endswith(".jpeg")):
                img = image.load_img((dirPath[0]+"/"+file), target_size=image_size)
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
            #x = x/255
                images = np.vstack([x])    
                prediction = model.predict(images)
                #print(prediction[0])
                a = prediction[0]
                if now == 0:
                    sumPredict=a
                else:
                    sumPredict = sumPredict+a

                id_top = sorted(range(len(a)), key=lambda i: a[i])[-5:]
                id_top[:]=[i+1 for i in id_top]
                id_top.reverse()
                #print(id_top)
                now +=1
                if now == 150:
                    break
                # setting value to progress bar
                ui.pbar.setValue(int(now*100/count))
                time.sleep(0.05)
                #print(f'Progress : ======= {now}/{count}')


        print(f'Progress : ======= {count}/{count}')
        end = time.time() - start ## собственно время работы программы
        #print(end) ## вывод времени

        #print(sumPredict)
        total_top = sorted(range(len(sumPredict)), key=lambda i: sumPredict[i])[-5:]
        total_top[:]=[i+1 for i in total_top]
        total_top.reverse()
        #print(total_top)
        text = "\t\nTop Predict:"
        for idx, x in enumerate(total_top):
            text += f'\t\n{idx+1}) {x}'
        ui.label.setText(f'Select folder: {dirName}{text}')
        time.sleep(0.2)
        top_1.append(total_top[0])
        top_2.append(total_top[1])
        top_3.append(total_top[2])
        top_4.append(total_top[3])
        top_5.append(total_top[4])
    else:
        ui.label.setText(f'Select folder: Не выбрано \t\nTop Predict:\t\n1)\t\n2)\t\n3)\t\n4)\t\n5)')


def createCsv():
    '''
    create Csv prediction
    '''
    global dirPath, top_1, top_2, top_3, top_4, top_5
    if top_1 ==[]:
        if dirPath !=[]:
            content = os.listdir(dirPath[0])
            global_dir = dirPath[0]
            for folder in content:
                dirPath = [global_dir+"/"+folder]
                #time.sleep(0.2)
                predictImage()
            df = pandas.DataFrame(data={"name": content, "top1": top_1, "top2": top_2, "top3": top_3, "top4": top_4, "top5": top_5})
            
            dirName = global_dir.split("/")[-1]
            #df.to_csv(f"./{dirName}-solution.csv", sep=',',index=False)
            df.to_csv(f"./AI_gamers.csv", sep=';',index=False)
            
        else:
            ui.label.setText(f'Select folder: Не выбрано \t\nTop Predict:\t\n1)\t\n2)\t\n3)\t\n4)\t\n5)')

    else:
        top_1, top_2, top_3, top_4, top_5 = [],[],[],[],[]
        dirPath =[]
        ui.label.setText(f'Select folder: Не выбрано \t\nTop Predict:\t\n1)\t\n2)\t\n3)\t\n4)\t\n5)')


    


ui.pushButton.clicked.connect(setImage)
ui.pushButton_2.clicked.connect(predictImage)
ui.pushButton_3.clicked.connect(createCsv)

# Run main loop
sys.exit(app.exec_())
