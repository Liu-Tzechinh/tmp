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
        print_speedup(speed_up)

    def test_small_add_4(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4, 4, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4, 4, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_small_add_8(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8, 8, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8, 8, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_small_add_16(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16, 16, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16, 16, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_add_32(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32, 32, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32, 32, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_add_64(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(64, 64, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(64, 64, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_add_128(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(128, 128, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(128, 128, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_add_256(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(256, 256, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(256, 256, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_medium_add_512(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(512, 512, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(512, 512, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_add_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(1024, 1024, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(1024, 1024, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_add_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2048, 2048, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2048, 2048, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_add_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4096, 4096, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4096, 4096, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_add_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8192, 8192, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8192, 8192, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_large_add_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16384, 16384, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16384, 16384, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_add_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32768, 32768, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32768, 32768, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_large_add_65536(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(65536, 65536, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(65536, 65536, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "add")
        self.assertTrue(is_correct)
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
        print_speedup(speed_up)

#    def test_medium_sub(self):
#        # TODO: YOUR CODE HERE
#        pass
#
#    def test_large_sub(self):
#        # TODO: YOUR CODE HERE
#        pass
    def test_small_sub_4(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4, 4, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4, 4, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_small_sub_8(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8, 8, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8, 8, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_small_sub_16(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16, 16, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16, 16, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_sub_32(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32, 32, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32, 32, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_sub_64(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(64, 64, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(64, 64, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_sub_128(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(128, 128, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(128, 128, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_sub_256(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(256, 256, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(256, 256, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_medium_sub_512(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(512, 512, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(512, 512, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_sub_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(1024, 1024, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(1024, 1024, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_sub_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2048, 2048, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2048, 2048, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_sub_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4096, 4096, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4096, 4096, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_sub_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8192, 8192, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8192, 8192, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_large_sub_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16384, 16384, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16384, 16384, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_sub_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32768, 32768, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32768, 32768, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_large_sub_65536(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(65536, 65536, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(65536, 65536, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "sub")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

class TestAbs(TestCase):
    def test_small_abs(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        is_correct, speed_up = compute([dp_mat], [nc_mat], "abs")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_abs(self):
        # TODO: YOUR CODE HERE
        pass

    def test_large_abs(self):
        # TODO: YOUR CODE HERE
        pass

# (OPTIONAL) Uncomment the following TestNeg class if you have implemented matrix negation.
# class TestNeg(TestCase):
#    def test_small_neg(self):
#        # TODO: YOUR CODE HERE
#        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
#        is_correct, speed_up = compute([dp_mat], [nc_mat], "neg")
#        self.assertTrue(is_correct)
#        print_speedup(speed_up)
#    def test_medium_neg(self):
#        # TODO: YOUR CODE HERE
#        pass

#    def test_large_neg(self):
#        # TODO: YOUR CODE HERE
#        pass

class TestMul(TestCase):
    def test_small_mul_2(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2, 2, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2, 2, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_mul(self):
        # TODO: YOUR CODE HERE
        pass

    def test_large_mul(self):
        # TODO: YOUR CODE HERE
        pass
    def test_small_mul_4(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4, 4, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4, 4, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_small_mul_8(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8, 8, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8, 8, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_small_mul_16(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16, 16, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16, 16, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_mul_32(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32, 32, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32, 32, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_mul_64(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(64, 64, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(64, 64, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_mul_128(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(128, 128, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(128, 128, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_mul_256(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(256, 256, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(256, 256, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_medium_mul_512(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(512, 512, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(512, 512, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_mul_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(1024, 1024, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(1024, 1024, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_mul_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2048, 2048, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2048, 2048, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_mul_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4096, 4096, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4096, 4096, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_mul_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8192, 8192, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8192, 8192, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_large_mul_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16384, 16384, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16384, 16384, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_mul_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32768, 32768, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32768, 32768, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_large_mul_65536(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(65536, 65536, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(65536, 65536, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "mul")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

class TestPow(TestCase):
    def test_small_pow_2(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        is_correct, speed_up = compute([dp_mat, 3], [nc_mat, 3], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_pow(self):
        # TODO: YOUR CODE HERE
        pass

    def test_large_pow(self):
        # TODO: YOUR CODE HERE
        pass
    def test_small_pow_4(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4, 4, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4, 4, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_small_pow_8(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8, 8, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8, 8, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_small_pow_16(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16, 16, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16, 16, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_pow_32(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32, 32, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32, 32, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_pow_64(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(64, 64, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(64, 64, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_pow_128(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(128, 128, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(128, 128, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_pow_256(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(256, 256, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(256, 256, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_medium_pow_512(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(512, 512, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(512, 512, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_medium_pow_1024(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(1024, 1024, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(1024, 1024, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_pow_2048(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(2048, 2048, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(2048, 2048, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_pow_4096(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(4096, 4096, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(4096, 4096, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_pow_8192(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(8192, 8192, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(8192, 8192, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_large_pow_16384(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(16384, 16384, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(16384, 16384, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

    def test_large_pow_32768(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(32768, 32768, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(32768, 32768, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)


    def test_large_pow_65536(self):
        # TODO: YOUR CODE HERE
        dp_mat1, nc_mat1 = rand_dp_nc_matrix(65536, 65536, seed=0)
        dp_mat2, nc_mat2 = rand_dp_nc_matrix(65536, 65536, seed=1)
        is_correct, speed_up = compute([dp_mat1, dp_mat2], [nc_mat1, nc_mat2], "pow")
        self.assertTrue(is_correct)
        print_speedup(speed_up)

class TestGet(TestCase):
    def test_get(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        self.assertEqual(round(dp_mat.get(rand_row, rand_col), decimal_places),
            round(nc_mat.get(rand_row, rand_col), decimal_places))

class TestSet(TestCase):
    def test_set(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        dp_mat.set(rand_row, rand_col, 2)
        nc_mat.set(rand_row, rand_col, 2)
        self.assertTrue(cmp_dp_nc_matrix(dp_mat, nc_mat))

class TestShape(TestCase):
    def test_shape(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        self.assertTrue(dp_mat.shape == nc_mat.shape)

class TestIndexGet(TestCase):
    def test_index_get(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        self.assertEqual(round(dp_mat[rand_row][rand_col], decimal_places),
            round(nc_mat[rand_row][rand_col], decimal_places))

class TestIndexSet(TestCase):
    def test_set(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        rand_row = np.random.randint(dp_mat.shape[0])
        rand_col = np.random.randint(dp_mat.shape[1])
        dp_mat[rand_row][rand_col] = 2
        nc_mat[rand_row][rand_col] = 2
        self.assertTrue(cmp_dp_nc_matrix(dp_mat, nc_mat))
        self.assertEqual(nc_mat[rand_row][rand_col], 2)

class TestSlice(TestCase):
    def test_slice(self):
        # TODO: YOUR CODE HERE
        dp_mat, nc_mat = rand_dp_nc_matrix(2, 2, seed=0)
        self.assertTrue(cmp_dp_nc_matrix(dp_mat[0], nc_mat[0]))
        self.assertTrue(cmp_dp_nc_matrix(dp_mat[1], nc_mat[1]))
