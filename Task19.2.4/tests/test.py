import pytest

from app.calculator import Calculator

class TestCalc:
     def setup(self):
         self.calculator = Calculator

     def test_adding_success(self):
         assert self.calculator.adding(self, 1, 1) == 2

     def test_adding_unsuccess(self):
         assert self.calculator.adding(self, 1, 1) == 3

     def test_multiply_success(self):
         assert self.calculator.multiply(self, 2, 2) == 4

     def test_multiply_unsuccess(self):
          assert self.calculator.multiply(self, 2, 2) == 5

     def test_subtraction_success(self):
         assert self.calculator.subtraction(self, 6, 3) == 3

     def test_subtraction_unsuccess(self):
          assert self.calculator.subtraction(self, 6, 3) == 2

     def test_division_success(self):
         assert self.calculator.division(self, 6, 2) == 3

     def test_division_unsuccess(self):
          assert self.calculator.division(self, 6, 2) == 2

     def test_zero_division(self):
         with pytest.raises(ZeroDivisionError):
             self.calculator.division(self, 1, 0)

     def teardown(self):
         print('Выполнение метода Teardown')