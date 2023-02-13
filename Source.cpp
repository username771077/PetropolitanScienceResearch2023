#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

void matmul(int M, int N, int K, float* A, float* B, float* C)
{
#pragma omp parallel for
    for (int i = 0; i < M; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            C[i * N + j] = 0;
            for (int k = 0; k < K; ++k)
                C[i * N + j] += A[i * K + k] * B[k * N + j];
        }
    }
}

int main(int argc, char* argv[])
{
    int M = 1000, N = 1000, K = 1000;
    float* A = (float*)malloc(M * K * sizeof(float));
    float* B = (float*)malloc(K * N * sizeof(float));
    float* C = (float*)malloc(M * N * sizeof(float));

    // Initialize matrices with some data

    matmul(M, N, K, A, B, C);

    free(A);
    free(B);
    free(C);
    return 0;
}
