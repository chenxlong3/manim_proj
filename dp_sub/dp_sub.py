from numbers import Number
from manimlib import *
import numpy as np

class problemIntro(Scene):
    def construct(self):
        text = """
        Given two strings text1 and text2, return the length of their 

        longest common subsequence. 


        If there is no common subsequence, return 0.
        """
        problem = Text(text, font="Comic Sans MS", font_size=40).shift(UP*2)
        self.play(Write(problem))
        self.wait()
        self.play(FadeOut(problem))

class test(Scene):
    def construct(self):
        obj_list = VGroup()
        for i in range(0, 3):
            for j in range(0, 5):
                tmp_num = Integer(0)
                tmp_num.shift(RIGHT*(j-2)*0.75 + DOWN*(i-1)*0.75 + UP)
                obj_list.add(tmp_num)
        self.play(Write(obj_list))
        self.wait()

class showStr(Scene):
    def construct(self):
        str1 = Text("a  b  c  d  e", font_size=70)
        str1_colored = Text("a  b  c  d  e", font_size=70,
            t2c={"a": BLUE, "c":BLUE, "e": BLUE}
        )
        str2 = Text("a\nc\ne", font_size=70)
        a = Text("a", font_size=70)
        # str1.arrange(buff = )
        str1.shift(2*UP)
        str2.shift(2.5*LEFT + 0.5*UP)
        str1_colored.shift(2*UP)

        self.play(Write(str1))
        # self.play(Transform(str1, str1_colored))
        self.play(str1[0].animate.set_color(BLUE), str1[6].animate.set_color(BLUE), str1[12].animate.set_color(BLUE))

        kw = {"run_time": 3, "path_arc": PI/2}
        self.play(TransformMatchingShapes(str1.copy(), str2), run_time=2)
        dp_mat = self.showMatrix()
        a.move_to([dp_mat[0][0].get_x()-1, dp_mat[0][0].get_y(), 0])
        self.play(FadeOut(str2), FadeIn(a))
        self.wait()

    def showMatrix(self):
        obj_list = VGroup()
        for i in range(0, 3):
            for j in range(0, 5):
                tmp_num = Integer(0)
                tmp_num.shift(RIGHT*(j-2)*0.75 + DOWN*(i-1)*0.7 + 0.5*UP)
                obj_list.add(tmp_num)
        self.play(Write(obj_list))
        self.wait()
        return obj_list