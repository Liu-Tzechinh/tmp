#include "matrix.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

/*
 * optimization 0: naive no function call -> _nnfd
 * optimization 1: no function call and no index compute -> nfd
 * optimization 2: _simd
 */
#define OPTION 0

// Include SSE intrinsics
#if defined(_MSC_VER)
#include <intrin.h>
#elif defined(__GNUC__) && (defined(__x86_64__) || defined(__i386__))
#include <immintrin.h>
#include <x86intrin.h>
#endif


/* Generates a random double between low and high */
double rand_double(double low, double high) {
    double range = (high - low);
    double div = RAND_MAX / range;
    return low + (rand() / div);
}

/* Generates a random matrix */
void rand_matrix(matrix *result, unsigned int seed, double low, double high) {
  srand(seed);
  for (int i = 0; i < result->rows; i++) {
    for (int j = 0; j < result->cols; j++) {
      //            set(result, i, j, rand_double(low, high));
      result->data[i * result->cols + j] = rand_double(low, high);
    }
  }
}

int size(matrix *mat) {
  return mat->rows * mat->cols;
}
/*
 * Returns the double value of the matrix at the given row and column.
 * You may assume `row` and `col` are valid. Note that the matrix is in row-major order.
 */
double get(matrix *mat, int row, int col) {
    // Task 1.1 TODO
  int index = mat->cols * row + col;
  return mat->data[index];
}

/*
 * Sets the value at the given row and column to val. You may assume `row` and
 * `col` are valid. Note that the matrix is in row-major order.
 */
void set(matrix *mat, int row, int col, double val) {
    // Task 1.1 TODO
  int index = mat->cols * row + col;
  mat->data[index] = val;
}

/*
 * Allocates space for a matrix struct pointed to by the double pointer mat with
 * `rows` rows and `cols` columns. You should also allocate memory for the data array
 * and initialize all entries to be zeros. `parent` should be set to NULL to indicate that
 * this matrix is not a slice. You should also set `ref_cnt` to 1.
 * You should return -1 if either `rows` or `cols` or both have invalid values. Return -2 if any
 * call to allocate memory in this function fails.
 * Return 0 upon success.
 */
int allocate_matrix(matrix **mat, int rows, int cols) {
  // Task 1.2 TODO
  // HINTS: Follow these steps.
  // 1. Check if the dimensions are valid. Return -1 if either dimension is not positive.
  if (rows < 1 || cols < 1) {
    return -1;
  }

  // 2. Allocate space for the new matrix struct. Return -2 if allocating memory failed.
  matrix *new_mat = malloc(sizeof(matrix));
  if (!new_mat) {
    return -2;
  }
  // 3. Allocate space for the matrix data, initializing all entries to be 0. Return -2 if allocating memory failed.
  new_mat->data = calloc(rows * cols, sizeof(double));
  if (!new_mat->data) {
    return -2;
  }
  // 4. Set the number of rows and columns in the matrix struct according to the arguments provided.
  new_mat->rows = rows;
  new_mat->cols = cols;
  // 5. Set the `parent` field to NULL, since this matrix was not created from a slice.
  new_mat->parent = NULL;
  // 6. Set the `ref_cnt` field to 1.
  new_mat->ref_cnt = 1;
  // 7. Store the address of the allocated matrix struct at the location `mat` is pointing at.
  *mat = new_mat;
  // 8. Return 0 upon success.
  return 0;
}

/*
 * You need to make sure that you only free `mat->data` if `mat` is not a slice and has no existing slices,
 * or that you free `mat->parent->data` if `mat` is the last existing slice of its parent matrix and its parent
 * matrix has no other references (including itself).
 */
void deallocate_matrix(matrix *mat) {
  // Task 1.3 TODO
  // HINTS: Follow these steps.
  // 1. If the matrix pointer `mat` is NULL, return.
  if (!mat) {
    return;
  }
  // 2. If `mat` has no parent: decrement its `ref_cnt` field by 1. If the `ref_cnt` field becomes 0, then free `mat` and its `data` field.
  if (!mat->parent) { // mat is not a slice
    mat->ref_cnt--;
    if (!mat->ref_cnt) {
      free(mat->data);
      free(mat);
    }
  } 
  // 3. Otherwise, recursively call `deallocate_matrix` on `mat`'s parent, then free `mat`.
  else {
    // from spec of summer 2021: Partial slices, however, are not supported
    // so mat[0][1:3] is impossible.
    deallocate_matrix(mat->parent);
    free(mat);
  }
}

