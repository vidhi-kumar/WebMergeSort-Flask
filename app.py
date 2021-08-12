from flask import Flask
from flask import render_template, request
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[l + i]
    for i in range(0, n2):
        R[i] = arr[m + i + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            arr[k] = R[j]
            j += 1
        else:
            arr[k] = L[i]
            i += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr):
    steps = ["-"]
    width = 1   
    n = len(arr)                                         
    while (width < n):
        l=0;
        while (l < n):
            r = min(l+(width*2-1), n-1)
            m = (l+r)//2
            if (width>n//2):       
                m = r-(n%width)  
            step = ""
            # dev part starts
            for itr in range(n):
                if itr == l:
                    if itr == n-1 and n%2 != 0:
                        step += str(arr[itr])
                    else:
                        step += "{" + str(arr[itr]) + " "
                elif itr == r:
                    step += str(arr[itr]) + "} "
                else:
                    step += str(arr[itr]) + " "
            if '(' in step or '{' in step:
                if steps[-1] == "-":
                    step += " _ _ _ _ max block size :" + str(width)
                steps.append(step)
            # dev part ends
            step = ""  
            merge(arr, l, m, r)
            # dev part starts
            for itr in range(n):
                if itr == l:
                    if itr == n-1 and n%2 != 0:
                        step += str(arr[itr])
                    else:
                        step += "(" + str(arr[itr]) + " "
                elif itr == r:
                    step += str(arr[itr]) + ") "
                else:
                    step += str(arr[itr]) + " "
            if (steps[-1] != step) and ('(' in step or '{' in step):
                steps.append(step)
            # dev part ends
            l += width*2
        steps += "-"
        width *= 2
    steps.pop(-1) # remove last hyphen
    return steps
   


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        input_string = request.form['array']
        try:
            int_array = [int(x) for x in input_string.split()]
            if len(int_array) == 1:
                ans_array = ["{1}", "(1)"]
            else:
                ans_array = mergeSort(int_array)
        except:
            ans_array = None
    else:
        ans_array=None
    return render_template('home.html', ans_array=ans_array)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    # app.run(debug=True) no debug mode in production
    app.run()