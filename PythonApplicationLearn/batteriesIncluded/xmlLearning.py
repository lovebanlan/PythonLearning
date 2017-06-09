
    #DOM vs SAX
    #����xml�����ַ�����DOM��SAX��DOM�������xml�����ڴ棬����Ϊ�������ռ���ڴ�󣬽��������ŵ���
    #��������������Ľڵ㡣SAX����ģʽ���߶��߽�����ռ���ڴ�С�������죬ȱ����������Ҫ�Լ������¼�

    #��������£����޿���SAX����ΪDOM����̫ռ�ڴ�

    #Python��ʹ��SAX����xml�ǳ���࣬ͨ�����ǹ��ĵ��¼���start_element, end_element �� char_data��
    #׼�����������������Ϳ��Խ���xml��

    #<a href='/'>python</a>
    #1. start_element�¼����ڶ�ȡ<a href='/'>ʱ
    #2. char_data�¼����ڶ�ȡpythonʱ
    #3. end_element�¼����ڶ�ȡ</a>ʱ


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