/*
 * Allocates space for a matrix struct pointed to by `mat` with `rows` rows and `cols` columns.
 * Its data should point to the `offset`th entry of `from`'s data (you do not need to allocate memory)
 * for the data field. `parent` should be set to `from` to indicate this matrix is a slice of `from`
 * and the reference counter for `from` should be incremented. Lastly, do not forget to set the
 * matrix's row and column values as well.
 * You should return -1 if either `rows` or `cols` or both have invalid values. Return -2 if any
 * call to allocate memory in this function fails.
 * Return 0 upon success.
 * NOTE: Here we're allocating a matrix struct that refers to already allocated data, so
 * there is no need to allocate space for matrix data.
 */
int allocate_matrix_ref(matrix **mat, matrix *from, int offset, int rows, int cols) {
  // Task 1.4 TODO
  // HINTS: Follow these steps.
  // 1. Check if the dimensions are valid. Return -1 if either dimension is not positive.
  if (rows < 1 || cols < 1) {
    return -1;
  }
  // 2. Allocate space for the new matrix struct. Return -2 if allocating memory failed.
  matrix *new_mat = malloc(sizeof(matrix));
  if (!new_mat) {
    return -2;
  }
  // 3. Set the `data` field of the new struct to be the `data` field of the `from` struct plus `offset`.
  new_mat->data = from->data + offset;
  // 4. Set the number of rows and columns in the new struct according to the arguments provided.
  new_mat->rows = rows;
  new_mat->cols = cols;
  // 5. Set the `parent` field of the new struct to the `from` struct pointer.
  new_mat->parent = from;
  // 6. Increment the `ref_cnt` field of the `from` struct by 1.
  from->ref_cnt++;
  new_mat->ref_cnt = 1;
  // 7. Store the address of the allocated matrix struct at the location `mat` is pointing at.
  *mat = new_mat;
  // 8. Return 0 upon success.
  return 0;
}

void fill_nnfd(matrix *mat, double val) {
  for (int i = 0; i < mat->rows; i++) {
    for (int j = 0; j < mat->cols; j++) {
      mat->data[i * mat->cols + j] = val;
    }
  }
}

void fill_nfd(matrix *mat, double val) {
  int n = size(mat);
  for (int i = 0; i < n; i++) {
    mat->data[i] = val;
  }
}

void fill_simd(matrix *mat, double val) {
  __m256d vals = _mm256_set1_pd(val);
  int n = size(mat);
  for (int i = 0; i < n / 4 * 4; i += 4) {
    _mm256_storeu_pd(mat->data+i, vals);
  }
  for (int i = n / 4 * 4; i < n; i++) {
    mat->data[i] = val;
  }
}

/*
 * Sets all entries in mat to val. Note that the matrix is in row-major order.
 */
void fill_matrix(matrix *mat, double val) {
  // Task 1.5 TODO
  fill_simd(mat, val);
}


int abs_nnfd(matrix *result, matrix *mat) {
  int index;
  for (int i = 0; i < mat->rows; i++) {
    for (int j = 0; j < mat->cols; j++) {
      index = i * mat->cols + j;
      result->data[index] = fabs(mat->data[index]);
    }
  }
  return 0;
}

int abs_nfd(matrix *result, matrix *mat) {
  int n = size(mat);
  for (int i = 0; i < n; i++) {
    result->data[i] = fabs(mat->data[i]);
  }
  return 0;
}

int abs_simd(matrix *result, matrix *mat) {
   __m256d _0 = _mm256_set1_pd(0);
   int n = size(mat);
  __m256d vals1, vals2;
  for (int i = 0; i < n / 4 * 4; i += 4) {
    vals1 = _mm256_loadu_pd(mat->data + i);
    vals2 = _mm256_sub_pd(_0, vals1);
    vals1 = _mm256_max_pd(vals1, vals2);
    _mm256_storeu_pd(result->data+i, vals1);
  }
  for (int i = n / 4 * 4; i < n; i++) {
    result->data[i] = fabs(mat->data[i]);
  }
  return 0;
}

/*
 * Store the result of taking the absolute value element-wise to `result`.
 * Return 0 upon success.
 * Note that the matrix is in row-major order.
 */
int abs_matrix(matrix *result, matrix *mat) {
    // Task 1.5 TODO
  switch (OPTION) {
  case 0:
    return abs_nnfd(result, mat);
  case 1:
    return abs_nfd(result, mat);
  case 2:
    return abs_simd(result, mat);
  }
}

int neg_nnfd(matrix *result, matrix *mat) {
  int index;
  for (int i = 0; i < mat->rows; i++) {
    for (int j = 0; j < mat->cols; j++) {
      index = i * mat->cols + j;
      result->data[index] = -fabs(mat->data[index]);
    }
  }
}

int neg_nfd(matrix *result, matrix *mat) {
  int n = size(mat);
  for (int i = 0; i < n; i++) {
    result->data[i] = -fabs(mat->data[i]);
    }
  }
}


int neg_simd(matrix *result, matrix *mat) {
   __m256d _0 = _mm256_set1_pd(0);
   int n = size(mat);
  __m256d vals1, vals2;
  for (int i = 0; i < n / 4 * 4; i += 4) {
    vals1 = _mm256_loadu_pd(mat->data + i);
    vals2 = _mm256_sub_pd(_0, vals1);
    vals1 = _mm256_min_pd(vals1, vals2);
    _mm256_storeu_pd(result->data+i, vals1);
  }
  for (int i = n / 4 * 4; i < n; i++) {
    result->data[i] = -fabs(mat->data[i]);
  }
  return 0;
}

/*
 * (OPTIONAL)
 * Store the result of element-wise negating mat's entries to `result`.
 * Return 0 upon success.
 * Note that the matrix is in row-major order.
 */
int neg_matrix(matrix *result, matrix *mat) {
    // Task 1.5 TODO
  switch (OPTION) {
  case 0:
    return neg_nnfd(result, mat);
  case 1:
    return neg_nfd(result, mat);
  case 2:
    return neg_simd(result, mat);
  }
}

int add_nnfd(matrix *result, matrix *mat1, matrix *mat2) {
  int index;
  for (int i = 0; i < mat1->rows; i++) {
    for (int j = 0; j < mat1->cols; j++) {
      index = i * mat1->cols + j;
      result->data[index] = mat1->data[index] + mat2->data[index];
    }
  }
  return 0;
}

int add_nfd(matrix *result, matrix *mat1, matrix *mat2) {
  int n = size(mat1);
  for (int i = 0; i < n; i++) {
    result->data[i] = mat1->data[i] + mat2->data[i];
  }
  return 0;
}

int add_simd(matrix *result, matrix *mat1, matrix *mat2) {
  int n = size(mat1);
  __m256d vals1, vals2, sum;
  for (int i = 0; i < n / 4 * 4; i += 4) {
    vals1 = _mm256_loadu_pd(mat1->data + i);
    vals2 = _mm256_loadu_pd(mat2->data + i);
    sum = _mm256_add_pd(vals1, vals2);
    _mm256_storeu_pd(result->data+i, sum);
  }
  for (int i = n / 4 * 4; i < n; i++) {
    result->data[i] = mat1->data[i] + mat2->data[i];
  }
  return 0;
}

int add_nfd_mp(matrix *result, matrix *mat1, matrix *mat2) {
  int n = size(mat1);
  #pragma omp parallel for
  for (int i = 0; i < n; i++) {
    result->data[i] = mat1->data[i] + mat2->data[i];
  }
  return 0;
}

int add_simd_mp(matrix *result, matrix *mat1, matrix *mat2) {
  int n = size(mat1);
  __m256d vals1, vals2, sum;
#pragma omp parallel for private(vals1, vals2, sum)
  for (int i = 0; i < n / 4 * 4; i += 4) {
    vals1 = _mm256_loadu_pd(mat1->data + i);
    vals2 = _mm256_loadu_pd(mat2->data + i);
    sum = _mm256_add_pd(vals1, vals2);
    _mm256_storeu_pd(result->data+i, sum);
  }
  
  for (int i = n / 4 * 4; i < n; i++) {
    result->data[i] = mat1->data[i] + mat2->data[i];
  }
  return 0;
}
/*
 * Store the result of adding mat1 and mat2 to `result`.
 * Return 0 upon success.
 * You may assume `mat1` and `mat2` have the same dimensions.
 * Note that the matrix is in row-major order.
 */
int add_matrix(matrix *result, matrix *mat1, matrix *mat2) {
    // Task 1.5 TODO
  switch(OPTION) {
  case 0:
    return add_nnfd(result, mat1, mat2);
  case 1:
    return add_nfd(result, mat1, mat2);
  case 2:
    return add_simd(result, mat1, mat2);
  }
}

int sub_nnfd(matrix *result, matrix *mat1, matrix *mat2) {
  // Task 1.5 TODO
  int index;
  for (int i = 0; i < mat1->rows; i++) {
    for (int j = 0; j < mat1->cols; j++) {
      index = i * mat1->cols + j;
      result->data[index] = mat1->data[index] - mat2->data[index];
    }
  }
  return 0;
}

int sub_nfd(matrix *result, matrix *mat1, matrix *mat2) {
  // Task 1.5 TODO
  int n = size(result);
  for (int i = 0; i < n; i++) {
    result->data[i] = mat1->data[i] - mat2->data[i];
  }
  return 0;
}


int sub_simd(matrix *result, matrix *mat1, matrix *mat2) {
  int n = size(mat1);
  __m256d vals1, vals2, sub;
  for (int i = 0; i < n / 4 * 4; i += 4) {
    vals1 = _mm256_loadu_pd(mat1->data + i);
    vals2 = _mm256_loadu_pd(mat2->data + i);
    sub = _mm256_sub_pd(vals1, vals2);
    _mm256_storeu_pd(result->data+i, sub);
  }
  for (int i = n / 4 * 4; i < n; i++) {
    result->data[i] = mat1->data[i] + mat2->data[i];
  }
  return 0;
}
/*
 * (OPTIONAL)
 * Store the result of subtracting mat2 from mat1 to `result`.
 * Return 0 upon success.
 * You may assume `mat1` and `mat2` have the same dimensions.
 * Note that the matrix is in row-major order.
 */
int sub_matrix(matrix *result, matrix *mat1, matrix *mat2) {
  // Task 1.5 TODO
  switch(OPTION) {
  case 0:
    return sub_nnfd(result, mat1, mat2);
  case 1:
    return sub_nfd(result, mat1, mat2);
  case 2:
    return sub_simd(result, mat1, mat2);
  }
}

int tran_nnfd(matrix *result, matrix *mat) {
  int index;
  for (int i = 0; i < mat->rows; i++) {
    for (int j = 0; j < mat->cols; j++) {
      result->data[j * result->cols + i] = mat->data[i * mat->cols + j];
    }
  }
  return 0;
}


int tran_simd(matrix *result, matrix *mat) {
  double e1, e2, e3, e4;
  int n = size(result);
  int rows = mat->rows;
  int cols = mat->cols;
  int row = -1;
  int col = -1;
  __m256d val = _mm256_set1_pd(0);
  for (int k = 0; k < n / 4 * 4; k += 4) {
    row = (row + 1) % rows;
    if (!row) { 
      col++;
    }
    e1 = mat->data[row * cols + col];
    row = (row + 1) % rows;
    if (!row) {
      col++;
    }
    e2 = mat->data[row * cols + col];
    row = (row + 1) % rows;
    if (!row) {
      col++;
    }
    e3 = mat->data[row * cols + col];
    row = (row + 1) % rows;
    if (!row) {
      col++;
    }
    e4 = mat->data[row * cols + col];
    val = _mm256_set_pd(e1, e2, e3, e4);
    _mm256_storeu_pd(result->data + k, val);
  }
  for (int k = n / 4 * 4; k < n; k++) {
    row = (row + 1) % rows;
    if (!row) {
      col++;
    }
    result->data[k] = mat->data[row * cols + col];
  }
  return 0;
}

