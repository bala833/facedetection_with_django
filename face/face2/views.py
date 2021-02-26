from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Videos,Face
from face2.forms import VideoForm,FaceForm
from rest_framework.response import Response

import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

# Create your views here.
import pytube

def face(request,template_name="new_face.html"):
    if request.method=='GET':
        count_all_face = Face.objects.all().count()
        print(count_all_face,"count_all_facecccccccccccccccccccc")
        try:
            face = Face.objects.all()
            print(face,'face')
            page = 'list'
        except Face.DoesNotExist:
            raise Http404("page is not exit")
    if request.method == 'POST':
        form= FaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,template_name,locals())
         
def add_face(request,template_name='add_face.html'):
    if request.method == 'POST':
        # request.POST.get('name')
        # print(request.user_id)
        form= FaceForm(request.POST)
        if form.is_valid():

            name =  request.POST.get('name')     
            Id = request.POST.get('user_id')  
            # Id='3'
            print(type(Id))
            # Id=(txt.get())
            # name='bala'
            if(is_number(Id) and name.isalpha()):
                cam = cv2.VideoCapture(0)
                harcascadePath = 'F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\haarcascade_frontalface_default.xml'
                #company
                # harcascadePath = "F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\haarcascade_frontalface_default.xml"
                # harcascadePath = "haarcascade_frontalface_default.xml"
                detector=cv2.CascadeClassifier(harcascadePath)
                sampleNum=0
                while(True):
                    _ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                        #incrementing sample number 
                        sampleNum=sampleNum+1
                        #saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\TrainingImage\\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                        # company 
                        # cv2.imwrite("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\TrainingImage\\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                        # cv2.imwrite("TrainingImage\\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                      
                        #display the frame
                        cv2.imshow('frame',img) 
                    #wait for 100 miliseconds 
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    # break if the sample number is morethan 60
                    elif sampleNum>60:
                        break
                cam.release()
                cv2.destroyAllWindows() 
                res = "Images Saved for ID : " + Id +" Name : "+ name
                row = [Id , name]
                with open('F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\StudentDetails.csv','w', newline='') as csvFile:
                # company
                # with open('F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\StudentDetails.csv','w', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                    print(writer)
                # csvFile.close()
            # return HttpResponse(res)
            form.save()
            return redirect('home')
    else:
        form =FaceForm()
    return render(request,template_name,locals())





def download(request):
    link = "https://www.youtube.com/watch?v=n06H7OcPd-g"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download()
    # print(downloaded)
    bala = 'bala'
    return bala


def load_page(request, template_name="landing_page.html"):

    try:
        name = Face.objects.all()
        count_all_face = Face.objects.all().count()
    except Face.DoesNotExist:
        raise Http404("page is not exit")

    return render(request,template_name,locals())

 
def upload_video(request):
     
    if request.method == 'POST': 
         
        title = request.POST['title']
        # video = request.POST['video']
        # print(title,"tttttt")
        # print(video)
        # print(request.POST)
        # print(request.FILES)
         
        form= VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        # content = Videos(title=title,video=video)
        # content.save()
            return redirect('videos')
    else:
        form = VideoForm()
        # context = {'form' : form}
     
    return render(request,'upload.html',locals())
 
 
def display(request):
     
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
     
    return render(request,'list.html',context)









window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
#window.geometry('1280x720')
window.configure(background='blue')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message2 = tk.Label(window, text="" ,fg="red"   ,bg="yellow",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=650, y=650)



def track_image1(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\datatrainningData.yml")
    harcascadePath = "F:\\22_02_2021\\facedetection_with_django\\face\\face2\\haarcascade_frontalface_default.xml"
    # harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)  
    # df=pd.read_csv("StudentDetails\\StudentDetails.csv")
    df=pd.read_csv("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        _ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])  
            print(Id, conf,"0000000000000000000000")                                 
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                print(aa,"rrrrrrrrrrrrrrrrrrrrrrr")
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\ImagesUnknown"))+1
                cv2.imwrite("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\ImagesUnknown/Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="F:\\22_02_2021\\facedetection_with_django\\face\\face2\\Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res=attendance
    message2.configure(text= res)










def track_image(request):
    # recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    recognizer.read("F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\trainningData.yml")
    # company
    # recognizer.read("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\trainningData.yml")

    harcascadePath = "F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\haarcascade_frontalface_default.xml"
    # company
    # harcascadePath = "F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\haarcascade_frontalface_default.xml"
    # harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)  
    # df=pd.read_csv("StudentDetails\\StudentDetails.csv")
    df=pd.read_csv("F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\StudentDetails.csv")
    # company
    # df=pd.read_csv("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\StudentDetails.csv")
    print(df,"name of user ")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        _ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])    
            print(Id, conf, ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")                               
            if(conf < 50):
                ts = time.time()        
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                print(aa,"eeeeeeeeeeeeeeeeeee")
                tt=str(Id)+"-"+aa
                # cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\ImagesUnknown"))+1
                # company
                # noOfFile=len(os.listdir("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\ImagesUnknown"))+1
                
                cv2.imwrite("F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\ImagesUnknown/Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                # company
                # cv2.imwrite("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\ImagesUnknown/Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\Attendance\\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    
    # company
    # fileName="F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\Attendance\\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res=attendance
    # return res
    # message2.configure(text= res)
    return HttpResponse(res)









message = tk.Label(window, text="Face-Recognition-Based-Attendance-Management-System" ,bg="Green"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'italic bold ')) 

message.place(x=110, y=20)
message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=600, y=400)

def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)   


txt = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=600, y=215)

txt2 = tk.Entry(window,width=20  ,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=600, y=315)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


def TakeImages(request):  
    name = request.GET.get('name', None)      
    Id = request.GET.get('user_id', None)    
    print(name, Id, "pppppppppppppppppppppppppppppppppp")  
    # Id='3'
    print(type(Id))
    # Id=(txt.get())
    # name='bala'
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = 'F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\haarcascade_frontalface_default.xml'
        #company
        # harcascadePath = "F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\haarcascade_frontalface_default.xml"
        # harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            _ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\TrainingImage\\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                # company 
                # cv2.imwrite("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\TrainingImage\\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                # cv2.imwrite("TrainingImage\\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
              
                #display the frame
                cv2.imshow('frame',img) 
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 60
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\StudentDetails.csv','w', newline='') as csvFile:
        # company
        # with open('F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\StudentDetails.csv','w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            print(writer)
        # csvFile.close()
    return HttpResponse(res)
        # message.configure(text= res)
    # else:
    #     if(is_number(Id)):
    #         res = "Enter Alphabetical Name"
    #         message.configure(text= res)
    #     if(name.isalpha()):
    #         res = "Enter Numeric Id"
    #         message.configure(text= res)
 

takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=100, y=500)















def TrainImages(request):
    print(cv2.__version__)
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    #recognizer = cv2.face.LBPHFaceRecognizer_create()
    # $cv2.createLBPHFaceRecognizer()
    harcascadePath = "F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\haarcascade_frontalface_default.xml"
    # company
    # harcascadePath = "F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\haarcascade_frontalface_default.xml"
    print(harcascadePath,"harcascadePath")
    # harcascadePath = "haarcascade_frontalface_default.xml"
    _detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\TrainingImage")
    # company
    # faces,Id = getImagesAndLabels("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\TrainingImage")
    # faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("F:\\MY WORK\\facedetection_with_django\\face\\face2\\data\\trainningData.yml")
    # company    
    # recognizer.save("F:\\22_02_2021\\facedetection_with_django\\face\\face2\\data\\trainningData.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
    # message.configure(text= res)
    return HttpResponse(res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids