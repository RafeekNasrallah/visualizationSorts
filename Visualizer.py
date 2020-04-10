import time
import tkinter as tk
from copy import deepcopy

ids = []
arr = [7,8,2,6,13,17,16,8,4,12,1,11]

################################################# MERGE SORT #################################################
def mergesort(a, begin, end, numbers,seconds):
    txt1 = canvas.create_text(60,80,fill="red",font="Times 13 italic bold",
                        text="splits are in Red")
    txt2 = canvas.create_text(155,95,fill="blue",font="Times 13 italic bold",
                        text="numbers in progres are in Blue and Green")
    txt3 = canvas.create_text(92,110,fill="black",font="Times 13 italic bold",
                        text="sorted parts are in Black")
    mid = int(begin + ((end - begin) / 2))
    for i in range(begin, mid + 1): # for every split i show it in red color
        canvas.itemconfig(numbers[i], fill="red")
    for i in range(mid + 1, len(a)): # and update all other charts with grey
        canvas.itemconfig(numbers[i], fill="grey")
    master.update()
    time.sleep(seconds)
    if not (begin == mid == end):
        mergesort(a, begin, mid, numbers,seconds)
        mergesort(a, mid + 1, end, numbers,seconds)
        sort(a, begin, end, mid + 1, numbers,seconds)
    removeobject(txt3,txt1,txt2) # removes all the text labels


def sort(a, begin, end, mid, numbers,seconds):
    for i in range(begin, mid): # charts that are in action are printed in blue
        canvas.itemconfig(numbers[i], fill="blue")
    for i in range(mid, end + 1): # charts that are in action are printed in blue
        canvas.itemconfig(numbers[i], fill="green")
    master.update()
    time.sleep(seconds)
    fst = []
    snd = []
    updatedcoordfst = [] # those lists are used to track the charts that were moved up
    updatedcoordsnd = []
    updatedsnd = 0 # counter for each one
    updatedfst = 0
    originals = [] # used to save the original coords before moving them up
    oric = 0
    for i in range(begin, mid): #adding the numbers in two different arrays so i can sort them in the main array after
        fst.append(a[i])
        originals.append(canvas.coords(numbers[i])) # saving the coords before moving them ups so we dont get lost
        for j in range(7):
            canvas.move(numbers[i],0,-10)
            master.update()
            time.sleep(0.0005)
        updatedcoordfst.append(numbers[i]) # saving the coords after moving them up so we dont get lost
    for i in range(mid, end + 1):
        snd.append(a[i])
        originals.append(canvas.coords(numbers[i]))
        for j in range(7):
            canvas.move(numbers[i],0,-10)
            master.update()
            time.sleep(0.0005)
        updatedcoordsnd.append(numbers[i])
    pos = begin
    countera = 0
    counterb = 0
    while countera != len(fst) and counterb != len(snd):
        if fst[countera] > snd[counterb]:
            (tempx1,tempy1,tempx2,tempy2) = originals[oric]
            oric+=1
            (at,b,c,d) = canvas.coords(updatedcoordsnd[updatedsnd])
            (hor,ver) = calslope(c,d,tempx2,tempy2) # finding the slope of the small number, and the first original spot
            while d < 600: # till they reach the ground
                canvas.move(updatedcoordsnd[updatedsnd],-hor,-ver) # moving them towards the original slot
                master.update()
                time.sleep(0.0005)
                (at,b,c,d) = canvas.coords(updatedcoordsnd[updatedsnd])
            numbers[pos] = updatedcoordsnd[updatedsnd] # then updating tbe numbers list with the new slots
            updatedsnd+=1
            a[pos] = snd[counterb]
            pos += 1
            counterb += 1
        else: # same goes everywhere
            if fst[countera] <= snd[counterb]:
                (tempx1,tempy1,tempx2,tempy2) = originals[oric]
                oric+=1
                (at,b,c,d) = canvas.coords(updatedcoordfst[updatedfst])
                (hor,ver) = calslope(c,d,tempx2,tempy2)
                while d < 600:
                    canvas.move(updatedcoordfst[updatedfst],hor,ver)
                    master.update()
                    time.sleep(0.0005)
                    (at,b,c,d) = canvas.coords(updatedcoordfst[updatedfst])
                numbers[pos] = updatedcoordfst[updatedfst]
                updatedfst = updatedfst + 1
                a[pos] = fst[countera]
                pos += 1
                countera += 1
    while countera != len(fst): #copying all other elements when one array is done
        (tempx1, tempy1, tempx2, tempy2) = originals[oric]
        oric += 1
        (at, b, c, d) = canvas.coords(updatedcoordfst[updatedfst])
        (hor, ver) = calslope(c, d,tempx2, tempy2)
        while d < 600:
            canvas.move(updatedcoordfst[updatedfst], hor, ver)
            master.update()
            time.sleep(0.0005)
            (at, b, c, d) = canvas.coords(updatedcoordfst[updatedfst])
        numbers[pos] = updatedcoordfst[updatedfst]
        updatedfst += 1
        a[pos] = fst[countera]
        pos += 1
        countera += 1
    while counterb != len(snd):
        (tempx1, tempy1, tempx2, tempy2) = originals[oric]
        oric += 1
        (at, b, c, d) = canvas.coords(updatedcoordsnd[updatedsnd])
        (hor, ver) = calslope(c, d,tempx2, tempy2)
        while d < 600:
            canvas.move(updatedcoordsnd[updatedsnd], -hor, ver)
            master.update()
            time.sleep(0.0005)
            (at, b, c, d) = canvas.coords(updatedcoordsnd[updatedsnd])
        numbers[pos] = updatedcoordsnd[updatedsnd]
        updatedsnd += 1
        a[pos] = snd[counterb]
        pos += 1
        counterb += 1
    for i in range(begin, end + 1): #changing color of the sorted chart to black
        canvas.itemconfig(numbers[i], fill="black")
    master.update()
    time.sleep(seconds)

def calslope(x2f,y2f,x2s,y2s):
    #(x1f,y1f,x2f,y2f) = canvas.coords(chart1)
    if x2s-x2f == 0:
        return (0,10)
    else:
        slope = (y2s-y2f) / (x2s-x2f)
        return (1,slope)



def getcoords(elem, leng, pos): #takes the element,how long an array is and where this element is, and returns the coords of the chart
    return 30 + (int(500 / leng)) * pos, 600 - (elem * 20), 30 + (int(500 / leng)) * pos, 600

def draw_boardmerge(start, end, numbers): #draws the charts depending on the array
    global arr
    a =deepcopy(arr)
    global ids
    for i in ids:
        canvas.delete(i)
    canvas.update()
    numbers.clear()
    seconds = entry1.get() # gets the text box input as seconds
    if len(entry1.get()) == 0: # if nothing is entered, the default is 0.2 seconds
        seconds=0.2
    seconds = float(seconds)
    numbers = []
    for count, ele in enumerate(a):# adding all charts
        numbers.append(canvas.create_line(getcoords(ele, (len(a)), count), width=500 / len(a) - 10))
    master.update()
    time.sleep(seconds)
    mergesort(a, start, end, numbers,seconds)
    ids=deepcopy(numbers)


################################################### QUICK SORT ###############################################

