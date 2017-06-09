
    #DOM vs SAX
    #操作xml有两种方法：DOM和SAX。DOM会把整个xml读入内存，解析为树，因此占用内存大，解析慢，优点是
    #可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件

    #正常情况下，有限考虑SAX，因为DOM是在太占内存

    #Python中使用SAX解析xml非常简洁，通常我们关心的事件是start_element, end_element 和 char_data，
    #准备好这三个函数，就可以解析xml了

    #<a href='/'>python</a>
    #1. start_element事件，在读取<a href='/'>时
    #2. char_data事件，在读取python时
    #3. end_element事件，在读取</a>时


from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
    <ol>
        <li><a href='/python'>Python</a></li>
        <li><a href='/ruby'>Ruby</a></li>
    </ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)