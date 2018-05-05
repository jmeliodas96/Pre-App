# https://openload.co/f/IrdPk03cIBU/Thor.Ragnarok.2017.1080p.LATiNO.mp4#
# https://openload.co/f/ZGccVHtWEr8/Blade.Runner.2049.2017.1080p.LATiNO.mp4#


import os
import re
import numpy

# get current working directorie
def getcwd():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

# get all files in subdirectories with extension .mk
def getallfiles(extension):
    dirpath = getcwd()
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dirpath) for f in filenames if os.path.splitext(f)[1] == extension]
    return result

# parse content in mk files
def get_content_mk(out):
    new_out = []
    for out in out.split('\n'):
        new_out.append(out)

    return new_out



def get_list_files():
    content     = []
    find = ['.mk','.apk']
    sizefind = len(find)
    j = 0
    for j in range(sizefind):
        extension   =   find[j]
        files       =   getallfiles(extension)
        sizefile    =   len(files)
        k = 0
        for k in range(sizefile):
            # print files[k]
            content.append(files[k])
    return content


def mk_list():

    content = get_list_files()

    mk      = []
    mk_re   = re.compile('.[a-z]+.[d]+.[m]+.-*')
    #
    # apk     = []
    # apk_re  = re.compile('.[a]+[p]+[k].*')


    sizecontent = len(content)
    d = 0

    # iter on mk and iter on apk
    for d in range(sizecontent):
        # apk_search = apk_re.search(content[d])
        mk_search = mk_re.search(content[d])

        # if apk_search:
        #     apk.append(content[d])

        if mk_search:
            mk.append(content[d])

    return mk
    # return apk

# read the files found in subdirectories
def read_files_mk(dirfile,sizefile):
    i = 0
    for i in range(sizefile):
        f= open(dirfile[i],"r")
        if (f.mode == "r"):
            out =  f.read()
            new_out_mk  =   get_content_mk(out)

        else:
            print 'no its read'
    return new_out_mk


# read the files found in subdirectories
def read_files_mk_v1(dirfile):

    f= open(dirfile,"r")
    if (f.mode == "r"):
        out =  f.read()
        new_out_mk  =   get_content_mk(out)

    else:
        print 'no its read'
    return new_out_mk


def main():
    # get list
    mkfiles = mk_list()
    sizemkfiles = len(mkfiles)

    # print mkfiles

    # # just get files mk
    # mk_content  = read_files_mk(mkfiles,sizemkfiles)
    # szmkcontent = len(mk_content)
    new_re  =   re.compile('.[AO]\S.+[UE]\W.+[:=]\W')
    # new_re  = re.compile(".[AO]\S.+[UE]\W.+[:=]\W+\b")
    new_one = []
    new_two = []
    g = 0

    # print mk_content

    # print sizemkfiles
    for g in range(sizemkfiles):
        print mkfiles[g]
        if(g == 0):
            first_mk = mkfiles[g]
        elif(g > 0):
            second_mk = mkfiles[g]

    # first android.mk
    content     = read_files_mk_v1(first_mk)
    size1       = len(content)
    content2    = read_files_mk_v1(second_mk)
    size2       = len(content2)
    print '\n'
    print content

    print '\n'
    print content2

    # test 1
    i = 0
    j = 0
    print '\n'
    for i in range(size1):
        print i,' : ',content[i]
        # new_mk = parse_mk(mk_content,i)
        new_search_mk = new_re.search(content[i])
        if new_search_mk:
            new_one.append(content[i])

    print '\n'
    # print content
    # print content2

    for j in range(size2):
        print j,' : ',content2[j]
        new_search_mk = new_re.search(content2[j])
        if new_search_mk:
            new_two.append(content2[j])

    # print new_mk
    this = 'DeviceInfo'
    print '\n'
    print new_one
    print new_two
    size3 = len(new_one)
    size4 = len(new_two)
    c = 0
    for c in range(size3):
        print new_one[c]
        if(new_one[c] == 'LOCAL_MODULE := facebook-puto'):
            print 'puto find'
            new_one[c] = this

    print new_one


if __name__ == "__main__":
    main()