def quicksort(a,begin,end,numbers,seconds):
    if begin > end:
        return
    (x1end,y1end,x2end,y2end) = canvas.coords(numbers[end]) # drawing all the arrows in their initial places
    piv = canvas.create_line(x1end,y1end-50,x2end,y1end-10, arrow=tk.LAST,fill="red")
    canvas.update()
    time.sleep(seconds)
    pivot = a[end]
    i = begin -1
    j = begin
    (x1j,y1j,x2j,y2j) = canvas.coords(numbers[j])
    jc = canvas.create_line(x1j,y1j-50,x2j,y1j-10, arrow=tk.LAST,fill="black") #  arrow where j should be
    if begin - 1 != -1: # arrow where i should be
        (x1i,y1i,x2i,y2i) = canvas.coords(numbers[i])
        ic = canvas.create_line(x1i,y1i-50,x2i,y1i-10, arrow=tk.LAST,fill="blue")
        updatecoords(ic,numbers[i])
    else: # when its -1
         ic = canvas.create_line(5,550,5,600, arrow=tk.LAST,fill="blue")
    samecoords(piv,jc,ic)
    time.sleep(seconds)
    while j != end:
        if a[j] > pivot:
            j+=1
            updatecoords(jc,numbers[j]) # coords are updated everytime the high of the char changes, so the arrow stays aboke the char
            samecoords(piv,jc,ic) # when all arrows go in the same coords, i just place them one above the other
            time.sleep(seconds)
        else: # here i swap i+1 with j
            i+=1
            (w,h,wb,hb) = canvas.coords(numbers[i])
            (aa,b,c,d) = canvas.coords(numbers[j])
            updatecoords(ic,numbers[i])
            samecoords(piv,jc,ic)
            txt1 = canvas.create_text(85,150,fill="blue",font="Times 12 italic bold",text="BLUE ")
            txt2 = canvas.create_text(190,150,fill="black",font="Times 12 italic bold",text="BLACK.")
            master.update()
            time.sleep(seconds)
            removeobject(txt1,txt2) #remove the txts after swaping
            time.sleep(seconds)
            canvas.coords(numbers[j],aa,h,c,hb) #the swaping.. changing coords
            canvas.coords(numbers[i],w,b,wb,d)
            updatecoords(jc,numbers[j]) # updating the arrows coords so they are above the NEW chart
            updatecoords(ic,numbers[i])
            samecoords(piv,jc,ic) # checking of arrows coords are the same
            time.sleep(seconds)
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            j+=1
            updatecoords(jc,numbers[j])
            samecoords(piv,jc,ic)
            time.sleep(seconds)
    i+=1
    updatecoords(ic,numbers[i])
    samecoords(piv,jc,ic)
    txt1 = canvas.create_text(85,150,fill="blue",font="Times 12 italic bold",text="BLUE ")
    txt2 = canvas.create_text(190,150,fill="red",font="Times 12 italic bold",text="RED.")
    master.update()
    time.sleep(seconds)
    removeobject(txt2,txt1)
    time.sleep(seconds)
    (w,h,wb,hb) = canvas.coords(numbers[i])
    (aa,b,c,d) = canvas.coords(numbers[end])
    canvas.coords(numbers[end],aa,h,c,hb)
    canvas.coords(numbers[i],w,b,wb,d)
    updatecoords(piv,numbers[end])
    updatecoords(ic,numbers[i])
    updatecoords(jc,numbers[j])
    samecoords(piv,ic,jc)
    time.sleep(seconds)
    temp = pivot
    a[end] = a[i]
    a[i] = temp
    removeobject(piv,ic,jc)
    quicksort(a,begin,i-1,numbers,seconds)
    quicksort(a,i+1,end,numbers,seconds)


def samecoords(piv,j,i): # this method takes the ids of 3 line objects and place them in a way that they dont cancel each other (one on the other)
    if canvas.coords(piv) == canvas.coords(j):
        if canvas.coords(piv) == canvas.coords(i):
            (w,h,wb,hb) = canvas.coords(j)
            canvas.coords(i,w,h-50,wb,h-10)
            canvas.coords(j,w, h-100,wb,h-60)
        else:
            (w,h,wb,hb) = canvas.coords(j)
            canvas.coords(j,w, h-50,wb,h-10)
    else:
        if canvas.coords(i) == canvas.coords(j):
            (w,h,wb,hb) = canvas.coords(i)
            canvas.coords(i,w, h-50,wb,h-10)
        else:
            if canvas.coords(piv) == canvas.coords(i):
                (w,h,wb,hb) = canvas.coords(j)
                canvas.coords(i,w,h-50,wb,h-10)
                if canvas.coords(i) == canvas.coords(j):
                    canvas.coords(i,w, h-100,wb,h-60)
    canvas.update()

def updatecoords(arrow,id): # takes the arrow and the chart, replace the arrow above the chart correctly
    (v,b,n,m) = canvas.coords(id)
    canvas.coords(arrow,v,b-50,n,b-10)
    canvas.update()

def draw_boardquick(start, end, numbers): #used to draw the charts
    global arr
    a =deepcopy(arr)
    global ids
    for i in ids: # deletings all old charts
        canvas.delete(i)
    canvas.update()
    numbers.clear()
    seconds = entry1.get() #saves the number and uses it for sleep variable
    if len(entry1.get()) == 0:
        seconds=0.2
    seconds = float(seconds)
    txt1 = canvas.create_text(35,150,fill="grey",font="Times 12 italic bold",text="SWAP ")
    txt2 = canvas.create_text(135,150,fill="grey",font="Times 12 italic bold",text="WITH ")
    txt3 = canvas.create_text(120,100,fill="black",font="Times 10 italic bold",text="Red arrow is pivot element \n black and blue arrows are the counters")
    canvas.update()
    for count, ele in enumerate(a): # drawing the charts
        (aa,b,c,d) = getcoords(ele, (len(a)), count)
        numbers.append(canvas.create_line(aa+10,b,c+10,d, width=350 / len(a) - 10))
    master.update()
    time.sleep(seconds)
    quicksort(a, start, end, numbers,seconds)
    removeobject(txt2,txt1,txt3) #removing all text objects
    ids = deepcopy(numbers)


