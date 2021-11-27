import PIL.Image
import io


def inject_png(injection_png,main):
    img = PIL.Image.open(injection_png)
    b_arr = io.BytesIO()
    img.save(b_arr, format='PNG')
    with open (main, 'ab') as f:
        f.write(b_arr.getvalue())

def inject_str(injection_str,main):
    injection_str = injection_str.encode('utf-8')
    with open(main,'ab') as f:
        f.write(injection_str)

def inject_exe(injecttion_exe,main):
    with open(main,'ab') as f, open(injecttion_exe,'rb') as f2:
        f.write(f2.read())
        print("успех!")