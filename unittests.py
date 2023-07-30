from utils import *
from unittest import TestCase

"""
- For each operation, you should write tests to test  on matrices of different sizes.
- Keep in mind that the tests provided in the starter code are NOT comprehensive. That is, we strongly
advise you to modify them and add new tests.
- Hint: use dp_mc_matrix to generate dumbpy and numc matrices with the same data and use
      cmp_dp_nc_matrix to compare the results
"""
class TestAdd(TestCase):
    def test_small_add_2(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2, 2, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2, 2, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        try:
            nc.Matrix(3, 3) + nc.Matrix(2, 2)
            self.assertTrue(False)
        except ValueError as e:
            print(e)
            pass
        print("test_small_add_2")
        print_speedup(speed_up)

    def test_small_add_4(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4, 4, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4, 4, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_small_add_4")
        print_speedup(speed_up)


    def test_small_add_8(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8, 8, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8, 8, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_small_add_8")
        print_speedup(speed_up)

    def test_small_add_16(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16, 16, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16, 16, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_small_add_16")
        print_speedup(speed_up)

    def test_small_add_32(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32, 32, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32, 32, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_small_add_32")
        print_speedup(speed_up)

    def test_medium_add_64(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(64, 64, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(64, 64, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_medium_add_64")
        print_speedup(speed_up)

    def test_medium_add_128(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(128, 128, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(128, 128, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_medium_add_128")
        print_speedup(speed_up)

    def test_medium_add_256(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(256, 256, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(256, 256, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_medium_add_256")
        print_speedup(speed_up)


    def test_medium_add_512(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(512, 512, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(512, 512, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_medium_add_512")
        print_speedup(speed_up)

    def test_medium_add_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(1024, 1024, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(1024, 1024, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_medium_add_1024")
        print_speedup(speed_up)

    def test_large_add_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2048, 2048, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2048, 2048, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_large_add_2048")
        print_speedup(speed_up)

    def test_large_add_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4096, 4096, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4096, 4096, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_large_add_4096")
        print_speedup(speed_up)

    def test_large_add_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8192, 8192, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8192, 8192, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_large_add_8192")
        print_speedup(speed_up)

    def test_large_add_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16384, 16384, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16384, 16384, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_large_add_16384")
        print_speedup(speed_up)

    def test_large_add_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32768, 32768, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32768, 32768, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print("test_large_add_32768")
        print_speedup(speed_up)

# (OPTIONAL) Uncomment the following TestSub class if you have implemented matrix subtraction.
class TestSub(TestCase):
    def test_small_sub_2(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2, 2, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2, 2, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        try:
            nc.Matrix(3, 3) - nc.Matrix(2, 2)
            self.assertTrue(False)
        except ValueError as e:
            print(e)
            pass
        print("test_small_sub_2")
        print_speedup(speed_up)

    def test_small_sub_4(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4, 4, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4, 4, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_small_sub_4")
        print_speedup(speed_up)


    def test_small_sub_8(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8, 8, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8, 8, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_small_sub_8")
        print_speedup(speed_up)

    def test_small_sub_16(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16, 16, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16, 16, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_small_sub_16")
        print_speedup(speed_up)

    def test_small_sub_32(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32, 32, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32, 32, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_small_sub_32")
        print_speedup(speed_up)

    def test_medium_sub_64(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(64, 64, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(64, 64, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_medium_sub_64")
        print_speedup(speed_up)

    def test_medium_sub_128(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(128, 128, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(128, 128, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_medium_sub_128")
        print_speedup(speed_up)

    def test_medium_sub_256(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(256, 256, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(256, 256, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_medium_sub_256")
        print_speedup(speed_up)


    def test_medium_sub_512(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(512, 512, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(512, 512, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_medium_sub_512")
        print_speedup(speed_up)

    def test_medium_sub_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(1024, 1024, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(1024, 1024, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_medium_sub_1024")
        print_speedup(speed_up)

    def test_large_sub_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2048, 2048, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2048, 2048, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_large_sub_2048")
        print_speedup(speed_up)

    def test_large_sub_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4096, 4096, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4096, 4096, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_large_sub_4096")
        print_speedup(speed_up)

    def test_large_sub_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8192, 8192, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8192, 8192, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_large_sub_8192")
        print_speedup(speed_up)

    def test_large_sub_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16384, 16384, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16384, 16384, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_large_sub_16384")
        print_speedup(speed_up)

    def test_large_sub_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32768, 32768, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32768, 32768, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print("test_large_sub_32768")
        print_speedup(speed_up)

class TestAbs(TestCase):
    def test_small_abs_2(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_small_abs_2")
        print_speedup(speed_up)

    def test_small_abs_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4, 4, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_small_abs_4")
        print_speedup(speed_up)

    def test_small_abs_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8, 8, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_small_abs_8")
        print_speedup(speed_up)

    def test_small_abs_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16, 16, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_small_abs_16")
        print_speedup(speed_up)

    def test_small_abs_32(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32, 32, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_small_abs_32")
        print_speedup(speed_up)

    def test_medium_abs_64(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 64, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_medium_abs_64")
        print_speedup(speed_up)

    def test_medium_abs_128(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(128, 128, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_medium_abs_128")
        print_speedup(speed_up)
        
    def test_medium_abs_256(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(256, 256, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print_speedup(speed_up)
        
    def test_medium_abs_512(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(512, 512, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_medium_abs_512")
        print_speedup(speed_up)
        
    def test_medium_abs_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(1024, 1024, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_medium_abs_1024")
        print_speedup(speed_up)
        
    def test_large_abs_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 2048, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_large_abs_2048")
        print_speedup(speed_up)
        
    def test_large_abs_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4096, 4096, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_large_abs_4096")
        print_speedup(speed_up)
        
    def test_large_abs_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8192, 8192, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_large_abs_8192")
        print_speedup(speed_up)

    def test_large_abs_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16384, 16384, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_large_abs_16384")
        print_speedup(speed_up)
        
    def test_large_abs_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32768, 32768, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print("test_large_abs_32768")
        print_speedup(speed_up)


class TestTran(TestCase):
    def test_small_tran_2(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_small_tran_2")
        print_speedup(speed_up)

    def test_small_tran_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4, 4, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_small_tran_4")
        print_speedup(speed_up)

    def test_small_tran_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8, 8, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_small_tran_8")
        print_speedup(speed_up)

    def test_small_tran_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16, 16, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_small_tran_16")
        print_speedup(speed_up)

    def test_small_tran_32(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32, 32, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_small_tran_32")
        print_speedup(speed_up)

    def test_medium_tran_64(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 64, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_medium_tran_64")
        print_speedup(speed_up)

    def test_medium_tran_128(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(128, 128, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_medium_tran_128")
        print_speedup(speed_up)
        
    def test_medium_tran_256(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(256, 256, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print_speedup(speed_up)
        
    def test_medium_tran_512(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(512, 512, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_medium_tran_512")
        print_speedup(speed_up)
        
    def test_medium_tran_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(1024, 1024, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_medium_tran_1024")
        print_speedup(speed_up)
        
    def test_large_tran_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 2048, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_large_tran_2048")
        print_speedup(speed_up)
        
    def test_large_tran_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4096, 4096, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_large_tran_4096")
        print_speedup(speed_up)
        
    def test_large_tran_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8192, 8192, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_large_tran_8192")
        print_speedup(speed_up)

    def test_large_tran_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16384, 16384, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_large_tran_16384")
        print_speedup(speed_up)
        
    def test_large_tran_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32768, 32768, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "tran")
        self.assertTrue(is_correct)
        print("test_large_tran_32768")
        print_speedup(speed_up)

        
# (OPTIONAL) Uncomment the following TestNeg class if you have implemented matrix negation.
class TestNeg(TestCase):
    def test_small_neg_2(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_small_neg_2")
        print_speedup(speed_up)

    def test_small_neg_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4, 4, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_small_neg_4")
        print_speedup(speed_up)

    def test_small_neg_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8, 8, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_small_neg_8")
        print_speedup(speed_up)

    def test_small_neg_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16, 16, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_small_neg_16")
        print_speedup(speed_up)

    def test_small_neg_32(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32, 32, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_small_neg_32")
        print_speedup(speed_up)

    def test_medium_neg_64(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 64, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_medium_neg_64")
        print_speedup(speed_up)

    def test_medium_neg_128(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(128, 128, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_medium_neg_128")
        print_speedup(speed_up)
        
    def test_medium_neg_256(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(256, 256, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print_speedup(speed_up)
        
    def test_medium_neg_512(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(512, 512, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_medium_neg_512")
        print_speedup(speed_up)
        
    def test_medium_neg_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(1024, 1024, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_medium_neg_1024")
        print_speedup(speed_up)
        
    def test_large_neg_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 2048, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_large_neg_2048")
        print_speedup(speed_up)
        
    def test_large_neg_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4096, 4096, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_large_neg_4096")
        print_speedup(speed_up)
        
    def test_large_neg_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8192, 8192, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_large_neg_8192")
        print_speedup(speed_up)

    def test_large_neg_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16384, 16384, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_large_neg_16384")
        print_speedup(speed_up)
        
    def test_large_neg_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32768, 32768, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
        self.assertTrue(is_correct)
        print("test_large_neg_32768")
        print_speedup(speed_up)

class TestMul(TestCase):
    def test_small_mul_2(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2, 2, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2, 2, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        try:
            nc.Matrix(3, 3) * nc.Matrix(2, 2)
            self.assertTrue(False)
        except ValueError as e:
            print(e)
            pass
        print("test_small_mul_2")
        print_speedup(speed_up)

    def test_small_mul_4(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4, 4, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4, 4, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_small_mul_4")
        print_speedup(speed_up)


    def test_small_mul_8(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8, 8, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8, 8, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_small_mul_8")
        print_speedup(speed_up)

    def test_small_mul_16(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16, 16, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16, 16, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_small_mul_16")
        print_speedup(speed_up)

    def test_small_mul_32(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32, 32, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32, 32, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_small_mul_32")
        print_speedup(speed_up)

    def test_medium_mul_64(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(64, 64, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(64, 64, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_medium_mul_64")
        print_speedup(speed_up)

    def test_medium_mul_128(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(128, 128, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(128, 128, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_medium_mul_128")
        print_speedup(speed_up)

    def test_medium_mul_256(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(256, 256, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(256, 256, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_medium_mul_256")
        print_speedup(speed_up)


    def test_medium_mul_512(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(512, 512, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(512, 512, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_medium_mul_512")
        print_speedup(speed_up)

    def test_medium_mul_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(1024, 1024, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(1024, 1024, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_medium_mul_1024")
        print_speedup(speed_up)

    def test_large_mul_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2048, 2048, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2048, 2048, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_large_mul_2048")
        print_speedup(speed_up)

    def test_large_mul_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4096, 4096, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4096, 4096, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_large_mul_4096")
        print_speedup(speed_up)

    def test_large_mul_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8192, 8192, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8192, 8192, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_large_mul_8192")
        print_speedup(speed_up)

    def test_large_mul_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16384, 16384, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16384, 16384, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_large_mul_16384")
        print_speedup(speed_up)

    def test_large_mul_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32768, 32768, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32768, 32768, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print("test_large_mul_32768")
        print_speedup(speed_up)


class TestPow(TestCase):
    def test_small_pow_2_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_2_4")
        print_speedup(speed_up)

    def test_small_pow_2_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_2_8")
        print_speedup(speed_up)


    def test_small_pow_2_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_2_16")
        print_speedup(speed_up)

    def test_small_pow_4_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4, 4, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_4_4")
        print_speedup(speed_up)

    def test_small_pow_4_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4, 4, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_4_8")
        print_speedup(speed_up)


    def test_small_pow_4_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4, 4, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_4_16")
        print_speedup(speed_up)

    def test_small_pow_8_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8, 8, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_8_4")
        print_speedup(speed_up)

    def test_small_pow_8_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8, 8, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_8_8")
        print_speedup(speed_up)


    def test_small_pow_8_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(8, 8, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_8_16")
        print_speedup(speed_up)

    def test_small_pow_16_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16, 16, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_16_4")
        print_speedup(speed_up)

    def test_small_pow_16_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16, 16, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_16_8")
        print_speedup(speed_up)


    def test_small_pow_16_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(16, 16, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_16_16")
        print_speedup(speed_up)


    def test_small_pow_32_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32, 32, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_32_4")
        print_speedup(speed_up)

    def test_small_pow_32_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32, 32, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_32_8")
        print_speedup(speed_up)


    def test_small_pow_32_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(32, 32, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_small_pow_32_16")
        print_speedup(speed_up)

    def test_medium_pow_64_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 64, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_64_4")
        print_speedup(speed_up)

    def test_medium_pow_64_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 64, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_64_8")
        print_speedup(speed_up)


    def test_medium_pow_64_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 64, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_64_16")
        print_speedup(speed_up)

    def test_medium_pow_128_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(128, 128, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_128_4")
        print_speedup(speed_up)

    def test_medium_pow_128_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(128, 128, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_128_8")
        print_speedup(speed_up)


    def test_medium_pow_128_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(128, 128, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_128_16")
        print_speedup(speed_up)

    def test_medium_pow_256_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(256, 256, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_256_4")
        print_speedup(speed_up)

    def test_medium_pow_256_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(256, 256, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_256_8")
        print_speedup(speed_up)


    def test_medium_pow_256_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(256, 256, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_256_16")
        print_speedup(speed_up)

    def test_medium_pow_512_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(512, 512, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_512_4")
        print_speedup(speed_up)

    def test_medium_pow_512_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(512, 512, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_512_8")
        print_speedup(speed_up)


    def test_medium_pow_512_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(512, 512, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_512_16")
        print_speedup(speed_up)


    def test_medium_pow_1024_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(1024, 1024, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_1024_4")
        print_speedup(speed_up)

    def test_medium_pow_1024_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(1024, 1024, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_1024_8")
        print_speedup(speed_up)


    def test_medium_pow_1024_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(1024, 1024, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_medium_pow_1024_16")
        print_speedup(speed_up)


    def test_large_pow_2048_4(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 2048, seed=0)
        is_correct, speed_up = compute([dp_mat, 4], [nc_mat, 4], "pow")
        self.assertTrue(is_correct)
        print("test_large_pow_2048_4")
        print_speedup(speed_up)

    def test_large_pow_2048_8(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 2048, seed=0)
        is_correct, speed_up = compute([dp_mat, 8], [nc_mat, 8], "pow")
        self.assertTrue(is_correct)
        print("test_large_pow_2048_8")
        print_speedup(speed_up)


    def test_large_pow_2048_16(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 2048, seed=0)
        is_correct, speed_up = compute([dp_mat, 16], [nc_mat, 16], "pow")
        self.assertTrue(is_correct)
        print("test_large_pow_2048_16")
        print_speedup(speed_up)


class TestGet(TestCase):
    def test_get_small(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        self.assertEqual(round(dp_mat.get(rand_row, rand_col), decimal_places),
            round(nc_mat.get(rand_row, rand_col), decimal_places))

    def test_get_medium(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 128, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        self.assertEqual(round(dp_mat.get(rand_row, rand_col), decimal_places),
            round(nc_mat.get(rand_row, rand_col), decimal_places))

    def test_get_large(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 4096, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        self.assertEqual(round(dp_mat.get(rand_row, rand_col), decimal_places),
            round(nc_mat.get(rand_row, rand_col), decimal_places))

class TestSet(TestCase):
    def test_set_small(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        dp_mat.set(rand_row, rand_col, 2)
        nc_mat.set(rand_row, rand_col, 2)
        self.assertTrue(cmp_dp_nc_matrix(dp_mat, nc_mat))


    def test_set_medium(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 128, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        dp_mat.set(rand_row, rand_col, 219)
        nc_mat.set(rand_row, rand_col, 918)
        self.assertTrue(cmp_dp_nc_matrix(dp_mat, nc_mat))

    def test_set_large(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 4096, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        dp_mat.set(rand_row, rand_col, 3)
        nc_mat.set(rand_row, rand_col, 3)
        self.assertTrue(cmp_dp_nc_matrix(dp_mat, nc_mat))

class TestShape(TestCase):
    def test_shape_small(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        self.assertTrue(dp_mat.shape == nc_mat.shape)
        
    def test_shape_medium(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 128, seed=0)
        self.assertTrue(dp_mat.shape == nc_mat.shape)

    def test_shape_large(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 4096, seed=0)
        self.assertTrue(dp_mat.shape == nc_mat.shape)
        
class TestIndexGet(TestCase):
    def test_index_get_small(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        self.assertEqual(round(dp_mat[rand_row][rand_col], decimal_places),
            round(nc_mat[rand_row][rand_col], decimal_places))

    def test_index_get_medium(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 128, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        self.assertEqual(round(dp_mat[rand_row][rand_col], decimal_places),
            round(nc_mat[rand_row][rand_col], decimal_places))

    def test_index_get_large(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2048, 4096, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        self.assertEqual(round(dp_mat[rand_row][rand_col], decimal_places),
            round(nc_mat[rand_row][rand_col], decimal_places))


class TestIndexSet(TestCase):
    def test_set_small(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        dp_mat[rand_row][rand_col] = 2
        nc_mat[rand_row][rand_col] = 2
        self.assertTrue(cmp_dp_nc_matrix(dp_mat, nc_mat))
        self.assertEqual(nc_mat[rand_row][rand_col], 2)

    def test_set_medium(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(64, 128, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        dp_mat[rand_row][rand_col] = 2
        nc_mat[rand_row][rand_col] = 2
        self.assertTrue(cmp_dp_nc_matrix(dp_mat, nc_mat))
        self.assertEqual(nc_mat[rand_row][rand_col], 2)


    def test_set_large(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(4096, 2048, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        dp_mat[rand_row][rand_col] = 2
        nc_mat[rand_row][rand_col] = 2
        self.assertTrue(cmp_dp_nc_matrix(dp_mat, nc_mat))
        self.assertEqual(nc_mat[rand_row][rand_col], 2)

class TestSlice(TestCase):
    def test_slice_small(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row_1 = np.random.randint(dp_mat.shape[0])
        rand_row_2 = np.random.randint(dp_mat.shape[0])
        self.assertTrue(cmp_dp_nc_matrix(dp_mat[rand_row_1], nc_mat[rand_row_1]))
        self.assertTrue(cmp_dp_nc_matrix(dp_mat[rand_row_2], nc_mat[rand_row_2]))

    def test_slice_medium(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row_1 = np.random.randint(dp_mat.shape[0])
        rand_row_2 = np.random.randint(dp_mat.shape[0])
        self.assertTrue(cmp_dp_nc_matrix(dp_mat[rand_row_1], nc_mat[rand_row_1]))
        self.assertTrue(cmp_dp_nc_matrix(dp_mat[rand_row_2], nc_mat[rand_row_2]))

    def test_slice_large(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row_1 = np.random.randint(dp_mat.shape[0])
        rand_row_2 = np.random.randint(dp_mat.shape[0])
        self.assertTrue(cmp_dp_nc_matrix(dp_mat[rand_row_1], nc_mat[rand_row_1]))
        self.assertTrue(cmp_dp_nc_matrix(dp_mat[rand_row_2], nc_mat[rand_row_2]))