int tran_matrix(matrix *result, matrix *mat) {
  switch(OPTION) {
  case 0:
    return tran_nnfd(result, mat1, mat2);
  case 1:
    return tran_nfd(result, mat1, mat2);
  case 2:
    return tran_simd(result, mat1, mat2);
  }
}

int mul_nnfd(matrix *result, matrix *mat1, matrix *mat2) {
    // Task 1.6 TODO
  for (int i = 0; i < mat1->rows; i++) {
    for (int k = 0; k < mat2->cols; k++) {
      double sum = 0;
      for (int j = 0; j < mat1->cols; j++) {
	sum += (mat1->data[i * mat1->cols + j] * mat2->data[j * mat2->cols + k]);
      }
      result->data[i $ result->cols + k] = sum;
    }
  }
  return 0;
}

int mul_simd(matrix *result, matrix *mat1, matrix *mat2) {
  // transpose mat2
  matrix *tmp;
  if (allocate_matrix(&tmp, mat2->cols, mat2->rows)) {
    return -1;
  }
  tran_matrix(tmp, mat2);

  __m256d vals1, vals2, vals3;
  double sum_array[4];// __attribute__ ((aligned(32)));
  for (int i = 0; i < mat1->rows; i++) {
    for (int k = 0; k < tmp->rows; k++) {
      vals3 = _mm256_set1_pd(0);
      for (int j = 0; j < mat1->cols / 4 * 4; j += 4) {
	vals1 = _mm256_loadu_pd(mat1->data + i * mat1->cols + j);
	vals2 = _mm256_loadu_pd(tmp->data + k * tmp->cols + j);
	vals3 = _mm256_fmadd_pd(vals1, vals2, vals3);
      }
      _mm256_storeu_pd(sum_array, vals3);
      result->data[i * mat2->cols + k] = sum_array[0] + sum_array[1] + sum_array[2] + sum_array[3];
      for (int j = mat1->cols / 4 * 4; j < mat1->cols; j++) {
	result->data[i * mat2->cols + k] += (mat1->data[i * mat1->cols + j] * tmp->data[k * tmp->cols + j]);
      }
    }
  }
  return 0;
}

/*
 * Store the result of multiplying mat1 and mat2 to `result`.
 * Return 0 upon success.
 * Remember that matrix multiplication is not the same as multiplying individual elements.
 * You may assume `mat1`'s number of columns is equal to `mat2`'s number of rows.
 * Note that the matrix is in row-major order.
 */
int mul_matrix(matrix *result, matrix *mat1, matrix *mat2) {
  switch(OPTION) {
  case 0:
    return mul_nnfd(result, mat1, mat2);
  case 1:
    return mul_nnfd(result, mat1, mat2);
  case 2:
    return mul_simd(result, mat1, mat2);
  }
}

/*
 * Store the result of raising mat to the (pow)th power to `result`.
 * Return 0 upon success.
 * Remember that pow is defined with matrix multiplication, not element-wise multiplication.
 * You may assume `mat` is a square matrix and `pow` is a non-negative integer.
 * Note that the matrix is in row-major order.
 */
int pow_matrix(matrix *result, matrix *mat, int pow) {
  // Task 1.6 TODO
  double value = 0;
  for (int i = 0; i < mat->rows; i++) {
    for (int j = 0; j < mat->cols; j++) {
      if (i == j) {
	value = 1;
      } else {
	value = 0;
      }
      set(result, i, j, value);
    }
  }
  matrix *tmp;
  allocate_matrix(&tmp, mat->rows, mat->cols);
  for (int k = 0; k < pow; k++) {
    mul_matrix(tmp, result, mat);
    for (int i = 0; i < mat->rows; i++) {
      for (int j = 0; j < mat->cols; j++) {
	set(result, i, j, get(tmp, i, j));
      }
    }
  }
  deallocate_matrix(tmp);
  return 0;
}
