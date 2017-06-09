# Base64 ��һ����64���ַ�����ʾ������������ݵķ���
import base64

#һ���ܴ���ȥ��=��base64���뺯����
def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s += b"="
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')