def removeobject(*args): # it gets some objects and deleted them from the canvas
    for i in args:
        canvas.delete(i)
    canvas.update()


##################################################### INSERTION SORT ###################################################
def insertionsort(arr,border,numbers,seconds):
    if border==len(arr):
        return
    counter = border
    for i in range(0,border): # coloring the initial charts, blue is the sorted array
        canvas.itemconfig(numbers[i], fill="blue")
    time.sleep(seconds)
    for j in range(border+1,len(arr)):
        canvas.itemconfig(numbers[j], fill="grey") # grey are the charts that havent been sorted yet
    canvas.itemconfig(numbers[counter],fill="red") #red is the new element ( which we will compare with the sorted array
    time.sleep(seconds)
    canvas.update()
    for i in range(border-1,-1,-1):
        (x1i,y1i,x2i,y2i) = canvas.coords(numbers[i])
        (savedc1i,savedy1i,savedx2i,savedy2i) = canvas.coords(numbers[i])
        for j in range(7): #moving chart from the sorted array up
            canvas.move(numbers[i],0,-10)
            canvas.update()
            time.sleep(0.05)
            (x1i,y1i,x2i,y2i) = canvas.coords(numbers[i])
        (x1c,y1c,x2c,y2c) = canvas.coords(numbers[counter])
        (savedx1c,savedy1c,savedx2c,savedy2c) = canvas.coords(numbers[counter])
        for j in range(7): #moving the chart of the new element up
            canvas.move(numbers[counter],0,-10)
            canvas.update()
            time.sleep(0.05)
            (x1c,y1c,x2c,y2c) = canvas.coords(numbers[counter])
        if arr[counter] < arr[i]:
            mel = (savedy2c-y2i) / (savedx2c-x2i) #calculate the slope, so it can move exactly down
            (updatedx1,updatedy1,updatedx2,updatedy2) = canvas.coords(numbers[i])
            while updatedy2<600: # only if the new one is smaller that the sorted one we swap them
                canvas.move(numbers[i],1,mel)
                canvas.update()
                time.sleep(0.005)
                (updatedx1,updatedy1,updatedx2,updatedy2) = canvas.coords(numbers[i])
            mel = (savedy2i-y2c) / (savedx2i-x2c) #calculating the other slope
            (updatedx1,updatedy1,updatedx2,updatedy2) = canvas.coords(numbers[counter])
            while updatedy2<600:
                canvas.move(numbers[counter],-1,-mel)
                canvas.update()
                time.sleep(0.005)
                (updatedx1,updatedy1,updatedx2,updatedy2) = canvas.coords(numbers[counter])
            temp = arr[i]
            arr[i] = arr[counter]
            arr[counter] = temp
            tempco = numbers[i]
            numbers[i] = numbers[counter]
            numbers[counter] = tempco
        else: # if the border element (new element) is bigger we just take them down and break the loop
            (updatedx1,updatedy1,updatedx2,updatedy2) = canvas.coords(numbers[i])
            while updatedy2 < 600:
                canvas.move(numbers[i],0,10)
                (updatedx1,updatedy1,updatedx2,updatedy2) = canvas.coords(numbers[i])
                canvas.update()
                time.sleep(0.1)
            (updatedx1,updatedy1,updatedx2,updatedy2) = canvas.coords(numbers[counter])
            while updatedy2<600:
                canvas.move(numbers[counter],0,10)
                (updatedx1,updatedy1,updatedx2,updatedy2) = canvas.coords(numbers[counter])
                canvas.update()
                time.sleep(0.1)
            break
        counter-=1
    insertionsort(arr,border+1,numbers,seconds)


