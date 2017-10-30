# -*- coding:utf-8 -*-
from urllib import request, error
# http://pythonhosted.org/pyquery/api.html
from pyquery import PyQuery as pq
import re


class QiuShiBaiKe:
    def __init__(self):
        self.__index__ = 1
        self.__header__ = {
            'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'}
        self.__url__ = 'https://www.qiushibaike.com/text/page/'
        self.__main_url__ = 'https://www.qiushibaike.com'
        # 一个对象存储一页的段子
        self.__stories__ = []
        # enable = True
        self.__enable__ = False

    # 获取页面源码
    def getPage(self, index=None, contentUrl=None):
        try:
            response = None
            if index:
                req = request.Request(self.__url__ + str(index))
                req.add_header('User-Agent', self.__header__['User-Agent'])
                response = request.urlopen(req)
            elif contentUrl:
                req = request.Request(self.__main_url__ + contentUrl)
                req.add_header('User-Agent', self.__header__['User-Agent'])
                response = request.urlopen(req)
            return response.read().decode('utf-8')
        except error.URLError as e:
            print('getPage失败！')
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
            return None

    # 获取页面上段子的内容
    # 每个段子包含作者及内容
    def getPageStories(self, index):
        content = self.getPage(index=index)
        self.saveHtmlFile(content=content)
        doc = pq(content)
        article_list = doc('article')
        pageStories = []
        for article in article_list.items():
            username = article.children('header a.username').text()
            view_intact = article.children('a.text span').text()
            if len(view_intact) > 1:
                intact_href = article.children('a.text').attr('href')
                intact_story = self.getPage(contentUrl=intact_href)
                text = self.getIntactStory(intact_story)
                pageStories.append([username, text])
            else:
                text = article.children('a.text').text()
                pageStories.append([username, text])
        return pageStories

    # 获取原文内容
    def getIntactStory(self, content):
        self.saveHtmlFile(intactHtml=content)
        doc = pq(content)
        return doc('div.content-text').text()

    # 保存页面
    def saveHtmlFile(self, content=None, intactHtml=None):
        if content:
            with open('./糗事百科.html', 'w', encoding='utf-8') as f:
                f.write(content)
        elif intactHtml:
            with open('./糗事原文.html', 'w', encoding='utf-8') as f:
                f.write(intactHtml)

    def load(self):
        if self.__enable__:
            if len(self.__stories__) < 2:
                pageStories = self.getPageStories(self.__index__)
                if pageStories:
                    self.__stories__.append(pageStories)
                    self.__index__ += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            receive = input()
            self.load()
            if receive == 'Q' or receive == 'q':
                self.__enable__ == False
                return
            print('当前第:%s页\n发布人:%s\n内容:%s\n' % (page, story[0], story[1]))

    def start(self):
        self.__enable__ = True
        self.load()
        nowPage = 0
        while self.__enable__:
            if len(self.__stories__) > 0:
                pageStories = self.__stories__[0]
                nowPage += 1
                del self.__stories__[0]
                self.getOneStory(pageStories, nowPage)
        return                


if __name__ == '__main__':
    crawler = QiuShiBaiKe()
    crawler.start()
