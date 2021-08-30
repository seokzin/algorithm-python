from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            print(f'title : {attrs[0][-1]}\n', end='')

    
    def handle_endtag(self, tag):
        if tag == 'p':  # p가 닫히는 순간 한줄을 모두 출력할 것
            temp = ''.join(x for x in p_list)

            while temp != temp.replace('  ', ' '):  # 공백 1개만 남김
                temp = temp.replace('  ', ' ')

            print(temp)
            p_list.clear()  # 한줄 출력 후 리스트 청소


    def handle_data(self, data):
        p_list.append(data)  # p 안의 내용물만 리스트에 담는다


p_list = []  # p 한줄의 내용을 모두 담는곳
parser = MyHTMLParser()
parser.feed(input())