# https://openload.co/f/IrdPk03cIBU/Thor.Ragnarok.2017.1080p.LATiNO.mp4#
# https://openload.co/f/ZGccVHtWEr8/Blade.Runner.2049.2017.1080p.LATiNO.mp4#


import os

# # get current working directorie
# cwd = os.getcwd()
# print cwd


# for file in os.listdir(dir_path):
#     if file.endswith(".apk"):
#         print (os.path.join(dir_path, file))


def getcurrentdir():
    # get current working directorie
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # print dir_path

    for file in os.listdir(dir_path):
        if file.endswith(".mk"):
            dirfiles = (os.path.join(dir_path, file))

            return dirfiles


def main():

    content

    dirfile = getcurrentdir()
    f= open(dirfile,"r")
    if (f.mode == "r"):
        out =  f.read()
        print out
    else:
        print 'no its read'


if __name__ == "__main__":
    main()
