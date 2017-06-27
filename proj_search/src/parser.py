# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

class Parser(HTMLParser):
    def init_parser(self):
        self.data_list = []

    def handle_data(self, data):
        self.data_list.append(data)

    def data_check(self):
        media_list = ["media", "video", "picture", "mp4", "wmv", "wav", "image", "img", "jpg", "png", "gif", "ogg", "bmp", "tiff"]
        check_tag = "div"
        if check_tag.value in media_list:
            self.data_list.append("-1")