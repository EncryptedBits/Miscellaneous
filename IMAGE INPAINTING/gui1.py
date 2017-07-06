import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import subprocess

class filedialogdemo(QWidget):
   def __init__(self, parent = None):
      self.fname=""

       
      super(filedialogdemo, self).__init__(parent)
      layout0=QVBoxLayout()


		
      layout = QVBoxLayout()
      self.btn = QPushButton("Select an image")
      #self.btn.clicked.connect(self.getfile)
      #self.connect(self.btn, SIGNAL('clicked()'), self.getfile)
      self.btn.clicked.connect(lambda:self.getfile())
      self.btn.setStyleSheet("background-color: lightblue") 
      layout.addWidget(self.btn)



      temp_layout=QHBoxLayout()
      snr_input_layout=QVBoxLayout()
      self.le = QLabel("Input Image")
      #temp_layout.addWidget(self.le)
      snr_input_layout.addWidget(self.le)
      self.snr_input=QLabel("")
      self.snr_input.setStyleSheet("color: blue;font-size:20px")
      snr_input_layout.addWidget(self.snr_input)
      #temp_layout.addStretch()
      
      temp_layout.addLayout(snr_input_layout)

      temp_layout.addStretch()
      

      snr_output_layout=QVBoxLayout()
      self.lle=QLabel("output Image")
      #temp_layout.addWidget(self.lle)
      snr_output_layout.addWidget(self.lle)
      self.snr_output=QLabel("")
      self.snr_output.setStyleSheet("color: blue;font-size:20px")
      snr_output_layout.addWidget(self.snr_output)
      
      temp_layout.addLayout(snr_output_layout)

      layout.addStretch()
      layout.addLayout(temp_layout)
      #layout.addWidget(self.le)


 
      #self.setLayout(layout)
      layout.setAlignment(Qt.AlignTop)

      
      layout0.addLayout(layout)

      layout1=QHBoxLayout()



      layout2=QVBoxLayout()
      self.le1=QLabel("   Image Enhancement")
      self.le1.setStyleSheet("color: red;font-size:20px")
      layout2.addWidget(self.le1)
      self.le2=QLabel("            Select Algorithm")
      layout2.addStretch()
      layout2.addWidget(self.le2)

      self.btn1 = QPushButton("ContrastEnhancement")
      self.btn1.clicked.connect(lambda:self.ContrastEnhancement('ENHANCEMENT/Contrasting.py',self.fname))
      self.btn1.setStyleSheet("background-color: lightgreen")
      layout2.addStretch()
      layout2.addWidget(self.btn1)

      self.btn2 = QPushButton("HistogramEquilisation")
      self.btn2.clicked.connect(lambda:self.HistogramEquilisation('ENHANCEMENT/histogramEquilisation.py',self.fname))
      self.btn2.setStyleSheet("background-color: lightgreen")
      layout2.addStretch()
      layout2.addWidget(self.btn2)

      self.btn3 = QPushButton("Negative")
      self.btn3.clicked.connect(lambda:self.Negative('ENHANCEMENT/Negative.py',self.fname))
      self.btn3.setStyleSheet("background-color: lightgreen")
      layout2.addStretch()
      layout2.addWidget(self.btn3)


      self.btn4 = QPushButton("StaticContrasting")
      self.btn4.clicked.connect(lambda:self.StaticContrasting('ENHANCEMENT/ContrastEnhacement.py',self.fname))
      self.btn4.setStyleSheet("background-color: lightgreen")
      layout2.addStretch()
      layout2.addWidget(self.btn4)

      self.btn5 = QPushButton("")
      self.btn5.clicked.connect(lambda:self.ImageSpecification('ENHANCEMENT/ImageSpecification.py',self.fname))
      self.btn5.setStyleSheet("background-color: lightgreen")
      #layout2.addStretch()
      
      #layout2.addWidget(self.btn5)

      #self.setLayout(layout2) 

      
      layout1.addLayout(layout2)

      layout3=QVBoxLayout()
      self.le3=QLabel("     Image   Restoration")
      self.le3.setStyleSheet("color: red;font-size:20px")
      layout3.addWidget(self.le3)
      self.le4=QLabel("             Select Algorithm")
      layout3.addStretch()
      layout3.addWidget(self.le4)

      self.btn6 = QPushButton("AnistropicDiffFilter")
      self.btn6.clicked.connect(lambda:self.AnistropicDiffFilter('RESTORATION/AnisotropicDiffFilter.py',self.fname))
      self.btn6.setStyleSheet("background-color: lightgreen")
      layout3.addStretch()
      layout3.addWidget(self.btn6)

      self.btn7 = QPushButton("ContraHarmonicMeanFilter")
      self.btn7.clicked.connect(lambda:self.ContraHarmonicFilter('RESTORATION/ContraHarmonicMeanFilter.py',self.fname))
      self.btn7.setStyleSheet("background-color: lightgreen")
      layout3.addStretch()
      layout3.addWidget(self.btn7)

      self.btn8 = QPushButton("MedianFilter")
      self.btn8.clicked.connect(lambda:self.MedianFilter('RESTORATION/MedianFilter.py',self.fname))
      self.btn8.setStyleSheet("background-color: lightgreen")
      layout3.addStretch()
      layout3.addWidget(self.btn8)


      self.btn9 = QPushButton("TotalVariationFilter")
      self.btn9.clicked.connect(lambda:self.TotalVariationFilter('RESTORATION/TotalVariationFilter.py',self.fname))
      self.btn9.setStyleSheet("background-color: lightgreen")
      layout3.addStretch()
      layout3.addWidget(self.btn9)

      self.btn10 = QPushButton("WinerFilter")
      self.btn10.clicked.connect(lambda:self.WinerFilter('RESTORATION/WinerFilter.py',self.fname))
      self.btn10.setStyleSheet("background-color: lightgreen")
      layout3.addStretch()
      layout3.addWidget(self.btn10)

      #self.setLayout(layout3) 

      layout1.addStretch()
      layout1.addLayout(layout3)



      layout4=QVBoxLayout()
      self.le5=QLabel("  Image Inpainting")
      self.le5.setStyleSheet("color: red;font-size:20px")
      layout4.addWidget(self.le5)
      self.le6=QLabel("       Select Algorithm")
      #layout4.addStretch()
      layout4.addWidget(self.le6)

      self.btn11 = QPushButton("Inpainting")
      self.btn11.clicked.connect(lambda:self.Inpainting1('INPAINTIING/inPainting.py',self.fname))
      self.btn11.setStyleSheet("background-color: lightgreen")
      #layout4.addStretch()
      layout4.addWidget(self.btn11)

      self.btn12 = QPushButton("Inpainting2")
      self.btn12.clicked.connect(self.getfile)
      self.btn12.setStyleSheet("background-color: lightgreen")
      #layout4.addStretch()
      #layout4.addWidget(self.btn12)

      #self.setLayout(layout4)

      layout1.addStretch()
      layout1.addLayout(layout4)



      layout0.addStretch()
      layout0.addLayout(layout1)

      self.setLayout(layout0)

      self.setWindowTitle("Explo")
      self.setGeometry(0, 0, 800, 2000)



		
   def getfile(self):
      self.fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpeg *.gif *.jpg *.png *.JPG *JPEG)")
      print self.fname
      self.le.setPixmap(QPixmap(self.fname))
      return self.fname
    

   def ContrastEnhancement(self, path,fname):
      self.snr_input.setText(QString(""))
      self.snr_output.setText(QString(""))
      print self.fname
      subprocess.call(['python',path,self.fname])
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/contrasting.png"))

   def HistogramEquilisation(self, path,fname):
      self.snr_input.setText(QString(""))
      self.snr_output.setText(QString(""))
      print self.fname
      subprocess.call(['python',path,self.fname])
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/histogramEqui.png"))

   def Negative(self, path,fname):
      self.snr_input.setText(QString(""))
      self.snr_output.setText(QString(""))
      print self.fname
      subprocess.call(['python',path,self.fname])
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/negative.png"))

   def StaticContrasting(self, path,fname):
      self.snr_input.setText(QString(""))
      self.snr_output.setText(QString(""))
      print self.fname
      subprocess.call(['python',path,self.fname])
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/StaticContrasting.png"))
      

   def ImageSpecification(self, path,fname):
      self.snr_input.setText(QString(""))
      self.snr_output.setText(QString(""))
      print self.fname
      subprocess.call(['python',path,self.fname])
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/ImageSpecification.png"))

   def AnistropicDiffFilter(self, path,fname):
      print self.fname
      #print self.lle
      subprocess.call(['python',path,self.fname])
      f=open("./snr.txt","r")
      var1=f.readline()
      var2=f.readline()
      f.close()
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/AnistropicDiff.png"))
      self.snr_input.setText(QString(var1))
      self.snr_output.setText(QString(var2))
      print var1,var2
      print " ergre"
      #self.snr_input.setText(QString(""))
      #self.snr_output.setText(QString(""))

   def ContraHarmonicFilter(self, path,fname):
      print self.fname
      #print self.lle
      subprocess.call(['python',path,self.fname])
      f=open("./snr.txt","r")
      var1=f.readline()
      var2=f.readline()
      f.close()
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/ContraHarmonicFilter.png"))
      self.snr_input.setText(QString(var1))
      self.snr_output.setText(QString(var2))
      print var1,var2
      print " ergre"
      #self.snr_input.setText(QString(""))
      #self.snr_output.setText(QString(""))

   def MedianFilter(self, path,fname):
      print self.fname
      #print self.lle
      subprocess.call(['python',path,self.fname])
      f=open("./snr.txt","r")
      var1=f.readline()
      var2=f.readline()
      f.close()
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/MedianFilter.png"))
      self.snr_input.setText(QString(var1))
      self.snr_output.setText(QString(var2))
      print var1,var2
      print " ergre"
      #self.snr_input.setText(QString(""))
      #self.snr_output.setText(QString(""))


   def TotalVariationFilter(self, path,fname):
      print self.fname
      #print self.lle
      subprocess.call(['python',path,self.fname])
      f=open("./snr.txt","r")
      var1=f.readline()
      var2=f.readline()
      f.close()
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/TotalVariationFilter.png"))
      self.snr_input.setText(QString(var1))
      self.snr_output.setText(QString(var2))
      print var1,var2
      print " ergre"
      #self.snr_input.setText(QString(""))
      #self.snr_output.setText(QString(""))

   def WinerFilter(self, path,fname):
      print self.fname
      #print self.lle
      subprocess.call(['python',path,self.fname])
      f=open("./snr.txt","r")
      var1=f.readline()
      var2=f.readline()
      f.close()
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/WinerFilter.png"))
      self.snr_input.setText(QString(var1))
      self.snr_output.setText(QString(var2))
      print var1,var2
      print " ergre"
      #self.snr_input.setText(QString(""))
      #self.snr_output.setText(QString(""))

   
   def Inpainting1(self, path,fname):
      self.snr_input.setText(QString(""))
      self.snr_output.setText(QString(""))
      print self.fname
      subprocess.call(['python',path,self.fname])
      self.lle.setPixmap(QPixmap("/media/semicolon/SourceCodes/ExploProject/RESULT/Inpainting1.png"))


  
			
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