def draw_boardinsertion(numbers): #used to draw the charts
    global arr
    a =deepcopy(arr)
    global ids
    for i in ids: # deletings all old charts
        canvas.delete(i)
    canvas.update()
    numbers.clear()
    seconds = entry1.get() #saves the number and uses it for sleep variable
    if len(entry1.get()) == 0:
        seconds=0.2
    seconds = float(seconds)
    for count, ele in enumerate(a): # drawing the charts
        (aa,b,c,d) = getcoords(ele, (len(a)), count)
        numbers.append(canvas.create_line(aa+10,b,c+10,d, width=350 / len(a) - 10))
    master.update()
    time.sleep(seconds)
    insertionsort(a,1,numbers,seconds)
    ids = deepcopy(numbers)



#############################################BUBBLE SORT #################################################
def bubblesort(arr,border,numbers,seconds):
    original = []
    for i in numbers:
        original.append(canvas.coords(i))
    if border == -1:
        return
    if border<=(len(arr)-1):
        for i in range(border,(len(arr))):
            canvas.itemconfig(numbers[i],fill="black")
    for i in range(0,border):
        canvas.itemconfig(numbers[i],fill="grey")
    for i in range(0,border-1):
        for j in range(7):
            canvas.move(numbers[i],0,-10)
            canvas.move(numbers[i+1],0,-10)
            master.update()
            time.sleep(0.05)
        if arr[i] > arr[i+1]:
            (fx1,fy12,fx2,fy2) = canvas.coords(numbers[i])
            (sx1,sy1,sx2,sy2) = original[i+1]
            (x,y) = calslope(sx2,sy2,fx2,fy2)
            while fy2<600:
                canvas.move(numbers[i],x,y)
                master.update()
                time.sleep(0.0005)
                (fx1,fy12,fx2,fy2) = canvas.coords(numbers[i])
            (fx1,fy12,fx2,fy2) = canvas.coords(numbers[i+1])
            (sx1,sy1,sx2,sy2) = original[i]
            (x,y) = calslope(fx2,fy2,sx2,sy2)
            while fy2<600:
                canvas.move(numbers[i+1],-x,-y)
                master.update()
                time.sleep(0.0005)
                (fx1,fy12,fx2,fy2) = canvas.coords(numbers[i+1])
            #swap(original,i,i+1)
            swap(numbers,i,i+1)
            swap(arr,i,i+1)
            """temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp"""
        else:
            for j in range(7):
                canvas.move(numbers[i],0,10)
                canvas.move(numbers[i+1],0,10)
                master.update()
                time.sleep(0.0005)
    bubblesort(arr,border-1,numbers,seconds)


def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return temp


def draw_boardbubble(numbers): #used to draw the charts
    global arr
    a =deepcopy(arr)
    global ids
    for i in ids: # deletings all old charts
        canvas.delete(i)
    canvas.update()
    numbers.clear()
    seconds = entry1.get() #saves the number and uses it for sleep variable
    if len(entry1.get()) == 0:
        seconds=0.2
    seconds = float(seconds)
    for count, ele in enumerate(a): # drawing the charts
        (aa,b,c,d) = getcoords(ele, (len(a)), count)
        numbers.append(canvas.create_line(aa+10,b,c+10,d, width=350 / len(a) - 10))
    master.update()
    time.sleep(seconds)
    bubblesort(a,len(a),numbers,seconds)
    ids = deepcopy(numbers)








master = tk.Tk()
canvas = tk.Canvas(master, width=500, height=600)
canvas.pack()
txt = canvas.create_text(77,20,fill="black",font="Times 10 italic bold",text="Enter how many seconds \n each step should take")
entry1 = tk.Entry (master)
canvas.create_window(73, 45, window=entry1)

while True:
    dup = deepcopy(arr)
    button = tk.Button(master,  text ="Merge Sort",width=15, height=2, command=lambda: draw_boardmerge(0, 11, ids)).place(x=370, y=0)
    button = tk.Button(master,  text ="Quick Sort",width=15, height=2, command=lambda: draw_boardquick(0, 11, ids)).place(x=250, y=0)
    button = tk.Button(master,  text ="Insertion Sort",width=15, height=2, command=lambda: draw_boardinsertion(ids)).place(x=250, y=40)
    button = tk.Button(master,  text ="Bubble Sort",width=15, height=2, command=lambda: draw_boardbubble(ids)).place(x=370, y=40)
    tk.mainloop()
