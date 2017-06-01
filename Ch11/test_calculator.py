import unittest             #內建模組，用來做單元測試
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):                #測試開始時的初始化設定
        self.calc = Calculator()

    def tearDown(self):             #測試結束後做還原資料的動作
        self.calc = None
        self.answer = None

    def test_plus(self):            #每個單元測試開頭都必須要以test名稱開頭
        self.answer = self.calc.plus(1, 2)
        self.assertEqual(self.answer, 3)

    def plus(self):                 #不是以test開頭的函式式不會執行的
        self.answer = self.calc.plus(1, 2)
        self.assertEqual(self.answer, 3)

    def test_minus(self):
        self.answer = self.calc.minus(3, 1)
        self.assertEqual(self.answer, 2)

    def test_multiply(self):
        self.answer = self.calc.multiply(2, 4)
        self.assertEqual(self.answer, 7)    #7與計算結果不相同，會噴出錯誤

    def test_divide(self):
        self.answer = self.calc.divide(4, 2)
        self.assertEqual(self.answer, 2)

if __name__ == '__main__':              #要呼叫unittest.main才會執行
    unittest.main()