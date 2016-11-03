#! /usr/bin/python
# coding:utf-8
import os
import sys

sys.path.append(os.path.abspath("../.."))
from modules import vulnerability
from modules.script_tools import *


class Vulnerability(vulnerability.VRL_Vulnerability):
    # 这里之上不要更改，除了增加import------------------------------------------------------------------------
    def __init__(self):
        '''Add information of your vulnerability here'''
        self.name = 'dop'
        # 这里的信息用于使用这一vulnerability显示给用户的信息。这里的名字可以写全称。格式请保持这种风格。尽量详尽。
        self.info = \
            '''Vulnerability Name : dop
            Vulnerability abstract : Data-Oriented Programming to construct expressive non-control
data exploits for arbitrary x86 programs. 
            Author : guoyingjie
            Environment : ASLR off; DEP on; PIE off; Architecture: amd64/i386.
            '''
        # 这里包括用户可以设置的所有选项和默认值。注意必须为字符串形式，取值时用eval函数。
        # 这里与exploit中相同key的值将被同步为exploit的值。
        self.options = {'port': '34567',
                        'static': 'False',
                        'aslr': 'off',
                        'architecture': 'amd64'}
        # 这里写出支持的exploit名称，以路径名为准。如有多个可以写为list。
        self.exploit = ['dop']

    def run(self):
        '''在这里运行你的程序，你可以单独运行这一脚本，会自动帮你运行。如果这里运行成功，那么VRL就可以调用你的脚本了。
        确保你运行的时候符合options中的设置。
        下面是一个简单的样例。'''
        aslr_off()
        if self.options['architecture'] == 'amd64':
            if self.options['static'] == 'False':
                file_name = 'dop'
            else:
                print 'static not find'
                return
        elif self.options['architecture'] == 'i386':
            print ' not find'
            return
        else:
            print 'Unrecognized architecture, stop.'
            return
        print 'Port: %s  listening > %s' % (self.options['port'], file_name)
        os.system(new_terminal('echo "Running..." && socat TCP4-LISTEN:' +
                               self.options['port'] + 'fork EXEC:./' + file_name))


# 这里之下不要更改---------------------------------------------------------------------------------
if __name__ == "__main__":
    if '__init__.py' not in os.listdir(os.curdir):
        os.mknod('__init__.py')
    vul = Vulnerability()
    print 'Vulnerability: ', vul.name, ' \n'
    print 'Checking:\n'
    if vul.frame_check():
        print 'Running:\n'
        vul.run()
